# Layout Foundations

## Grids

| Grid | When | Specs |
|---|---|---|
| **12-column** | Default for SaaS/marketing | max-width 1200-1280px, gutter 24px desktop / 16px mobile |
| **Editorial** | Magazines, long-form | 6-8 col within 720-840px measure, wide side margins |
| **Asymmetric** | Editorial, portfolios | 2:1 or 3:2 splits, consistent across page |
| **Bento** | Feature-rich pages | CSS grid, tile spans 2×1/2×2, 16-24px gaps, consistent module sizes |
| **Freeform** | Brutalist/anti-grid | Intentional overlaps/rotations, but anchored to a hidden baseline |
| **Rule-of-thirds** | Imagery-led | Text on third-lines, images on thirds |

## Spacing system

One scale, everywhere (4px base):

```
4 · 8 · 12 · 16 · 24 · 32 · 48 · 64 · 96 · 128
```

- **Inside components**: 8/12/16/24.
- **Between components**: 24/32/48.
- **Between sections**: 64-128 (marketing), 48-64 (dense UI).
- **Hero padding top**: 96-160 desktop, 48-64 mobile.

## Responsive strategy

- Verify at 1440 · 768 · 390 (canonical mobile) · 360 (narrow floor).
  Full ladder and strategy: `responsive/RESPONSIVE-FOUNDATIONS.md`.
- **Desktop→tablet**: collapse 12-col to 8-col, side-by-side heroes stack.
- **Tablet→mobile**: nav → burger/overlay, grids → 1-col, bento → ordered stack
  (hero tile first!), type scale drops ~15-20%.
- Touch targets ≥ 44×44px. No hover-dependent information (must be visible on touch).
- Never scale typography with `vw` alone — clamp() with min/max.

```css
h1 { font-size: clamp(2.25rem, 5vw + 1rem, 4.5rem); }
```

## Section anatomy (marketing page)

1. Nav (sticky, 64-72px)
2. Hero (60-80vh or content-height)
3. Social proof strip (optional, quiet)
4. Features (pattern ≠ hero pattern)
5. Deep dive / how it works
6. Proof (case studies / testimonials — real ones)
7. Pricing (if applicable)
8. Final CTA
9. Footer (sitemap + real contact)

Dense app pages invert: nav → primary content → rails/panels; marketing
patterns do not leak into app UI.