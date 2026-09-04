# 04 · Bento Grid

**Overview:** Information as a tiled wall of modular cards — asymmetric cells of different sizes pack one dense, scannable surface. Every tile is a self-contained unit; the grid itself is the composition.

**Visual principles:** asymmetric modular grid · varied tile spans · dense but ordered · one tile always dominates · visible cell boundaries · dashboard-like scanability.

## Typography
- **Recommended families (Google Fonts):** Text/Sans: Inter, Jakarta Sans. Display: Space Grotesk. Mono (labels, metrics): IBM Plex Mono, JetBrains Mono.
- **Pairing:** Space Grotesk (H1–H2, 500–700) + Inter (H3–body) + IBM Plex Mono (tile eyebrows, numbers, metrics).
- **Scale:** H1 52/60 · H2 36/44 · H3 24/32 (tile titles) · H4 20/28 · H5 17/24 · body 16/1.6 · tile body 15/1.5 · small 13/1.5.
- **Body:** 15–16px inside tiles, line-height 1.5. Tile text is compact — measure ~40–50ch.
- **Uppercase:** mono eyebrow labels 11–12px, +0.08em, on tile headers and stat tiles.
- **CSS:**
```css
h1 { font: 600 52px/1.15 'Space Grotesk'; letter-spacing: -0.02em; }
.tile h3 { font: 600 24px/1.3 'Space Grotesk'; }
.tile p { font: 400 15px/1.5 'Inter'; color: var(--color-text-secondary); }
.tile-label { font: 500 11px/1 'IBM Plex Mono'; letter-spacing: .08em; text-transform: uppercase; }
```
- **Typical mistakes:** same font size in every tile (kills hierarchy); body text stretched across wide tiles; centered tile copy; decorative huge numbers with no unit/context.

## Layout & Frames
- **Grid:** CSS Grid with named areas or explicit spans; 12-col base, container 1200–1280px, gap 12–16px (tight gaps read as a bento; 24px+ reads as separate cards).
- **Tile spans:** mix col spans (3/4/5/6/8) and row spans (1/2). Classic rhythm: one 8-col hero tile + 4-col column of two stacked tiles; then 4/4/4 row; then 6/6; one tile should always be ~2× the area of the smallest.
- **Hero:** the hero itself can be a bento — headline tile + product-visual tile + metric tiles. Never center everything.
- **Frame patterns:** full-bento hero, bento feature wall, stats band as bento, footer-adjacent CTA tile inside the grid.
- **Responsive:** 2-col below 1024px (spans collapse to full/half), 1-col below 640px; drop row spans on mobile; tile padding 24px→16px.

## Visual hierarchy
- First seen: the largest tile (visual or metric), then H1 tile, then accent-colored CTA tile. Exactly one tile may shout (accent bg or oversized number); the rest whisper. Eye path: dominant tile → headline → CTA tile → small detail tiles.

## Color system
- **Light:** bg #F4F4F2 · tile #FFFFFF · text #111111 · secondary #5C5C58 · border #E2E2DE · primary action #111111 · accent #0D9488 (teal — used on ONE tile + links) · stat highlight #0D9488.
- **Dark:** bg #0C0C0B · tile #161615 · text #F4F4F2 · secondary #A1A19B · border #262624 · accent #2DD4BF.
- Neutral tiles with 1px borders; accent appears in at most 1–2 tiles. Avoid: every tile a different pastel (rainbow bento), gradients inside tiles.

## Components
Tiles: flat, 12–16px radius, 1px border, optional 2px border for the one featured tile. Stat tiles: mono number 40–48px + unit + caption. Media tiles: image/video fills the tile, caption below inside. CTA tile: accent or dark bg, one action. Navbar: 64px, flat, hairline bottom border. Pricing: plans as three equal tiles inside the bento. Dashboards: this IS the dashboard style — widgets = tiles. Modals: single tile centered, dim backdrop. Badges: small mono chips inside tile headers. Tables: inside a wide tile, hairline rows.

## Shape language
Radius 12–16px consistent across tiles. Borders over shadows (shadow at most 1 subtle on hover). Depth comes from size contrast and borders, not elevation. Icons: 1.5px stroke line icons, one family. No blobs, no decorative shapes — the grid is the decoration.

## Visual direction
Fits: real product screenshots, charts (sparklines, bars, donuts), data/metrics, photography cropped to tiles, icon+label pairs. Breaks cohesion: gradient tiles, 3D floating objects, mixed illustration styles, more than one accent color.

## Motion & Interaction
Hover: tile lifts 2px + border darkens, 180ms ease-out. Staggered reveal on load: tiles fade+rise 12px, 40ms apart, once. Live data (counters, sparklines) may tick — nothing else moves. `prefers-reduced-motion`: disable all reveals and ticks. The grid should look finished in a screenshot.

## When to use
Product features overview, dashboards/analytics, AI/developer tools, changelogs, personal link-hubs, portfolio walls, pricing+features combo pages. Anything where many equal-importance facts must be scanned fast.

## When NOT to use
Long-form storytelling, editorial content, luxury/premium brands (bento reads utilitarian), single-message landing pages (one CTA gets lost in the grid), legal/compliance pages.

## Do
- Vary tile sizes deliberately — one dominant, one accent, rest neutral
- Keep gaps tight and consistent (12–16px)
- Give every tile one job: metric, visual, text, or action
- Use mono labels + real numbers in stat tiles
- Align all tile content to top-left
- Collapse to 1-col with preserved reading order on mobile
- Fill every tile — no half-empty cells

## Don't
- Rainbow pastel tiles (5 tile colors)
- Same-size tiles everywhere (that's a card grid, not a bento)
- Gradient or glass tiles
- Centered text inside tiles
- Decorative empty tiles "for balance"
- More than one accent-colored tile per viewport
- Icons in three different styles across tiles

## Anti AI-slop (bento edition)
Purple gradient tiles, glassmorphic blurs, emoji as tile icons, "10x your workflow" tiles with no data, sparkle/star decorations on corners, identical stat tiles with fake percentages. Slop = a bento where tiles exist to fill space, not to inform.

## Good vs Bad examples
- **Good:** Apple M-chip pages / Linear features page — one hero tile, disciplined spans, real screenshots, monochrome with one accent.
- **Bad:** every tile a different pastel gradient with an emoji icon, centered lorem text, five "✨ AI-powered" tiles — colorful noise, zero hierarchy.
## 14 · Accessibility Notes
- Contrast targets: body 4.5:1, large text/UI 3:1 — verify every text/background pair in this style's palette.
- Focus states: ring on the interactive tile only; tile borders must not all glow at once.
- Motion: this style tempts toward every tile hovering/lifting simultaneously — stagger hover motion, animate one tile at a time. Every animated surface needs a `prefers-reduced-motion` static fallback.
- Common a11y failure in this style: low-contrast text on colored tiles (white on pastel accent) — tiles are surfaces, not backgrounds for failing contrast.

## 15 · Design Decisions Explained (why, not just what)
- **Why these fonts:** a workhorse grotesk handles varied tile content; expressive display fonts per-tile fragment the grid into a ransom note
- **Why this radius:** one radius for all tiles — uniformity IS the bento promise; mixing radii destroys the modular metaphor
- **Why this density:** the style's superpower and its trap: high density needs ruthless tile hierarchy (one hero tile, supporting tiles quiet)
- **Signature move:** the ONE element that makes a page instantly recognizable as this style — use once per page, deliberately.
- **When to break the rules:** one full-bleed break of the grid per page (a tile spanning edge-to-edge) adds drama without breaking the system
