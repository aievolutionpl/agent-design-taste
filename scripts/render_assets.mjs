#!/usr/bin/env node
/**
 * Render the data-driven README graphics from source (assets/*.png|jpg): the
 * workflow diagram, the routing chart and the social preview. Every screenshot
 * in them is a real render of a styles/NN/example.html, and every number is
 * computed from styles/index.json at render time. The .webp files in assets/
 * are AI Evolution Polska artwork and are not produced by this script.
 *
 *   node scripts/render_assets.mjs              # capture examples + render all
 *   node scripts/render_assets.mjs banner       # render one source by name
 *   node scripts/render_assets.mjs --no-capture # reuse cached screenshots
 *
 * Sources: assets/src/<name>.html. Each declares its output with
 *   <meta name="adt:out"  content="banner.jpg">
 *   <meta name="adt:size" content="1280x440">     (CSS px; rendered at 2x)
 *   <meta name="adt:full" content="true">         (optional: grow to content height)
 *
 * Example screenshots are cached in assets/.cache/ (gitignored).
 * Requires Playwright: npm i -D playwright && npx playwright install chromium
 */
import { chromium } from 'playwright';
import { readdirSync, readFileSync, mkdirSync, existsSync } from 'node:fs';
import { resolve, dirname, join } from 'node:path';
import { pathToFileURL } from 'node:url';

const ROOT = resolve(dirname(new URL(import.meta.url).pathname), '..');
const SRC = join(ROOT, 'assets', 'src');
const CACHE = join(ROOT, 'assets', '.cache', 'shots');
const args = process.argv.slice(2);
const only = args.filter((a) => !a.startsWith('--'));
const capture = !args.includes('--no-capture');

const index = JSON.parse(readFileSync(join(ROOT, 'styles', 'index.json'), 'utf8'));
const browser = await chromium.launch();

// 1 · capture every example at the canonical desktop and mobile viewports
if (capture) {
  mkdirSync(CACHE, { recursive: true });
  for (const s of index.styles) {
    const url = pathToFileURL(join(ROOT, s.files.example)).href;
    for (const [tag, width, height] of [['desktop', 1440, 900], ['mobile', 390, 844]]) {
      const page = await browser.newPage({ viewport: { width, height }, deviceScaleFactor: tag === 'mobile' ? 2 : 1 });
      await page.goto(url, { waitUntil: 'networkidle' });
      await page.evaluate(() => document.fonts.ready);
      await page.waitForTimeout(1800); // let entrance animations settle
      await page.screenshot({ path: join(CACHE, `${s.slug}-${tag}.jpg`), type: 'jpeg', quality: 92 });
      await page.close();
    }
    console.log(`  shot  ${s.slug}`);
  }
}

// 2 · render each source page into assets/
const sources = readdirSync(SRC).filter((f) => f.endsWith('.html'))
  .filter((f) => !only.length || only.includes(f.replace(/\.html$/, '')));

for (const file of sources) {
  const html = readFileSync(join(SRC, file), 'utf8');
  const out = html.match(/name="adt:out"\s+content="([^"]+)"/)?.[1];
  const size = html.match(/name="adt:size"\s+content="(\d+)x(\d+)"/);
  if (!out || !size) { console.log(`  skip  ${file} (no adt:out / adt:size)`); continue; }
  const [width, height] = [Number(size[1]), Number(size[2])];
  const page = await browser.newPage({ viewport: { width, height }, deviceScaleFactor: 2 });
  await page.addInitScript((data) => { window.ADT = data; }, {
    styles: index.styles, signals: index.signals,
    shots: pathToFileURL(CACHE).href + '/',
  });
  await page.goto(pathToFileURL(join(SRC, file)).href, { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(300);
  // Fixed-size art clips to adt:size; long art opts in with <meta name="adt:full" content="true">.
  const grow = /name="adt:full"\s+content="true"/.test(html);
  const full = grow ? await page.evaluate(() => document.documentElement.scrollHeight) : height;
  const target = join(ROOT, 'assets', out);
  const jpeg = out.endsWith('.jpg');
  await page.screenshot({
    path: target, fullPage: full > height, type: jpeg ? 'jpeg' : 'png',
    ...(jpeg ? { quality: 86 } : {}),
  });
  await page.close();
  console.log(`  ok    assets/${out}  (${width}x${Math.max(full, height)} @2x)`);
}

await browser.close();
if (!existsSync(CACHE)) console.log('\nno screenshot cache — run without --no-capture first');
