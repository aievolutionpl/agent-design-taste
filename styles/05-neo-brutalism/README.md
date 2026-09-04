# 05 · Neo-Brutalism

**Bold, raw, unconventional.**

## 01 · Overview

Raw, loud and deliberately unpolished — hard black borders, flat saturated color blocks, chunky type and solid offset shadows that mimic physical paper cutouts. It looks like a zine, behaves like a design system.

## 02 · Design philosophy

A refusal of the softening conventions of modern UI — no ambient shadows, no gentle radii, no gradient sheen. Instead: flat saturated color, black outlines, hard offset shadows and type set loud. It is honest about the medium; a button looks stamped onto the page, not extruded from it.

**Design decisions explained — why, not just what**

- **Why these fonts:** ultra-bold grotesks (Archivo Black) are the voice — the style IS loud typography; light weights contradict the material
- **Why this radius:** 0-4px radius only; rounded brutalism is just default UI with a border — the sharpness is semantic
- **Why this density:** high-contrast density works: big type, chunky blocks — but elements must align to a grid even when they look chaotic

## 03 · Visual principles

hard 2–3px borders everywhere · solid offset shadows (no blur) · bold oversized type · flat saturated color blocks · high contrast · intentional imperfection.

## 04 · Typography

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

## 05 · Layout & grid

- **Grid:** 12-col or freeform stacked blocks; container 1160–1240px; section spacing 80–96px.
- **Blocks:** content sits in bordered, color-filled blocks that may be rotated ±1–2°, offset, or overlapping — never floating glass.
- **Hero:** oversized ALL-CAPS headline over a flat color field, with a bordered card or sticker elements overlapping the edge.
- **Frame patterns:** full-bleed color bands, sticker/pricing cards, marquee strip, oversized footer.

## 06 · Visual hierarchy

- First seen: the giant headline, then the yellow/high-contrast CTA, then stickers/badges. Contrast does the pointing: brightest block = most important. Eye path: headline → CTA → accent blocks → details.

## 07 · Color system

- **Light:** bg #FFFDF5 (paper) · text #111111 · border/shadow #111111 · blocks: yellow #FFD02F, pink #FF90E8, blue #4D7CFE, green #23C55E, orange #FF6B35 · primary action #FFD02F with #111 border. Max 3–4 block colors per page.
- **Dark:** bg #111111 · surface #1E1E1E · text #FFFDF5 · border/shadow #FFFDF5 · blocks same saturations, slightly deepened (#E6B800, #E879C7, #3D6BE0).
- No gradients, no transparency, no soft shadows — colors are flat ink.

## 08 · Components

Buttons: flat color, 2px #111 border, solid offset shadow (e.g. `4px 4px 0 #111`); hover = translate(2px,2px) + shadow shrinks to 2px — the signature press effect. Cards: 2px border + 6px 6px 0 #111 offset shadow. Navbar: bordered bar or floating sticker pill. Inputs: 2px border, offset shadow on focus, mono placeholder. Pricing: sticker cards, featured plan has bigger offset + rotation. Badges/stamps: mono uppercase chips with 2px border. Modals: hard-bordered panel with big offset shadow, no blur backdrop (use solid 50% black). Marquee: repeating uppercase mono strip between sections.

Anatomy and the required state matrix (default / hover / focus-visible / active / disabled / loading / error / success) are universal — see `component-patterns/COMPONENT-PATTERNS.md`. This section defines the *skin*, not the behaviour.

## 09 · Shape language

Radius 0 everywhere (max 4px on pills). Borders 2px, always #111 (or paper color on dark). Offset shadows are solid, axis-aligned, no blur — `Xpx Ypx 0 #000`. Depth = offset, not elevation. Icons: chunky filled or 2px-stroke icons; emoji allowed sparingly as raw stickers.

## 10 · Imagery & visual direction

Fits: flat vector illustration, sticker sheets, halftone/print textures, big stat numbers, marquees, hand-drawn arrows/underlines. Breaks cohesion: glassmorphism, gradients, photorealistic 3D, thin elegant serifs, soft pastels.

Per-style image direction table: `visual-language/VISUAL-LANGUAGE-FOUNDATIONS.md` § 10.

## 11 · Motion

Snappy, not smooth: hover/press 120ms steps or linear — the offset-shadow press effect on every interactive element. Marquee scrolls continuously (pause on hover). Reveal: blocks pop in with scale 0.96→1, 200ms, staggered. `prefers-reduced-motion`: stop marquee and reveals. Motion should feel mechanical, like paper being moved.

## 12 · Responsive behaviour

Verify at **1440 · 768 · 390** (canonical mobile) and once at **360** (narrow floor). Responsive means recomposition, not stacking — `responsive/RESPONSIVE-FOUNDATIONS.md`.

- **Adaptation:** borders and offsets stay; H1 → 36–40px mobile, stack stickers, rotation reduced to 0 on mobile.
- **Non-negotiable for this style:** Borders and offsets stay at full weight. Thinning them "to fit" turns brutalism into a default card with a border.

## 13 · Accessibility

- Contrast targets: body 4.5:1, large text/UI 3:1 — verify every text/background pair in this style's palette.
- Focus states: thick black 3px+ outline focus — it's already the aesthetic, keep it on every interactive element.
- Motion: this style tempts toward bouncy spring easing everywhere — hard shadows should SNAP (150ms linear), not wobble. Every animated surface needs a `prefers-reduced-motion` static fallback.
- Common a11y failure in this style: yellow-on-white or neon-on-neon text; loud style still means 4.5:1 body contrast.

The universal floor — contrast, focus, keyboard, semantics, motion, touch targets, zoom — is in `accessibility/ACCESSIBILITY.md`. This section covers what *this style specifically* gets wrong.

## 14 · When to use

Youth brands, indie tools, dev/hacker communities, events, merch/ecommerce drops, portfolios with attitude, crypto/web3-adjacent. Audience expects energy and anti-corporate honesty.

## 15 · When NOT to use

Fintech, health, enterprise, legal, luxury — anything needing trust and calm. Long text-heavy reading (all-caps fatigues). Also wrong for dense dashboards (borders + offsets get noisy).

## 16 · Do

- 2px black borders on every interactive surface
- Solid offset shadows: `4px 4px 0 #111`, shrink on press
- Oversized ALL-CAPS Archivo Black headlines
- Flat saturated blocks, max 3–4 colors per page
- Mono uppercase stamps for labels/meta
- Visible grid/structure — brutalism is honest about its skeleton
- Real copy with personality, even blunt tone

## 17 · Don't

- Blurred or translucent shadows
- Gradients anywhere
- Thin 1px hairline borders
- Light-weight body fonts
- Rounded soft everything (that's cute-ism, not brutalism)
- More than 4 block colors (rainbow soup)
- Glass, blur, neumorphism
- Centered everything with no grid logic

## 18 · Anti-slop — neo-brutalism edition

Pastel "soft brutalism" with 16px radius + tiny shadows (that's just default UI with a yellow button), random rotation everywhere, emoji stickers on every corner, gradient text, lorem-blocks in huge type. Slop = aggression as decoration without structure; real neo-brutalism is loud AND rigorously aligned.

**Good vs bad**

- **Good:** Gumroad post-2021 — hard borders, offset shadows, one yellow, giant caps, rigorous grid underneath the noise.
- **Bad:** pastel cards with soft shadows and a random rotated "WOW" sticker — reads as default SaaS wearing a costume, no borders, no conviction.

Universal severity levels (BLOCKER / STRONG / MINOR): `ANTI-SLOP.md`.

## 19 · Style combinations

One dominant + at most one supporting style. The supporting style owns exactly one layer — typography, one section type, or micro-motion — never structure.

- **Works with:** Bento (04) — hard borders plus modular grid structure
- **Avoid pairing with:** Claymorphism (08) — raw versus soft is incoherent · Neumorphism (07) — the two shadow languages contradict each other

Full rules: `STYLE-COMBINATIONS.md`.

## 20 · Signature move

**A hard, un-blurred offset shadow** (`4px 4px 0 var(--color-text)`) that collapses to zero on press, so the element visibly slams into the page. No blur radius, ever.

Use it **once per page**, deliberately. A signature move repeated on every element is no longer a signature.

## 21 · When to break the rules

never soften it; if the brand can't take loudness, change style — half-brutalism is the definition of slop

## 22 · Example prompts

Ready-to-paste prompts for Codex, Claude, Lovable and v0: [`prompts.md`](prompts.md)

## 23 · Design tokens

- [`tokens.css`](tokens.css) — **canonical.** If this file and the prose above disagree, the token wins.
- [`tokens.json`](tokens.json) — generated, for design tools and JS
- [`tokens.tailwind.css`](tokens.tailwind.css) — generated, Tailwind v4 `@theme`

Regenerate the two derived files with `python3 scripts/gen_tokens.py` after editing `tokens.css`.

## 24 · Example implementation

[`example.html`](example.html) — a single-file, zero-dependency page built strictly from this style's DNA and tokens. Open it in a browser.

It is **one valid interpretation, not a spec.** Copying it wholesale is how every page ends up identical — read it, then compose something else.
