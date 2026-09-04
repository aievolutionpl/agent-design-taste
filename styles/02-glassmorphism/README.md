# 02 · Glassmorphism

**Translucent. Layered. Modern.**

## 01 · Overview

Frosted translucent surfaces floating over a vivid, colorful background. Depth comes from blur + light borders, not shadows. One hard rule governs everything: **readability first, glass second — never more than 2 glass surfaces per view.**

## 02 · Design philosophy

Depth through translucency. Surfaces sit *in front of* a scene rather than on a page: they blur what is behind them, admit a hint of its color, and carry a light edge that reads as a bevel. It borrows the physics of frosted glass to make layer order legible without lines or heavy shadows.

**Design decisions explained — why, not just what**

- **Why these fonts:** a clean geometric sans survives blur best; thin serifs dissolve into the frosted layer and become unreadable
- **Why this radius:** larger radii (16-20px) reinforce the soft 'pane' metaphor; sharp corners make glass look like broken windows
- **Why this density:** 2 glass surfaces per view max — more translucency stacks into visual noise; content density belongs on solid surfaces

## 03 · Visual principles

frosted translucency · colorful gradient backdrop · light borders (white alpha) · soft elevation · airy spacing · glass is a highlight, not a layout system.

## 04 · Typography

- **Recommended families (Google Fonts):** Text/Sans: Inter, Plus Jakarta Sans, Outfit. Display: Plus Jakarta Sans. Mono: JetBrains Mono.
- **Pairing:** Plus Jakarta Sans (H1–H2, 700) + Inter (H3–body) + JetBrains Mono (labels/data).
- **Scale:** H1 56/64 · H2 40/48 · H3 28/36 · H4 22/30 · H5 18/26 · H6 16/24 · body 17/1.6 · small 14/1.5.
- **Body:** 17px, line-height 1.6, letter-spacing 0. Measure 60–65ch.
- **Uppercase:** 11–12px eyebrow labels only, +0.08em tracking, never headings.
- **CSS:**
```css
h1 { font: 700 56px/1.15 'Plus Jakarta Sans'; letter-spacing: -0.02em; }
body { font: 400 17px/1.6 'Inter'; }
.eyebrow { font: 600 12px/1 'JetBrains Mono'; letter-spacing: 0.08em; text-transform: uppercase; }
```
- **Typical mistakes:** light (300) weights on glass (contrast dies); text sitting directly on the busy background; 5+ weights; centered walls of paragraph text.

## 05 · Layout & grid

- **Grid:** 12-col, max-width 1200px, gutters 24px.
- **Spacing:** 8-base scale; sections 96px apart — glass surfaces need breathing room or they stack into fog.
- **Hero:** split hero — glass card on one side over the gradient field, headline on solid background. Never a wall of glass cards.
- **Frame patterns:** split hero with one glass panel, alternating features on solid surfaces, one glass stat/pricing highlight, solid CTA band.

## 06 · Visual hierarchy

- First seen: H1 (highest contrast element), then primary CTA, then the single glass card. Glass attracts the eye — reserve it for the one thing that should be looked at. Eye path: headline → sub → CTA → glass panel proof.

## 07 · Color system

- **Background (required):** vivid multi-stop gradient — e.g. #6366F1 → #EC4899 → #F59E0B, or deep navy #0F172A with two colored glows. Glass is meaningless over flat color.
- **Light:** text #111111 on solid areas · secondary #555555 · on-glass text = darkest legible tone for that backdrop.
- **Dark:** bg #0F172A base · text #F8FAFC · secondary #94A3B8 · on-glass text always near-white.
- **Glass recipe:** `background: rgb(255 255 255 / 0.10–0.18)` (dark) or `rgb(255 255 255 / 0.55–0.70)` (light) · `backdrop-filter: blur(16–24px) saturate(160%)` · border `1px solid rgb(255 255 255 / 0.25)` · radius 16–24px · shadow `0 8px 32px rgb(0 0 0 / 0.12)`.
- One accent max (#8B5CF6 or brand color) for CTAs — solid fill, never translucent CTA.
- Avoid: neon glows on glass, second accent, text-color gradients, >20% white overlays stacking.

## 08 · Components

Buttons: solid accent fill or solid dark/white — never glass buttons (contrast untestable). Cards: solid surfaces by default; glass card = the ONE highlighted panel per view. Navbar: glass allowed (surface #1 of 2) with blur ≥16px and dark text. Inputs: solid white/dark field, 1px border — never translucent inputs. Pricing: solid cards, one glass "highlighted" plan max. Modals: glass backdrop panel allowed (counts as the view's glass surface — dim the page behind). Dashboards: solid panels, one glass summary strip. Badges: solid pill. Tooltips: solid dark. Tables: solid, hairline rows — never glass rows.

**The 2-surface rule:** a view may contain at most 2 glass surfaces (typically navbar + hero card). Everything else is solid. If you need a third, you need a different style.

Anatomy and the required state matrix (default / hover / focus-visible / active / disabled / loading / error / success) are universal — see `component-patterns/COMPONENT-PATTERNS.md`. This section defines the *skin*, not the behaviour.

## 09 · Shape language

Radius 16–24px on glass, 12px on solid components. Borders always visible on glass (1px white alpha) — a borderless blur is unreadable. Depth = blur + border + one soft shadow. No nested glass (glass inside glass = mud).

## 10 · Imagery & visual direction

Fits: abstract color fields/gradients behind glass, product screenshots inside glass frames, duotone photography. Breaks cohesion: flat white background (glass invisible), busy photo behind body text, heavy illustration + glass fighting for attention, 3D blobs under every section.

Per-style image direction table: `visual-language/VISUAL-LANGUAGE-FOUNDATIONS.md` § 10.

## 11 · Motion

Hover on glass: brightness 1.05 + border alpha +0.05, 200ms ease-out. Reveals: translateY 16px + opacity, 400ms. Background gradient may drift slowly (60s loop) — that's the whole ambient show. `prefers-reduced-motion`: freeze background, disable reveals, keep hover color shifts only.

## 12 · Responsive behaviour

Verify at **1440 · 768 · 390** (canonical mobile) and once at **360** (narrow floor). Responsive means recomposition, not stacking — `responsive/RESPONSIVE-FOUNDATIONS.md`.

- **Adaptation:** glass blur cost is real on mobile — drop to 1 glass surface or replace with solid surface below 720px; H1→34px.
- **Non-negotiable for this style:** Blur is expensive on mobile GPUs. At 390px, reduce to one glass surface — or swap to a solid surface entirely and keep the palette.

## 13 · Accessibility

- Contrast targets: body 4.5:1, large text/UI 3:1 — verify every text/background pair in this style's palette.
- Focus states: a solid 2px ring — focus indicators get lost in blur and translucency.
- Motion: this style tempts toward parallax blobs behind every glass surface — blur + movement = motion sickness and battery drain. Every animated surface needs a `prefers-reduced-motion` static fallback.
- Common a11y failure in this style: text over translucent glass over a vivid image fails contrast unpredictably — always give glass surfaces a solid fallback background.

The universal floor — contrast, focus, keyboard, semantics, motion, touch targets, zoom — is in `accessibility/ACCESSIBILITY.md`. This section covers what *this style specifically* gets wrong.

## 14 · When to use

Music/media apps, weather, fintech dashboards, creative tools, design-agency sites, event/hospitality brands — anywhere a colorful brand moment + one floating highlight panel reads as premium.

## 15 · When NOT to use

Dense content (docs, data tables, long-form reading — blur kills contrast over time), enterprise/trust-first B2B, healthcare, government. Also not for whole-dashboards: glass is garnish, not architecture.

## 16 · Do

- Cap at 2 glass surfaces per view — count them
- Put vivid, simple gradients behind glass; solid color behind body text
- Use 1px white-alpha border on every glass surface
- blur(16–24px) + saturate(160%) minimum for legibility
- Solid CTAs only
- Test text contrast on the worst background spot behind the glass
- Fall back to solid surfaces on mobile / no backdrop-filter support
- Use `@supports (backdrop-filter: blur(1px))` guard with solid fallback

## 17 · Don't

- Glass cards stacked in grids
- Glass buttons, inputs, or table rows
- Light font weights on glass
- Text directly over the busy background (glass exists to fix that — use it)
- Borderless blur panels
- Nested glass surfaces
- Purple-blue gradient + Inter default combo as the entire identity
- Fake transparency over flat color (just looks dirty)

## 18 · Anti-slop — glassmorphism edition

The slop tell: a purple gradient hero, five floating glass cards with generic feature blurbs, glowing neon orbs, gradient text "Revolutionize your workflow". Real glassmorphism is *restrained*: vivid backdrop, one or two precise glass moments, bulletproof contrast. If every card is frosted, nothing is.

**Good vs bad**

- **Good:** Apple Music/visionOS-style marketing pages — rich color field, one frosted panel carrying the key content, solid type elsewhere.
- **Bad:** SaaS landing where nav, hero, all 6 feature cards, pricing and footer are translucent — fog stack, unreadable, zero hierarchy.

Universal severity levels (BLOCKER / STRONG / MINOR): `ANTI-SLOP.md`.

## 19 · Style combinations

One dominant + at most one supporting style. The supporting style owns exactly one layer — typography, one section type, or micro-motion — never structure.

- **Works with:** Bento (04) — bento structure with glass on exactly ONE highlighted tile
- **Avoid pairing with:** Maximalism (12) — translucency over visual noise is unreadable · Editorial (11) — reading flow dies behind blur

Full rules: `STYLE-COMBINATIONS.md`.

## 20 · Signature move

**One frosted panel over a vivid, deliberately blurred background** — where the blur lets the color beneath show through just enough to prove the panel is in front of something real. One panel. Not thirty.

Use it **once per page**, deliberately. A signature move repeated on every element is no longer a signature.

## 21 · When to break the rules

drop glass entirely for dense sections (tables, forms) — glass is for navigation, overlays and heroes, never for data

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
