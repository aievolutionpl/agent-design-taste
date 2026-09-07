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
    // 'load' + fonts.ready rather than 'networkidle': a page with webfonts or a
    // long-lived connection never goes idle, and waiting for that is minutes of
    // nothing. Layout is settled once fonts have swapped in.
    await page.goto(target.url, { waitUntil: 'load', timeout: 20_000 }).catch(() => {});
    await page.evaluate(() => document.fonts?.ready).catch(() => {});
    await page.waitForTimeout(250);

    const metrics = await page.evaluate(() => {
      const de = document.documentElement;
      const label = (el) => el.tagName.toLowerCase() +
        (typeof el.className === 'string' && el.className.trim()
          ? '.' + el.className.trim().split(/\s+/)[0] : '');

      // An element clipped by an ancestor's overflow does not create page scroll,
      // so it must not be blamed for it (deliberate bleed is a valid technique).
      const clipped = (el) => {
        for (let p = el.parentElement; p && p !== de; p = p.parentElement) {
          const ox = getComputedStyle(p).overflowX;
          if (ox === 'hidden' || ox === 'clip' || ox === 'auto' || ox === 'scroll') return true;
        }
        return false;
      };

      let widest = null;
      let widestOverflow = 0;
      for (const el of document.body.querySelectorAll('*')) {
        if (clipped(el)) continue;
        const r = el.getBoundingClientRect();
        const over = Math.round(r.right - de.clientWidth);
        if (over > widestOverflow) { widestOverflow = over; widest = label(el); }
      }

      // WCAG 2.2 SC 2.5.8 exempts targets that sit inline within a sentence or
      // block of text, so an inline link inside a paragraph is not a finding.
      const inlineInText = (el) => {
        if (getComputedStyle(el).display !== 'inline') return false;
        const p = el.parentElement;
        if (!p) return false;
        return (p.textContent || '').trim().length > (el.textContent || '').trim().length + 8;
      };

      const targets = [...document.querySelectorAll('a,button,input,select,[role="button"]')]
        .map((el) => ({ el, r: el.getBoundingClientRect() }))
        .filter((t) => t.r.width > 0 && t.r.height > 0);

      // SC 2.5.8 also exempts an undersized target whose 44px-diameter circle
      // does not overlap any neighbour's — a narrow nav link with real spacing
      // around it is comfortable to tap. Only flag targets that are BOTH
      // undersized and crowded.
      const crowded = (t) => targets.some((o) => {
        if (o.el === t.el) return false;
        const dx = (t.r.left + t.r.width / 2) - (o.r.left + o.r.width / 2);
        const dy = (t.r.top + t.r.height / 2) - (o.r.top + o.r.height / 2);
        return Math.hypot(dx, dy) < 44;
      });

      const small = targets
        .filter(({ el, r }) => {
          if (inlineInText(el)) return false;
          if (r.width >= 44 && r.height >= 44) return false;
          // Height below the comfortable minimum is a finding regardless of
          // spacing — a 15px-tall link is hard to hit even in open space.
          if (r.height < 32) return true;
          return crowded({ el, r });
        })
        .map(({ el }) => el)
        .map((el) => `${label(el)} ${Math.round(el.getBoundingClientRect().width)}x${Math.round(el.getBoundingClientRect().height)}`);

      return { scrollW: de.scrollWidth, clientW: de.clientWidth, widest, widestOverflow, small };
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
    if (isMobile && metrics.small.length > 0) {
      flags.push(`${metrics.small.length} touch target(s) < 44px: ` +
        metrics.small.slice(0, 3).join(', ') + (metrics.small.length > 3 ? ' …' : ''));
    }

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
