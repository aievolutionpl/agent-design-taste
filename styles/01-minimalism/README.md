# 01 · Minimalism

**Less, but better.**

## 01 · Overview

Less but better. Every element earns its place through function; whitespace, type and one accent color do all the expressive work.

## 02 · Design philosophy

"Less, but better." The design's job is to disappear so the content can act. Every element must justify itself functionally; decoration is treated as a failure of editing rather than a layer of polish. What remains — whitespace, typography and one accent color — does all the expressive work.

**Design decisions explained — why, not just what**

- **Why these fonts:** a neutral grotesk carries restraint without personality overload; the whitespace does the expressing — a display serif here would fight the quietness
- **Why this radius:** small radii (8-12px) signal precision; pill-everything would make it look like a consumer app, sharp 0 can read harsh in B2B
- **Why this density:** low density is the point — but never below the information threshold: a page with one sentence is empty, not minimal

## 03 · Visual principles

extreme restraint · generous whitespace · one accent color · typography-led hierarchy · invisible chrome · content is the interface.

## 04 · Typography

- **Recommended families (Google Fonts):** Text/Sans: Inter, Instrument Sans, Jakarta Sans. Grotesk: Archivo. Serif accent (optional): Newsreader. Mono: IBM Plex Mono.
- **Pairing:** Archivo (H1–H2, 600) + Inter (H3–body) + IBM Plex Mono (labels/data).
- **Scale:** H1 56/64 · H2 40/48 · H3 28/36 · H4 22/30 · H5 18/26 · H6 16/24 · body 17/1.6 · small 14/1.5.
- **Body:** 17px, line-height 1.6, letter-spacing 0. Measure 65ch.
- **Uppercase:** only 11–12px eyebrow labels, +0.1em tracking, never headings.
- **CSS:**
```css
h1 { font: 600 56px/1.15 'Archivo'; letter-spacing: -0.02em; }
body { font: 400 17px/1.6 'Inter'; }
.eyebrow { font: 500 12px/1 'IBM Plex Mono'; letter-spacing: 0.1em; text-transform: uppercase; }
```
- **Typical mistakes:** thin (200) weights on dark bg; centered paragraphs; 6 weights in play; decoration instead of hierarchy.

## 05 · Layout & grid

- **Grid:** 12-col, max-width 1200px, gutters 24px. Freeform only in hero.
- **Spacing:** 8-base scale; sections 96–128px apart.
- **Hero:** split hero or centered hero with one large image. Nothing floats.
- **Frame patterns:** split hero, centered hero, alternating features, full-bleed image sections.

## 06 · Visual hierarchy

- First seen: H1, then primary CTA, then hero visual. One primary action per screen. Eye path: headline → sub → CTA → proof.

## 07 · Color system

- **Light:** bg #FFFFFF · surface #F7F7F5 · text #111111 · secondary #555555 · border #E5E5E2 · primary action #111111 · accent #2563EB (one only).
- **Dark:** bg #0A0A0A · surface #161616 · text #F5F5F4 · border #262626 · accent same.
- Saturation near-zero except accent. Avoid: pastel gradients, second accent, colored section backgrounds.

## 08 · Components

Buttons: solid black (or white on dark), 12px radius max, no shadows. Cards: flat, 1px border, no elevation. Navbar: 64px, logo left, 3–5 links, text CTA. Inputs: 1px border, 8px radius, label above. Tabs: underline indicator. Pricing: whitespace separates plans, no "most popular" confetti. Dashboards: border-separated, not shadow-separated. Modals: plain panel, dim backdrop. Badges: outline only. Tooltips: dark, minimal. Tables: hairline rows.

Anatomy and the required state matrix (default / hover / focus-visible / active / disabled / loading / error / success) are universal — see `component-patterns/COMPONENT-PATTERNS.md`. This section defines the *skin*, not the behaviour.

## 09 · Shape language

Radius 8–12px (or 0 for sharp minimal). Borders over shadows. Depth = spacing, not elevation. No strokes on icons > 1.5px relative weight.

## 10 · Imagery & visual direction

Fits: real photography (one treatment), line icons, no illustration, no 3D, no grain. Breaks cohesion: gradients, mixed icon fills, decorative blobs, emoji.

Per-style image direction table: `visual-language/VISUAL-LANGUAGE-FOUNDATIONS.md` § 10.

## 11 · Motion

Minimal: hover 150ms ease-out (opacity/border), reveals translateY 16px/400ms once. `prefers-reduced-motion`: disable all. If it needs motion to be interesting, the design failed.

## 12 · Responsive behaviour

Verify at **1440 · 768 · 390** (canonical mobile) and once at **360** (narrow floor). Responsive means recomposition, not stacking — `responsive/RESPONSIVE-FOUNDATIONS.md`.

- **Adaptation:** drop gutters to 16px, H1→34px mobile, stack split heroes.
- **Non-negotiable for this style:** The accent stays the only color. Do not add a second accent to compensate for the whitespace you lost.

## 13 · Accessibility

- Contrast targets: body 4.5:1, large text/UI 3:1 — verify every text/background pair in this style's palette.
- Focus states: a 2px accent-colored ring, never just a color change.
- Motion: this style tempts toward parallax and scroll reveals that add nothing to a quiet page. Every animated surface needs a `prefers-reduced-motion` static fallback.
- Common a11y failure in this style: light gray secondary text (#999 on white) fails 4.5:1 — keep secondary ≥ #555.

The universal floor — contrast, focus, keyboard, semantics, motion, touch targets, zoom — is in `accessibility/ACCESSIBILITY.md`. This section covers what *this style specifically* gets wrong.

## 14 · When to use

SaaS, fintech, health, corporate, enterprise, premium/luxury-adjacent, dev docs. Audience expects clarity and trust.

## 15 · When NOT to use

Youth brands needing personality, events, gaming, kids products — minimalism reads cold; maximal/expressive styles convert better there.

## 16 · Do

- One accent color, used for actions only
- Whitespace at section level (96px+)
- Real photography, single treatment
- Hairline borders, flat surfaces
- Typography carries hierarchy
- Left-align body text
- One primary CTA per view
- Kill any element you can't justify

## 17 · Don't

- Gradients "for depth"
- Three font families
- Decorative illustration
- Colored info-box sections
- Shadow stacking
- Uppercase headings
- More than one accent
- Fake stats filling whitespace

## 18 · Anti-slop — minimalism edition

Purple accents, glass cards, gradient text, "Trusted by 50,000+ teams" walls, floating 3D shapes — all slop here. In minimalism slop = anything added without function.

**Good vs bad**

- **Good:** Stripe docs — flat surfaces, hairlines, one blue, type does everything.
- **Bad:** minimalist landing with glass nav, gradient blob hero and neon CTA — three styles fighting, zero restraint.

Universal severity levels (BLOCKER / STRONG / MINOR): `ANTI-SLOP.md`.

## 19 · Style combinations

One dominant + at most one supporting style. The supporting style owns exactly one layer — typography, one section type, or micro-motion — never structure.

- **Works with:** Swiss (10) — grid rigour over minimalist restraint · Kinetic Typography (15) — a kinetic hero headline only · Claymorphism (08) — puffy accents on a restrained palette · 3D/Spatial (14) — one 3D centrepiece, minimal everything else
- **Avoid pairing with:** Y2K (13) — nostalgia needs density; starved of it, the pairing just reads as odd

Full rules: `STYLE-COMBINATIONS.md`.

## 20 · Signature move

**One accent color, reserved exclusively for actions,** on an otherwise achromatic page — so the single blue thing on screen *is* the thing to click. Use it for the primary action and nothing else.

Use it **once per page**, deliberately. A signature move repeated on every element is no longer a signature.

## 21 · When to break the rules

allow ONE expressive element (oversized number, single accent illustration) when restraint starts reading as blandness — break the pattern deliberately, once

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
