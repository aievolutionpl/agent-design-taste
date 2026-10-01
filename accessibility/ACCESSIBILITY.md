# Accessibility — a quality gate, not an appendix

Accessibility is the **P2 floor** in the precedence chain (`docs/PRECEDENCE.md`).
Only brand and legal constraints sit above it, and even then the rule is
*preserve the brand, derive an accessible variant* — never *ship the failure*.

Six of the requirements on this page are 🔴 blockers in `ANTI-SLOP.md` and hard
blockers in the Design Taste Score: body contrast, mobile overflow, focus
visibility, reduced-motion handling, touch-target size, and never conveying
information by color alone. They are not opinions and they do not get traded
against aesthetics.

Target: **WCAG 2.2 Level AA**.

---

## 1. Contrast

| Content | Minimum | Notes |
|---|---|---|
| Body text | **4.5:1** | Against its *actual* background, including images and glass |
| Large text (≥24px, or ≥18.66px bold) | **3:1** | Measured in CSS pixels |
| UI component boundaries, icons carrying meaning | **3:1** | Borders, toggle tracks, chart lines, focus rings |
| Disabled elements | exempt | But then explain unavailability in adjacent text |

**How to check without guessing.** Contrast is arithmetic: relative luminance of
both colors, then `(L1 + 0.05) / (L2 + 0.05)`. Compute it from the token values —
do not eyeball it, and do not assume "looks fine on my screen."

**Where contrast fails silently**
- Text over photography or video — the ratio changes per pixel. Use an opaque
  scrim, and measure the worst region, not the average.
- Text over glass/translucent surfaces — the backdrop is unknown at author time.
  Give every glass surface an opaque fallback and measure against *that*.
- Neumorphic surfaces — same-color surfaces cannot reach 3:1 for boundaries.
  This is the structural flaw of the style, not a tuning problem.
- Placeholder text, timestamps, "secondary" grey — the most common real-world
  failure. `#999` on white is 2.8:1 and fails.

**Never rely on color alone.** Error, success, warning, chart series, status
dots, required fields, graph lines — each needs a shape, an icon, a label, or a
pattern in addition to its color.

---

## 2. Focus visibility

Every interactive element gets a visible `:focus-visible` indicator. Removing
outlines without replacing them makes the interface unusable by keyboard —
🔴 blocker, every time.

```css
:focus-visible {
  outline: 2px solid var(--color-accent);
  outline-offset: 2px;
  border-radius: inherit;
}
/* legacy reset — only ever paired with a :focus-visible replacement */
:focus:not(:focus-visible) { outline: none; }
```

- The ring needs **3:1 against both** the component and the page behind it.
  A blue ring on a blue button is invisible.
- **Make the ring solid.** A ring at 30–40% opacity composites to roughly a
  third of the contrast its hue suggests — `rgb(37 99 235 / 0.35)` on white
  measures about 1.8:1, not the 5.2:1 the colour alone would give. Every style
  in this repository shipped a translucent ring once; all of them failed. If
  you want a soft glow, put it *outside* a solid ring, not instead of one.
- Verify it, don't eyeball it: `python3 scripts/check_contrast.py` resolves each
  style's `--shadow-focus`, composites any alpha, and measures it against both
  the page and the surface.
- Style-specific traps: glass and neumorphism swallow thin rings — go thicker
  and solid; brutalism already *is* a thick outline, so keep it and add offset.
- Never let a sticky header cover the focused element. `scroll-margin-top` on
  focusable targets fixes this.

---

## 3. Keyboard

- Everything actionable by mouse is actionable by keyboard.
- Tab order follows visual order. If you reordered with CSS `order` or
  `grid-area`, you probably broke this — verify by tabbing.
- **No traps.** Focus must always be able to leave, except deliberately inside
  an open modal (where ESC must work).
- Provide a **skip link** to `<main>` as the first focusable element.
- Standard keys behave normally: ESC closes, Enter/Space activate, arrows move
  within composite widgets (tabs, menus, listboxes, sliders).
- Custom widgets follow the established pattern or they are not accessible.
  A `<div onclick>` is not a button.

---

## 4. Semantic HTML

The cheapest accessibility you will ever get. Landmarks and native elements
carry roles, states and keyboard behavior for free.

```html
<header> <nav aria-label="Main"> … </nav> </header>
<main id="main"> … </main>
<footer> … </footer>
```

- `<button>` for actions, `<a href>` for navigation. Never swapped.
- One `<h1>` per page. Never skip heading levels for visual size — change the
  scale instead.
- Lists are `<ul>` / `<ol>`. Tables are `<table>` with `<th scope>`.
- ARIA is a patch, not a foundation: a native element beats a div with roles.
  The first rule of ARIA is not to use ARIA.

---

## 5. Naming

Every control has an accessible name a screen reader can announce.

- Form fields: `<label for>`. Placeholder is **not** a label — it disappears on
  input and usually fails contrast.
- Icon-only buttons: `aria-label="Close dialog"` — descriptive, not "button".
- Images: meaningful `alt`, or `alt=""` for genuinely decorative art. `alt="image"`
  is worse than nothing.
- Links: the text makes sense out of context. Ten "Read more" links tell a
  screen-reader user nothing.
- Landmarks that repeat get names: `<nav aria-label="Footer">`.

---

## 6. Motion

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

- Any animated page without this is a 🔴 blocker.
- Reduced motion means **usable**, not merely frozen: a scroll-driven reveal
  must render in its final state, not stay invisible.
- Nothing flashes more than three times per second.
- Auto-playing motion longer than 5 seconds needs a pause control.
- Parallax and scroll-jacking are vestibular triggers. Treat them as costs.

---

## 7. Touch targets

- **≥44×44px** for anything tappable, including padding. (WCAG 2.2 sets 24×24
  as the AA minimum; 44 is the practical floor and what this repository requires.)
- ≥8px between adjacent targets.
- Small visual controls can still have a large hit area — expand with padding or
  a pseudo-element, not by making the icon bigger.

---

## 8. Zoom and reflow

- Content reflows at 320px-equivalent width without horizontal scrolling.
- 200% browser zoom loses no content or function.
- Text can be resized to 200% without clipping — avoid fixed heights on text
  containers; prefer `min-height`.
- Use `rem` for type. `px` type ignores the user's browser setting.

---

## 9. Forms

- Label above the field, always visible.
- Errors: icon + text + color, adjacent to the field, announced via
  `aria-live` or by moving focus.
- The message says how to fix it: "Enter a date after today", not "Invalid".
- `aria-describedby` links helper text and errors to the field.
- `autocomplete` on personal-data fields — it is an accessibility requirement,
  not a convenience.
- Never disable submit without telling the user what is missing.

---

## 10. Where each style tends to fail

| Style | Its characteristic failure | Fix |
|---|---|---|
| Minimalism | Light grey secondary text (`#999`) | Secondary text no lighter than `#555` on white |
| Glassmorphism | Text over unpredictable translucent backgrounds | Opaque fallback surface; measure against it |
| Liquid Glass | Refraction distorts text near edges | Text ≥16px, padded away from material boundaries |
| Bento | White text on pastel tiles | Tiles are surfaces, not an excuse to fail contrast |
| Neo-Brutalism | Neon-on-neon, yellow on white | Loud still means 4.5:1 |
| Anti-Grid | Rotated overlapping text; DOM order ≠ visual order | Keep DOM order logical; do not rotate body text |
| Neumorphism | **Structural**: same-color surfaces cannot reach 3:1 | Add real outlines, or do not use it for controls |
| Claymorphism | White text on pastel puffs | Darken the clay or darken the text |
| Skeuomorphism | Real-looking controls without real semantics | A knob is still an `<input type="range">` |
| Swiss | Justified text rivers; red accent on grey | Ragged right; check accent-on-surface ratios |
| Editorial | 15px grey serif body over long articles | ≥17px, `#333` minimum, 65–75ch measure |
| Maximalism | Text on patterned backgrounds | Solid plates behind all text |
| Y2K | Chrome and iridescent text | Dark backing plate behind metallic text |
| 3D / Spatial | Text on tilted planes; parallax on every move | Text on flat layers; static fallback |
| Kinetic Type | Animated text carrying unique information | Duplicate critical info statically |

---

## Verification protocol

Not "I considered accessibility" — these, actually performed:

1. **Tab through the entire page.** Every stop visible, order logical, no traps.
2. **Compute contrast** for the three most-used text/background pairs.
3. **Emulate `prefers-reduced-motion: reduce`.** Page fully usable.
4. **Zoom to 200%.** Nothing clipped, nothing lost.
5. **Render at 390px.** No horizontal scroll, targets ≥44px.
6. **Turn off color** (grayscale render). Every state still distinguishable.
7. **Read the DOM order** aloud. It should make sense as prose.

Automated checkers (axe, Lighthouse) catch roughly a third of issues. They are
a floor, not a pass. Steps 1, 6 and 7 are what they cannot do.

---

## In the score

Accessibility carries the **highest single weight (12/100)** in
`evaluation/DESIGN-TASTE-SCORE.md`, and eight of its failures are hard blockers
that fail a design regardless of total. That is the intended asymmetry: a
beautiful interface that excludes people is not a good interface.
