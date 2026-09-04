# 05 · Neo-Brutalism

**Overview:** Raw, loud and deliberately unpolished — hard black borders, flat saturated color blocks, chunky type and solid offset shadows that mimic physical paper cutouts. It looks like a zine, behaves like a design system.

**Visual principles:** hard 2–3px borders everywhere · solid offset shadows (no blur) · bold oversized type · flat saturated color blocks · high contrast · intentional imperfection.

## Typography
- **Recommended families (Google Fonts):** Display: Archivo Black, Space Grotesk 700, Anton. Text: Space Grotesk, Archivo, Jakarta Sans. Mono (labels, stamps): Space Mono, IBM Plex Mono.
- **Pairing:** Archivo Black (H1–H2) + Space Grotesk (H3–body) + Space Mono (labels/stamps).
- **Scale:** H1 64/1.0 · H2 44/1.05 · H3 26/1.3 · H4 20/1.4 · body 16/1.6 · small 14/1.5.
- **Body:** 16px, line-height 1.6. Body can be 500 weight — neo-brutalism has no anemic thin text.
- **Uppercase:** headings often ALL-CAPS; mono labels 12px uppercase +0.1em as "stamps".
- **CSS:**
```css
h1 { font: 400 64px/1.0 'Archivo Black'; text-transform: uppercase; letter-spacing: -0.01em; }
body { font: 500 16px/1.6 'Space Grotesk'; }
.stamp { font: 700 12px/1 'Space Mono'; letter-spacing: .1em; text-transform: uppercase; }
```
- **Typical mistakes:** light weights (300–400 body), tight all-caps body paragraphs, thin borders, soft rounded fonts (Nunito-style) that kill the rawness.

## Layout & Frames
- **Grid:** 12-col or freeform stacked blocks; container 1160–1240px; section spacing 80–96px.
- **Blocks:** content sits in bordered, color-filled blocks that may be rotated ±1–2°, offset, or overlapping — never floating glass.
- **Hero:** oversized ALL-CAPS headline over a flat color field, with a bordered card or sticker elements overlapping the edge.
- **Frame patterns:** full-bleed color bands, sticker/pricing cards, marquee strip, oversized footer.
- **Responsive:** borders and offsets stay; H1 → 36–40px mobile, stack stickers, rotation reduced to 0 on mobile.

## Visual hierarchy
- First seen: the giant headline, then the yellow/high-contrast CTA, then stickers/badges. Contrast does the pointing: brightest block = most important. Eye path: headline → CTA → accent blocks → details.

## Color system
- **Light:** bg #FFFDF5 (paper) · text #111111 · border/shadow #111111 · blocks: yellow #FFD02F, pink #FF90E8, blue #4D7CFE, green #23C55E, orange #FF6B35 · primary action #FFD02F with #111 border. Max 3–4 block colors per page.
- **Dark:** bg #111111 · surface #1E1E1E · text #FFFDF5 · border/shadow #FFFDF5 · blocks same saturations, slightly deepened (#E6B800, #E879C7, #3D6BE0).
- No gradients, no transparency, no soft shadows — colors are flat ink.

## Components
Buttons: flat color, 2px #111 border, solid offset shadow (e.g. `4px 4px 0 #111`); hover = translate(2px,2px) + shadow shrinks to 2px — the signature press effect. Cards: 2px border + 6px 6px 0 #111 offset shadow. Navbar: bordered bar or floating sticker pill. Inputs: 2px border, offset shadow on focus, mono placeholder. Pricing: sticker cards, featured plan has bigger offset + rotation. Badges/stamps: mono uppercase chips with 2px border. Modals: hard-bordered panel with big offset shadow, no blur backdrop (use solid 50% black). Marquee: repeating uppercase mono strip between sections.

## Shape language
Radius 0 everywhere (max 4px on pills). Borders 2px, always #111 (or paper color on dark). Offset shadows are solid, axis-aligned, no blur — `Xpx Ypx 0 #000`. Depth = offset, not elevation. Icons: chunky filled or 2px-stroke icons; emoji allowed sparingly as raw stickers.

## Visual direction
Fits: flat vector illustration, sticker sheets, halftone/print textures, big stat numbers, marquees, hand-drawn arrows/underlines. Breaks cohesion: glassmorphism, gradients, photorealistic 3D, thin elegant serifs, soft pastels.

## Motion & Interaction
Snappy, not smooth: hover/press 120ms steps or linear — the offset-shadow press effect on every interactive element. Marquee scrolls continuously (pause on hover). Reveal: blocks pop in with scale 0.96→1, 200ms, staggered. `prefers-reduced-motion`: stop marquee and reveals. Motion should feel mechanical, like paper being moved.

## When to use
Youth brands, indie tools, dev/hacker communities, events, merch/ecommerce drops, portfolios with attitude, crypto/web3-adjacent. Audience expects energy and anti-corporate honesty.

## When NOT to use
Fintech, health, enterprise, legal, luxury — anything needing trust and calm. Long text-heavy reading (all-caps fatigues). Also wrong for dense dashboards (borders + offsets get noisy).

## Do
- 2px black borders on every interactive surface
- Solid offset shadows: `4px 4px 0 #111`, shrink on press
- Oversized ALL-CAPS Archivo Black headlines
- Flat saturated blocks, max 3–4 colors per page
- Mono uppercase stamps for labels/meta
- Visible grid/structure — brutalism is honest about its skeleton
- Real copy with personality, even blunt tone

## Don't
- Blurred or translucent shadows
- Gradients anywhere
- Thin 1px hairline borders
- Light-weight body fonts
- Rounded soft everything (that's cute-ism, not brutalism)
- More than 4 block colors (rainbow soup)
- Glass, blur, neumorphism
- Centered everything with no grid logic

## Anti AI-slop (neo-brutalism edition)
Pastel "soft brutalism" with 16px radius + tiny shadows (that's just default UI with a yellow button), random rotation everywhere, emoji stickers on every corner, gradient text, lorem-blocks in huge type. Slop = aggression as decoration without structure; real neo-brutalism is loud AND rigorously aligned.

## Good vs Bad examples
- **Good:** Gumroad post-2021 — hard borders, offset shadows, one yellow, giant caps, rigorous grid underneath the noise.
- **Bad:** pastel cards with soft shadows and a random rotated "WOW" sticker — reads as default SaaS wearing a costume, no borders, no conviction.