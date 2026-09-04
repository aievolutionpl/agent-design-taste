# Responsive Foundations

**Responsive does not mean "stack everything vertically."**

Stacking is what happens when nobody decided. Real responsive design is
*recomposition*: at each viewport the hierarchy, the crop, the navigation and
sometimes the content itself are different, because the reading situation is
different.

---

## The canonical viewport ladder

One ladder for the whole repository. Do not invent others.

| Width | Name | Role | Checked |
|---|---|---|---|
| **1440** | Desktop | Primary composition — where the design is authored | always |
| 1024 | Laptop / tablet landscape | Optional intermediate | when the 12-col grid breaks awkwardly |
| **768** | Tablet | Adaptation — where two-column layouts must decide | always |
| **390** | **Mobile (canonical)** | **Primary verification viewport** — check first | always |
| 360 | Narrow floor | Regression only: overflow, clipping, wrapping | before delivery |

**390 × 844** is the canonical mobile check. **360** is the narrow floor: if the
layout holds at 360 it holds at every width above it. Earlier versions of this
repository disagreed with themselves here — 390 is now the single canonical
number, everywhere.

Breakpoints in CSS are where *the layout breaks*, not where a device sits. The
ladder above is what you **verify**; the breakpoints you **write** come from
the content.

---

## Three compositions, not one that shrinks

### Desktop (1440) — compose
Horizontal relationships available: side-by-side comparison, sticky columns,
persistent navigation, multi-column reading. Use the width for *relationships*,
not for making things bigger.

### Tablet (768) — adapt
The decision point. Every two-column relationship either survives at ~360px per
column or it does not. Sidebars collapse to icons or drawers. 12-col grids drop
to 8 or 6. Type scale steps down ~10%.

### Mobile (390) — recompose
Not the desktop page, narrower. Ask three questions:

1. **What comes first?** Source order becomes reading order. The most important
   thing goes first — which is often *not* what was top-left on desktop.
2. **What gets a different crop?** Landscape hero imagery becomes portrait,
   cropped to the subject.
3. **What gets dropped or deferred?** Decorative columns, secondary nav, and
   "also see" rails can move behind progressive disclosure. Content the user
   came for never gets hidden.

---

## Content priority beats source order

Write the DOM in the mobile priority order and let CSS rearrange it upward.
Rearranging *downward* with `order` or `grid-area` breaks the reading order for
screen readers and keyboard users — the visual order changes, the DOM does not.

```css
/* mobile-first: DOM order is the reading order */
.hero { display: grid; gap: var(--spacing-6); }

@media (min-width: 768px) {
  .hero { grid-template-columns: 1.2fr 1fr; align-items: center; }
}
```

If you must reorder visually, verify tab order afterwards. Every time.

---

## Fluid type

Never scale type with `vw` alone: unreadable at 320px, absurd at 2560px. Always
`clamp()`, and always include a `rem` term in the fluid middle so the text still
responds to the user's browser font-size setting.

```css
h1 { font-size: clamp(2.25rem, 1.5rem + 3.5vw, 4.5rem); line-height: 1.05; }
p  { font-size: clamp(1rem, 0.95rem + 0.3vw, 1.125rem); line-height: 1.6; }
```

- Body never below **16px** on mobile — and on iOS, an input below 16px zooms
  the page on focus.
- Measure stays 60–75 characters at every width. On mobile that usually means
  the container, not a max-width.
- Display headings need **deliberate line breaks** at each viewport. A hero
  headline that wraps by accident looks like a bug because it is one.

---

## Grid collapse strategy

| Desktop | Tablet | Mobile |
|---|---|---|
| 12 columns | 8 columns | 4 columns |
| Gutter 24px | 20px | 16px |
| Container 1200–1280px | fluid, 32px margins | fluid, 20–24px margins |
| 4-up card row | 2-up | 1-up (or 2-up for small tiles) |
| 3-up feature row | 2-up + 1 | 1-up, priority ordered |
| Bento with hero tile | 2 columns, hero spans both | single column, **hero tile first** |
| Sidebar + content | icon rail + content, or drawer | drawer or bottom tabs |
| Data table | sticky first column + horizontal scroll | one card per row |

---

## Navigation transformation

| Desktop | Mobile | When |
|---|---|---|
| Top bar, 4–6 links + CTA | Burger overlay + CTA visible in the bar | Marketing sites |
| Top bar, 7+ links | Overlay with grouped sections | Large sites |
| Persistent sidebar | Bottom tab bar (≤5) | Apps used repeatedly |
| Persistent sidebar | Drawer | Apps with many destinations |
| Mega menu | Accordion inside an overlay | E-commerce, documentation |

The primary CTA never hides behind a hamburger. It stays in the bar.

---

## Touch

- **Targets ≥44×44px**, including padding. Spacing between adjacent targets
  ≥8px so a thumb cannot hit two.
- **No hover-only information.** Anything revealed by hover must also appear on
  focus and be reachable by tap.
- **Thumb zones**: primary actions in the lower-middle third; destructive
  actions away from it.
- **Safe areas**: `env(safe-area-inset-bottom)` on fixed bottom bars.
- **Gestures need alternatives.** Swipe-to-delete also needs a visible button.

---

## Imagery across breakpoints

- **Change the crop, not the scale.** `<picture>` with art-directed sources:

```html
<picture>
  <source media="(min-width: 768px)" srcset="hero-wide.avif" type="image/avif">
  <source media="(min-width: 768px)" srcset="hero-wide.jpg">
  <img src="hero-portrait.jpg" alt="…" width="780" height="975" loading="eager">
</picture>
```

- Always set `width`/`height` (or `aspect-ratio`) — layout shift is a real
  usability failure, not a metric.
- Below 768px: drop background video to a poster image.
- Below 768px: replace live 3D canvases with a static render.

---

## Progressive disclosure — the honest version

Legitimate on mobile: secondary navigation, long specification tables, extended
FAQs, filter panels, "related items" rails.

**Not** legitimate: the thing the user came for. If a mobile user has to expand
something to reach the primary content, the mobile page is wrong — not the user.

Accordions must be `<button>` + `aria-expanded`, and their content must be
findable by in-page search (rendered, not lazily absent from the DOM).

---

## Zoom and reflow

WCAG requires content to reflow at 320px-equivalent width without two-axis
scrolling, and to remain usable at 200% zoom.

- Test 200% browser zoom at 1440 — this is *not* the same as viewing at 720px.
- Use `rem` for type and container queries or `%`/`fr` for layout.
- Fixed-height containers with overflowing text are the most common zoom
  failure. Prefer `min-height`.

---

## Verification checklist

At 1440, 768 and 390, and once at 360:

- [ ] No horizontal scroll (🔴 blocker at 390)
- [ ] Reading order matches visual order
- [ ] Every touch target ≥44px on mobile
- [ ] Type readable: body ≥16px, measure ≤75ch
- [ ] Images re-cropped, not squeezed
- [ ] Navigation transformed, not shrunk
- [ ] Tables handled by a real strategy, not by shrinking
- [ ] Hero headline breaks where you intended
- [ ] Nothing important behind progressive disclosure
- [ ] 200% zoom still usable
- [ ] Bottom-fixed elements clear the safe area
