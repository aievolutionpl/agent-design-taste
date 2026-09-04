# 03 · Liquid Glass

**Fluid light and motion.**

## 01 · Overview

Apple's Liquid Glass language (2025): a translucent material that behaves like real glass — it bends and refracts light from what's beneath it, carries a moving specular highlight, and adapts its tint to surrounding content. The interface feels alive: fluid springy motion, floating layers over rich content. Built for **consumer apps**.

## 02 · Design philosophy

Glass as a material, not a texture. Surfaces refract, pool light at their edges and deform in response to motion, so the interface reads as a fluid layer above the content rather than a stack of cards. Light behaviour — not decoration — communicates state and hierarchy.

**Design decisions explained — why, not just what**

- **Why these fonts:** rounded-humanist sans matches the fluid material; rigid grotesks clash with the organic light behavior
- **Why this radius:** full pills (999px) echo the liquid metaphor — the material has no corners, neither should the chrome
- **Why this density:** consumer-light by design; this style collapses under dashboards — it's a marketing/navigation language

## 03 · Visual principles

refractive translucency (not flat frost) · specular highlight on the top edge · fluid, springy motion · floating layered controls over rich media · dynamic adaptation (glass picks up the color under it) · playful but physically grounded.

## 04 · Typography

- **Recommended families (Google Fonts):** Text/Sans: Inter (closest to SF), Manrope, Figtree. Display: Figtree (rounded warmth) or Manrope. Mono: Geist Mono or JetBrains Mono.
- **Pairing:** Figtree (H1–H2, 700) + Inter (H3–body) + Geist Mono (labels/stats).
- **Scale:** H1 56/64 · H2 40/48 · H3 28/36 · H4 22/30 · H5 18/26 · H6 16/24 · body 17/1.6 · small 14/1.5.
- **Body:** 17px, line-height 1.6, friendly and direct. Measure 60ch.
- **Uppercase:** 11–12px capsule labels only; never headings.
- **CSS:**
```css
h1 { font: 700 56px/1.12 'Figtree'; letter-spacing: -0.015em; }
body { font: 400 17px/1.6 'Inter'; }
.eyebrow { font: 600 12px/1 'Geist Mono'; letter-spacing: 0.08em; text-transform: uppercase; }
```
- **Typical mistakes:** static corporate tone (this is a consumer style); heavy serif formality; tiny blurred text on bright imagery; four weights fighting.

## 05 · Layout & grid

- **Grid:** 12-col, max-width 1200px, gutters 24px. Content flows over a rich background; layers float, they don't tile.
- **Spacing:** 8-base scale; sections 96px apart. Floating elements get 16–24px clearance.
- **Hero:** full-bleed rich media (gradient mesh, photo, or video still) with a floating glass control capsule + headline either on a scrim or below the media. Glass elements float like physical objects.
- **Frame patterns:** full-bleed media hero with floating pill nav, horizontally scrolling card rails (solid cards), one floating glass dock/action bar, big CTA.

## 06 · Visual hierarchy

- First seen: the hero media + floating glass control (the "toy"), then H1, then primary CTA. Liquid Glass invites touch — the primary action should be the most physically-present element. Eye path: media → floating control → headline → CTA.

## 07 · Color system

- **Background:** rich, moving media — gradient mesh (e.g. #0EA5E9 → #8B5CF6 → #F472B6 over #0B1120), duotone photo, or soft video. Liquid glass needs changing light underneath to read as glass.
- **Dark (native mode):** bg #0B1120 · text #FFFFFF · secondary rgb(255 255 255 / 0.65) · on-glass text white.
- **Light (native mode):** bg #F5F7FA · text #0B1120 · on-glass text near-black.
- **Liquid glass recipe:** `backdrop-filter: blur(14px) saturate(180%) brightness(1.08)` · tint `rgb(255 255 255 / 0.14)` adaptive · **specular highlight:** inset `inset 0 1px 0 rgb(255 255 255 / 0.4)` + top-edge gradient sheen · subtle outer border `rgb(255 255 255 / 0.22)` · radius pill or 24–32px continuous curve · shadow `0 12px 40px rgb(0 0 0 / 0.18)`.
- Accent: one vivid hue (#0A84FF iOS blue or brand). CTAs solid or tinted glass capsule with verified contrast — test on brightest content beneath.
- Avoid: matte gray slabs, static flat backgrounds, >3 floating glass elements, colored text on glass.

## 08 · Components

Buttons: capsule — solid accent (primary) or tinted glass capsule with white text + specular (secondary). Nav: floating glass pill, centered, detached from edges. Cards: **solid** (content cards carry information); glass reserved for controls, docks, and transport elements. Inputs: solid rounded fields. Segmented control: glass capsule with sliding thumb. Sliders: glass track, glowing thumb. Media player: floating glass dock is the signature component. Modals: glass sheet sliding from bottom with dimmed spring. Badges: small capsules. Switches: iOS-style. Dashboards: not this style — liquid glass is consumer, not enterprise.

**Glass budget:** glass = controls & chrome (nav, dock, player, segmented controls), never content containers. Content lives on solid surfaces or directly on the media.

Anatomy and the required state matrix (default / hover / focus-visible / active / disabled / loading / error / success) are universal — see `component-patterns/COMPONENT-PATTERNS.md`. This section defines the *skin*, not the behaviour.

## 09 · Shape language

Pill capsules and 24–32px continuous-curve radii — no sharp corners anywhere. Inner top-edge specular line on every glass element (the "light source is above" tell). Depth: layers stack with real shadow + refraction, physically plausible. Icons: SF-Symbols-like filled/rounded, 1.5–2px stroke.

## 10 · Imagery & visual direction

Fits: rich photography, gradient meshes, video stills, product renders (headphones, watches, speakers), 3D object floats. Breaks cohesion: flat corporate layouts, dense tables, sharp corners, hard 1px borders on content cards, gray-on-gray enterprise tone.

Per-style image direction table: `visual-language/VISUAL-LANGUAGE-FOUNDATIONS.md` § 10.

## 11 · Motion

This style lives on motion. Springs, not linear eases: `cubic-bezier(0.34, 1.56, 0.64, 1)` (overshoot) for entrances and toggles; 200–500ms. Floating elements bob subtly with scroll parallax (±8px). Segmented thumbs slide with spring. Press feedback: scale 0.97 + specular brightens. Background media drifts slowly. Hover on glass: brightness 1.1 + shadow lift, 250ms spring. `prefers-reduced-motion`: freeze parallax/drift, springs → simple fades, keep all layout stable.

## 12 · Responsive behaviour

Verify at **1440 · 768 · 390** (canonical mobile) and once at **360** (narrow floor). Responsive means recomposition, not stacking — `responsive/RESPONSIVE-FOUNDATIONS.md`.

- **Adaptation:** floating dock becomes a bottom bar under 720px; blur drops to 1 glass layer; H1→34px.
- **Non-negotiable for this style:** The floating dock becomes a bottom bar with safe-area padding; ambient motion pauses rather than continuing off-screen.

## 13 · Accessibility

- Contrast targets: body 4.5:1, large text/UI 3:1 — verify every text/background pair in this style's palette.
- Focus states: high-contrast pill outlines; the fluid material eats thin focus rings.
- Motion: this style tempts toward everything morphs and floats — continuous animation without reduced-motion fallback is the #1 failure. Every animated surface needs a `prefers-reduced-motion` static fallback.
- Common a11y failure in this style: liquid refraction distorts text near edges — keep text 16px+ with padding away from material boundaries.

The universal floor — contrast, focus, keyboard, semantics, motion, touch targets, zoom — is in `accessibility/ACCESSIBILITY.md`. This section covers what *this style specifically* gets wrong.

## 14 · When to use

Consumer products: music, fitness, smart home, wearables, camera/photo apps, social, travel booking, consumer hardware marketing (Apple-adjacent brands). Youthful, tactile, premium-consumer positioning.

## 15 · When NOT to use

Enterprise SaaS, fintech compliance dashboards, healthcare, legal, dev tools — anything where trust/seriousness beats delight. Also not for content-dense sites: glass controls over dense text destroy readability.

## 16 · Do

- Reserve glass for controls and floating chrome — content on solid surfaces
- Give every glass element the specular top highlight
- Use spring easing (slight overshoot) for all interaction
- Keep radius continuous/pill — softness is the material's identity
- Adapt tint: glass picks up the hue beneath it (dynamic tinting)
- One accent; solid CTA for the primary action
- Test contrast on the brightest frame of the background media
- Rich, moving background — glass over flat color is dead glass

## 17 · Don't

- Glass content cards, grids, or tables
- Static gray backdrop
- Linear/robotic easing (kills the "liquid")
- Sharp corners or 1px hard borders on floating elements
- More than 3 floating glass elements per view
- Long-form text directly on glass
- Emulating Apple's UI one-to-one (copy the material, not the product)
- Motion without reduced-motion fallback

## 18 · Anti-slop — liquid glass edition

The slop tell: iOS-clone UI with fake notch, five glass toolbars stacked over a stock purple mesh, springs everywhere with no purpose, "Designed for the future" hero. Real Liquid Glass: one rich scene, a few floating controls that feel physically touchable, springy motion that responds to the user. The material serves the content's media — it never replaces a layout system.

**Good vs bad**

- **Good:** Apple's iOS 26 marketing pages / visionOS — rich moving media, floating glass controls with real speculars, solid type panels, springy scroll moments.
- **Bad:** An "iPhone clone" landing — fake status bar, glass card grid with lorem feature text, translucent buttons over unreadable gradients. Slop wears the material; taste uses it.

Universal severity levels (BLOCKER / STRONG / MINOR): `ANTI-SLOP.md`.

## 19 · Style combinations

One dominant + at most one supporting style. The supporting style owns exactly one layer — typography, one section type, or micro-motion — never structure.

- **Works with:** Bento (04) — fluid surfaces inside bento containers
- **Avoid pairing with:** Editorial (11) — refraction and long-form reading are incompatible · Swiss (10) — the material contradicts the rigour

Full rules: `STYLE-COMBINATIONS.md`.

## 20 · Signature move

**A floating pill-shaped control cluster whose edges bend the content behind them** and that visibly reflows as its contents change size. The material responds; that response is the identity.

Use it **once per page**, deliberately. A signature move repeated on every element is no longer a signature.

## 21 · When to break the rules

swap liquid for solid panels in settings/forms — familiarity beats material consistency where users work

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
