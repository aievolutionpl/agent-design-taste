#!/usr/bin/env node
/**
 * Rendered verification — screenshot a page at the canonical viewports and
 * report the faults you cannot see in code.
 *
 *   node scripts/screenshot.mjs                      # all 15 style examples
 *   node scripts/screenshot.mjs 10                   # one style, by id or slug
 *   node scripts/screenshot.mjs http://localhost:3000
 *   node scripts/screenshot.mjs ./dist/index.html
 *
 * Output goes to screenshots/ (gitignored — do not commit binaries).
 *
 * Requires Playwright:  npm i -D playwright && npx playwright install chromium
 */
import { chromium } from 'playwright';
import { readdirSync, mkdirSync, existsSync } from 'node:fs';
import { resolve, dirname, join } from 'node:path';
import { pathToFileURL } from 'node:url';

const ROOT = resolve(dirname(new URL(import.meta.url).pathname), '..');
const OUT = join(ROOT, 'screenshots');

// The canonical viewport ladder. Do not add others without changing SKILL.md.
const VIEWPORTS = [
  { name: 'desktop', width: 1440, height: 900 },
  { name: 'tablet', width: 768, height: 1024 },
  { name: 'mobile', width: 390, height: 844 },   // canonical — check this first
  { name: 'narrow', width: 360, height: 800 },   // narrow floor — overflow only
];

function targets(arg) {
  if (!arg) {
    return readdirSync(join(ROOT, 'styles'), { withFileTypes: true })
      .filter((d) => d.isDirectory())
      .map((d) => ({ name: d.name, url: pathToFileURL(join(ROOT, 'styles', d.name, 'example.html')).href }));
  }
  if (/^https?:\/\//.test(arg)) return [{ name: 'page', url: arg }];
  const dirs = readdirSync(join(ROOT, 'styles'));
  const match = dirs.find((d) => d === arg || d.startsWith(`${arg}-`));
  if (match) {
    return [{ name: match, url: pathToFileURL(join(ROOT, 'styles', match, 'example.html')).href }];
  }
  const p = resolve(arg);
  if (!existsSync(p)) {
    console.error(`not found: ${arg} (expected a style id/slug, a file path, or a URL)`);
    process.exit(2);
  }
  return [{ name: 'page', url: pathToFileURL(p).href }];
}

const list = targets(process.argv[2]);
mkdirSync(OUT, { recursive: true });

const browser = await chromium.launch();
let blockers = 0;

for (const target of list) {
  console.log(`\n${target.name}`);
  for (const vp of VIEWPORTS) {
    const ctx = await browser.newContext({
      viewport: { width: vp.width, height: vp.height },
      deviceScaleFactor: 1,
      reducedMotion: vp.name === 'narrow' ? 'reduce' : 'no-preference',
    });
    const page = await ctx.newPage();
    await page.goto(target.url, { waitUntil: 'networkidle' }).catch(() => {});
    await page.waitForTimeout(350);

    const metrics = await page.evaluate(() => {
      const de = document.documentElement;
      let widest = null;
      let widestOverflow = 0;
      for (const el of document.body.querySelectorAll('*')) {
        const r = el.getBoundingClientRect();
        const over = Math.round(r.right - de.clientWidth);
        if (over > widestOverflow) {
          widestOverflow = over;
          widest = el.tagName.toLowerCase() + (el.className && typeof el.className === 'string'
            ? '.' + el.className.trim().split(/\s+/)[0] : '');
        }
      }
      const tiny = [...document.querySelectorAll('a,button,input,select,[role="button"]')]
        .filter((el) => {
          const r = el.getBoundingClientRect();
          return r.width > 0 && (r.width < 44 || r.height < 44);
        }).length;
      return {
        scrollW: de.scrollWidth,
        clientW: de.clientWidth,
        widest,
        widestOverflow,
        tiny,
      };
    });

    const overflow = metrics.scrollW > metrics.clientW + 1;
    const isMobile = vp.width <= 390;
    const file = join(OUT, `${target.name}--${vp.name}-${vp.width}.png`);
    await page.screenshot({ path: file, fullPage: true });

    const flags = [];
    if (overflow) {
      flags.push(`horizontal overflow +${metrics.scrollW - metrics.clientW}px` +
        (metrics.widest ? ` (widest: ${metrics.widest})` : ''));
      if (isMobile) blockers++;
    }
    if (isMobile && metrics.tiny > 0) flags.push(`${metrics.tiny} touch target(s) < 44px`);

    const status = flags.length ? (isMobile && overflow ? '🔴' : '🟠') : '  ';
    console.log(`  ${status} ${vp.name.padEnd(8)} ${String(vp.width).padStart(4)}px  ` +
      (flags.length ? flags.join(' · ') : 'clean'));

    await ctx.close();
  }
}

await browser.close();
console.log(`\nscreenshots → ${OUT}`);
if (blockers) {
  console.log(`\n🔴 ${blockers} BLOCKER(s): horizontal overflow at a mobile viewport.`);
  console.log('   See ANTI-SLOP.md and evaluation/DESIGN-TASTE-SCORE.md (B2).');
  process.exit(1);
}
console.log('\nNo blockers detected. Now LOOK at the screenshots — the checks above');
console.log('catch overflow and touch targets; they cannot see hierarchy or taste.');
