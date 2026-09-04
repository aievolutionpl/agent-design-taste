# 14 · 3D / Spatial UI

**Depth you can move through.**

## 01 · Overview

Interfaces built in depth, not just on a plane. Content lives on layers in a shared perspective space — the camera (scroll/cursor) moves, and the interface moves with it. Depth is used to explain relationships: foreground = interactive, background = context.

## 02 · Design philosophy

Depth as a navigational dimension. Elements occupy z-space, cast real shadows and respond to viewpoint, so hierarchy can be expressed by distance rather than by size alone. Used well it makes a product feel like a place; used badly it makes text unreadable at an angle.

**Design decisions explained — why, not just what**

- **Why these fonts:** geometric sans with wide weights (Space Grotesk) matches dimensional space; thin fonts break up at small 3D scales
- **Why this radius:** depth-driven: layer radii increase toward the viewer (8/12/16px) — the radius becomes a depth cue
- **Why this density:** low-mid: each 3D layer costs attention; spatial UI shows FEW things in MORE space

## 03 · Visual principles

real perspective · layered z-space · parallax storytelling · one vanishing point · depth through position not decoration · vanilla CSS 3D transforms (no libraries required) · motion serves spatial comprehension.

## 04 · Typography

- **Recommended families (Google Fonts):** Display: Space Grotesk, Clash-adjacent — use Space Grotesk. Text: Inter. Mono: Space Mono, IBM Plex Mono.
- **Pairing:** Space Grotesk (H1–H2, 500–700) + Inter (H3–body) + Space Mono (labels/coordinates/depth data).
- **Scale:** H1 60/64 · H2 42/50 · H3 26/34 · H4 21/30 · H5 18/26 · H6 16/24 · body 17/1.6 · small 14/1.5.
- **Body:** 17px, line-height 1.6, letter-spacing 0. Measure 62ch. Headlines may get slight negative tracking (-0.02em); body never.
- **Uppercase:** 11–12px mono labels with +0.12em tracking for layer/coordinate annotations ("LAYER 02 · Z:-120PX") — a signature detail of the style.
- **CSS:**
```css
h1 { font: 700 60px/1.06 'Space Grotesk'; letter-spacing: -0.02em; }
body { font: 400 17px/1.6 'Inter'; }
.layer-label { font: 500 11px/1 'Space Mono'; letter-spacing: 0.12em; text-transform: uppercase; }
```
- **Typical mistakes:** italic faux-3D text; type rotated more than ~8°; headings transformed in Z until blurry; body copy inside tilted planes.

## 05 · Layout & grid

- **Grid:** normal 12-col grid on the content plane; depth is added *around* the grid, not instead of it. Max-width 1200px.
- **3D stage:** a `.scene` wrapper gets `perspective: 1200px` (one per section — never competing perspectives), children get `transform-style: preserve-3d`.
- **Layers:** 2–4 meaningful layers per section (e.g. card at z:0, floating panel at z:60px, ambient shape at z:-150px). Beyond 4 layers it becomes noise.
- **Parallax:** scroll-driven translateZ/translateY offsets on layers; cursor-parallax only in the hero, ±10px max, lerped.
- **Hero:** full-viewport scene with a centered/exploded composition — product UI plane straight-on, supporting planes rotated on Y (rotateY ±12–20°) and offset in Z.
- **Frame patterns:** spatial hero, layered feature cards (stack in Z, fan out on hover/scroll), exploded diagram sections, flat-pricing (keep pricing FLAT — depth here hurts conversion), spatial footer.

## 06 · Visual hierarchy

- First seen: the object closest to camera (hero plane), then H1, then CTA. Depth must reinforce hierarchy: the thing you want clicked is in front, larger, shadowed; context recedes. One primary CTA per view.

## 07 · Color system

- **Light:** bg #F4F4F0 (slightly warm so white planes float) · surface #FFFFFF · text #0E0E10 · secondary #5A5A5E · border #E3E3DE · accent #4F46E5 (indigo) used for interaction + depth-edges only.
- **Dark:** bg #060608 · surface #101014 · text #F2F2F0 · secondary #8E8E94 · border #1F1F26 · accent #8B8BF5. Dark mode is the natural home of this style — planes read as lit objects.
- Ambient/atmosphere layers may use large soft radial glows of the accent at ≤12% opacity. Avoid: rainbow depth (each layer a different hue), neon on light bg.

## 08 · Components

Buttons: solid primary with a 1px top-edge highlight (light inset line) to feel dimensional; hover lifts translateZ(8px)+shadow, 200ms. Cards: planes with real shadow depth (soft, large-blur, low-opacity — `0 24px 60px -24px rgb(0 0 0 / 0.25)`), tilt max 6° on hover. Navbar: flat, on the content plane — do not float the nav in 3D. Inputs: flat, 1px border; only focus state lifts. Modals: rise out of the page (scale 0.96→1 + translateY) not full rotateX flips. Badges/chips: flat. Depth annotations: mono micro-labels on layer edges. Never: text buttons rotated in 3D, 3D carousels for navigation.

Anatomy and the required state matrix (default / hover / focus-visible / active / disabled / loading / error / success) are universal — see `component-patterns/COMPONENT-PATTERNS.md`. This section defines the *skin*, not the behaviour.

## 09 · Shape language

Planes are rounded rectangles, radius 12–16px — radius does not grow with depth. Depth cues, in order of preference: (1) actual Z-position + perspective, (2) large soft shadow, (3) slight desaturation/blur of far layers, (4) scale. Corners of rotated planes may show 1px accent edge-light. No skeuomorphic bevels, no textured "3D" PNG blobs.

## 10 · Imagery & visual direction

Fits: product screenshots on tilted planes, isometric/exploded diagrams, subtle grid or dot floor extending to a horizon, gradient atmospheres (very restrained), soft glows. Breaks cohesion: flat illustrations competing with 3D planes, emoji, heavy skeuomorphism (wood, glass+metal mixed), more than one perspective per viewport.

Per-style image direction table: `visual-language/VISUAL-LANGUAGE-FOUNDATIONS.md` § 10.

## 11 · Motion

Everything motion does should answer "how is this arranged in space?" Signature moves: scroll-driven layer parallax (staggered speeds), hover lift translateZ(8–12px), card fan-out (adjacent cards rotateY ∓6°, translateZ ∓40px), slow ambient rotation (60s+ loops, small amplitude). Durations 300–500ms, `cubic-bezier(0.16, 1, 0.3, 1)`. **Fallbacks are mandatory:** `@media (prefers-reduced-motion: reduce)` kills parallax/rotation and flattens transforms to static layering with shadows; also provide a JS-free static appearance if JS is off (CSS-only scroll effects). If WebGL is used it must be a decorative layer that can be removed with zero content loss — content stays in DOM/HTML.

## 12 · Responsive behaviour

Verify at **1440 · 768 · 390** (canonical mobile) and once at **360** (narrow floor). Responsive means recomposition, not stacking — `responsive/RESPONSIVE-FOUNDATIONS.md`.

- **Adaptation:** below 900px collapse depth: remove rotateY, drop parallax, keep only soft shadow layering. Never make users scroll through mandatory 3D on mobile.
- **Non-negotiable for this style:** Collapse depth entirely: remove `rotateY`, drop parallax, keep soft shadow layering. Never require 3D interaction to reach content.

## 13 · Accessibility

- Contrast targets: body 4.5:1, large text/UI 3:1 — verify every text/background pair in this style's palette.
- Focus states: 2D focus rings on top of the 3D layer; 3D-transformed controls must keep standard focus behavior.
- Motion: this style tempts toward parallax responds to every mouse move — respect reduced-motion with a static 2D layout fallback. Every animated surface needs a `prefers-reduced-motion` static fallback.
- Common a11y failure in this style: text on tilted/rotated 3D planes (effective size and contrast change with angle) — keep text on flat layers, 3D for objects.

The universal floor — contrast, focus, keyboard, semantics, motion, touch targets, zoom — is in `accessibility/ACCESSIBILITY.md`. This section covers what *this style specifically* gets wrong.

## 14 · When to use

Product launches (especially dev tools, AR/VR/spatial apps, hardware, mapping), interactive storytelling, portfolio hero moments, feature explanations where "layers" is literally the product story. Audience expects wow and will tolerate scroll friction.

## 15 · When NOT to use

Dense B2B dashboards, docs, checkout, healthcare/finance trust-critical flows, accessibility-first products, anything users must scan fast all day — depth taxes reading speed.

## 16 · Do

- One perspective per section; one shared vanishing logic per page
- 2–4 layers max, each with a reason to exist in Z
- Depth reinforces hierarchy (front = action)
- Real CSS: `perspective`, `preserve-3d`, `translateZ`, `rotateY`
- Big soft shadows + far-layer desaturation as depth cues
- Mono coordinate/layer labels as a craft detail
- Dark mode first; light mode needs stronger shadows
- Ship the reduced-motion flattened version and test it

## 17 · Don't

- rotateX(45deg) walls of text
- Depth for decoration with no informational meaning
- Floating 3D stock blobs/illustrations pasted on a flat page
- Parallax on body text or navigation
- 3D-flip carousels as primary navigation
- Mandatory 3D interactions on mobile
- More than one accent color "per dimension"
- WebGL for content that could be a plane

## 18 · Anti-slop — 3D spatial edition

Random purple orbs, floating glass cubes, "3D abstract shapes" hero renders with no relation to content, every card rotateY(15deg), scroll-jacked full-page 3D scenes, Spline embeds where a screenshot would do. Slop = depth without meaning.

**Good vs bad**

- **Good:** Linear/Arc-style product heroes — a flat, readable UI plane, gently tilted, with supporting layers parallaxing behind; depth explains the product.
- **Bad:** a landing page where the entire content column is rotated in perspective, text blurs, and a purple 3D blob covers the CTA — motion sickness, zero comprehension.

Universal severity levels (BLOCKER / STRONG / MINOR): `ANTI-SLOP.md`.

## 19 · Style combinations

One dominant + at most one supporting style. The supporting style owns exactly one layer — typography, one section type, or micro-motion — never structure.

- **Works with:** Minimalism (01) — a 3D centrepiece with minimalist everything else · Glassmorphism (02) — glass panels floating in 3D space
- **Avoid pairing with:** Editorial (11) — serif reading flow versus spatial depth · Swiss (10) — the grid is flat by definition

Full rules: `STYLE-COMBINATIONS.md`.

## 20 · Signature move

**A single hero object at a fixed depth that responds to scroll or pointer,** while every piece of text stays on a flat 2D plane in front of it. Depth for objects, flatness for words.

Use it **once per page**, deliberately. A signature move repeated on every element is no longer a signature.

## 21 · When to break the rules

a fully flat 2D section after a 3D journey gives the eyes rest and the 3D meaning — alternate dimensions deliberately

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
