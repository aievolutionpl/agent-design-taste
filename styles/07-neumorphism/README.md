# 07 · Neumorphism (Soft UI)

**Soft extruded surfaces.**

## 01 · Overview

Surfaces extruded from a single background color. Depth comes from a matched pair of soft shadows — one light (top-left) and one dark (bottom-right) — on elements that share the background's hue. Tactile, quiet, almost physical. It is also the style with the **worst accessibility record in modern UI** — read the a11y section before using it.

## 02 · Design philosophy

A single background material, extruded. Elements do not sit on the page — they are pushed out of it or pressed into it by a matched pair of light and dark shadows. The result is quiet and tactile, and structurally low in contrast, which is precisely why it belongs on decorative surfaces and never on critical controls.

**Design decisions explained — why, not just what**

- **Why these fonts:** soft rounded sans matches the extruded material; condensed or display faces make soft UI look inflated
- **Why this radius:** large radii (16-24px) are required — soft shadows only read as extrusion on curved surfaces
- **Why this density:** low-to-medium only: every element pays a legibility tax; dense neumorphic dashboards are unusable

## 03 · Visual principles

single-hue surfaces · dual soft shadows (light + dark) · extruded "pushable" components · inset pressed states · minimal color, shape does the work · rounded, plush geometry.

## 04 · Typography

- **Recommended families (Google Fonts):** Rounded-friendly sans: Nunito Sans, Jakarta Sans, Manrope. Accent: Poppins (600–700).
- **Pairing:** Manrope (H1–H3, 700–800) + Nunito Sans (body) — friendly geometry matches the plush surfaces.
- **Scale:** H1 48/1.1 · H2 36/1.2 · H3 24/1.3 · body 16/1.65 · small 14/1.5. Soft style tolerates slightly looser leading.
- **Body:** 16px, letter-spacing 0, max 60ch.
- **Uppercase:** small pill labels only, 11–12px +0.06em.
- **CSS:**
```css
h1 { font: 800 48px/1.1 'Manrope', sans-serif; letter-spacing: -0.015em; }
body { font: 400 16px/1.65 'Nunito Sans', sans-serif; }
.pill { font: 600 11px/1 'Nunito Sans'; letter-spacing: 0.06em; text-transform: uppercase; }
```
- **Typical mistakes:** gray-on-gray text below 4.5:1; ultra-thin weights (200–300) blending into surfaces; sharp condensed fonts (wrong personality).

## 05 · Layout & grid

- **Grid:** 12-col, max 1100px, generous gutters (32px). Neumorphism works best with fewer, larger cards.
- **Spacing:** airy — sections 96px+, padding inside cards 32px+ so shadows have room to read.
- **Hero:** centered or split hero with one extruded device/widget mockup; the widget is the star.
- **Frame patterns:** centered hero with extruded widget, card trios, stat tiles, large pill CTA band.

## 06 · Visual hierarchy

- First seen: extruded hero widget, then the filled (accent) CTA, then heading. Hierarchy must come from **size and position** — elevation is too subtle to carry it alone.

## 07 · Color system

- **Light:** bg #ECF0F3 · surface same as bg (#ECF0F3 — that's the point) · text #111827 · secondary #4B5563 · shadow-dark #C8D0E0 · shadow-light #FFFFFF · accent #4F6AF0 (interactive fill only).
- **Dark:** bg #23272E · surface same · text #E5E7EB · secondary #9CA3AF · shadow-dark #14161B · shadow-light #3B424D · accent same.
- Near-monochrome + one accent. Avoid: saturated section backgrounds, gradients (they kill the matched-shadow illusion), second accent.

## 08 · Components

Buttons: raised = surface + dual shadow (`6px 6px 12px dark, −6px −6px 12px light`); pressed = **inset** (`inset 4px 4px 8px dark, inset −4px −4px 8px light`). Primary CTA: filled accent with soft matching shadow — the ONLY high-contrast control. Cards: raised panels, radius 20–24px. Inputs: **inset** wells, radius 12–16px. Toggles: inset track + raised knob. Icon buttons: raised circles/squircles, must include a visible border or label for a11y. Tabs: raised active pill on an inset track. Sliders: inset track, raised thumb. Never: sharp corners (radius < 8px breaks the softness), heavy borders, hard shadows.

Anatomy and the required state matrix (default / hover / focus-visible / active / disabled / loading / error / success) are universal — see `component-patterns/COMPONENT-PATTERNS.md`. This section defines the *skin*, not the behaviour.

## 09 · Shape language

Radius 12–28px, generous. No visible borders — boundary = shadow pair. Depth = soft blur (8–20px) with matched angles (light source top-left). Two elevation levels only: raised and inset. Focus rings: 3px solid accent offset 2px — always visible.

## 10 · Imagery & visual direction

Fits: soft 3D-feel product renders, pastel gradients *inside* accent elements only, rounded line icons (2px), frosted overlays. Breaks cohesion: brutal black borders, neon, hard shadows, dense photography (photo edges clash with extruded surfaces).

Per-style image direction table: `visual-language/VISUAL-LANGUAGE-FOUNDATIONS.md` § 10.

## 11 · Motion

Soft and springy: 200ms ease-out on press (raise→inset swap is the signature interaction); cards lift 2px on hover. `prefers-reduced-motion`: disable lift, keep instant inset state change. Focus states must never be shadow-only — use the accent ring.

## 12 · Responsive behaviour

Verify at **1440 · 768 · 390** (canonical mobile) and once at **360** (narrow floor). Responsive means recomposition, not stacking — `responsive/RESPONSIVE-FOUNDATIONS.md`.

- **Adaptation:** cards stack; keep 24px+ page margins so shadows don't clip at the viewport edge.
- **Non-negotiable for this style:** Keep ≥24px page margins so the dual shadows do not clip at the viewport edge, and give every control a real border at this size.

## 13 · Accessibility

> ### ⚠️ Contrast & accessibility — the defining problem
> Neumorphism's signature look **requires** low contrast between surface and background (typically ΔL ≤ 10%). That breaks the WCAG floor in three compounding ways:
> 1. **Component boundaries fail 1.4.11 Non-text Contrast (3:1):** a `#E0E0E0` card on `#ECF0F3` bg is ~1.2:1. Shadows are the only edge cue — they disappear on cheap/low-gamma screens and in bright light.
> 2. **Icon-only and ghost controls become invisible:** no border, no fill — just a soft bump. Users with low vision, older screens, or sunlight cannot find them at all.
> 3. **Disabled-looking enabled states:** everything soft and low-contrast reads as "off". This is the practical failure mode reported repeatedly since the style's 2020 wave: controls that look decorative get missed, and users click the wrong thing.
> **Mitigation if you must use it:** keep ≥ 3:1 contrast for all interactive boundaries (add a visible 1px border or darker fill on hover/focus), never rely on shadow alone to signal interactivity, always show visible focus rings (`:focus-visible`, 3px accent ring), and put text in #111-on-light / #F5F5F5-on-dark with ≥ 4.5:1.

- Contrast targets: body 4.5:1, large text/UI 3:1 — verify every text/background pair in this style's palette.
- Focus states: critical: soft-shadow surfaces swallow focus rings — use strong color rings (3px accent), test on real keyboards.
- Motion: this style tempts toward pressing animations with deep dual shadows — subtle 2-4px travel is enough, more looks like melting. Every animated surface needs a `prefers-reduced-motion` static fallback.
- Common a11y failure in this style: THE structural flaw: same-color surfaces mean borders and states have almost no contrast — WCAG 1.4.11 (3:1 non-text) is usually impossible without adding outlines; use only for decorative surfaces, never for critical controls.

The universal floor — contrast, focus, keyboard, semantics, motion, touch targets, zoom — is in `accessibility/ACCESSIBILITY.md`. This section covers what *this style specifically* gets wrong.

## 14 · When to use

Smart-home controls, ambient/wellness apps, gadget companion apps, decorative hero widgets, concept showcases. Audience: consumer, relaxed, tactile.

## 15 · When NOT to use

- **Never:** banking, healthcare, government, accessibility-first products, dense data tools, dashboards with many controls, anything WCAG-compliance-audited.
- **Avoid:** dark-mode-heavy products (soft shadows fail harder on dark), low-end display audiences, enterprise procurement checklists.
- **OK only for:** decorative marketing surfaces, smart-home/ IoT companion apps, weather/ambience widgets, landing heroes — i.e. content that can fall back to plain flat panels without loss. If a control must be found and used by everyone, neumorphism is the wrong tool; use it as garnish over an accessible base, not as the base.
Fintech/banking, healthcare, government, enterprise dashboards, data-dense tools, or any product with an accessibility requirement. The style's core mechanism (surface≈background) is structurally incompatible with WCAG 1.4.11. Use flat cards with clear borders instead.

## 16 · Do

- Match surface and background hue (that's the aesthetic)
- Always pair shadows: light top-left + dark bottom-right
- Use inset for pressed/active and input wells
- One filled accent CTA — your guaranteed-contrast control
- Add a visible focus ring and a fallback border on interactive elements
- Keep card count low; shadows need whitespace
- Test on a cheap display and in sunlight

## 17 · Don't

- Rely on shadow alone to mark a button
- Put gray text below 4.5:1 contrast
- Use it in dark-heavy data UIs or compliance contexts
- Hard shadows, sharp corners, heavy borders
- Stack neumorphic cards on neumorphic cards (mush)
- Gradient backgrounds behind neumorphic surfaces (shadows stop matching)

## 18 · Anti-slop — neumorphism edition

Everything soft but nothing clickable, white-on-white text, gray ghost buttons everywhere, neumorphic tables (never), random pastel gradients behind the soft panels — slop here = softness applied to a context that needs legibility. If you can't screenshot it and still point at the primary CTA in one second, it failed.

**Good vs bad**

- **Good:** smart-home dashboard concept — 6 large extruded tiles, inset temperature well, one accent-filled "away mode" button, all labels ≥ 4.5:1.
- **Bad:** neumorphic settings page — ghost icon-buttons, gray labels at 1.6:1, five levels of soft elevation, no visible focus anywhere. It looks like a screensaver and behaves like one.

Universal severity levels (BLOCKER / STRONG / MINOR): `ANTI-SLOP.md`.

## 19 · Style combinations

One dominant + at most one supporting style. The supporting style owns exactly one layer — typography, one section type, or micro-motion — never structure.

- **Works with:** Minimalism (01) — a flat, accessible base with neumorphic surfaces used as decorative garnish only
- **Avoid pairing with:** Neo-Brutalism (05) and Anti-Grid (06) — opposite shadow languages · Swiss (10) — soft extrusion contradicts grid rigour · Maximalism (12) — soft surfaces disappear in noise

Full rules: `STYLE-COMBINATIONS.md`.

## 20 · Signature move

**A control that switches from raised (outset dual shadow) to pressed (inset)** on activation, appearing to physically depress into the surface. Pair it with a real border so it is still findable.

Use it **once per page**, deliberately. A signature move repeated on every element is no longer a signature.

## 21 · When to break the rules

add ONE flat, high-contrast control color (a real button) — pure monochrome neumorphism fails; hybrid soft-plus-solid works

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
