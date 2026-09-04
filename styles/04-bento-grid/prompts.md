# 04 Bento Grid — ready prompts

## Codex
```
Build a single-file HTML landing page for "Pulseboard" (analytics tool for
indie SaaS founders). Style: bento grid — one dense modular grid, no
separate stacked sections. Fonts: Space Grotesk 600 for H1/H2/tile titles
(letter-spacing -0.02em), Inter 15px/1.5 for tile body, IBM Plex Mono 11px
uppercase tile labels (+0.08em). Palette: #F4F4F2 page bg, white tiles,
#E2E2DE 1px tile borders, 16px radius, ONE accent #0D9488 used on a single
CTA tile and key metrics. Grid: CSS Grid, 12-col, 1240px container, 16px
gaps — one 8-col hero tile with headline+CTA, 4-col column with two
stacked stat tiles, then mixed 4/4/4 and 6/6 rows with a real mini chart
(inline SVG sparkline), a feature tile, a screenshot tile and a pricing
tile. Top-left align all tile content. Hover: tile lifts 2px, border
darkens, 180ms. Responsive: 2-col below 1024px, 1-col below 640px, spans
collapse in reading order. No gradients, no glassmorphism, no emoji icons,
no rainbow pastel tiles. Include prefers-reduced-motion reset.
```

## Claude
```
Design a bento-grid landing page for Pulseboard, an analytics tool for
indie SaaS founders. The whole page is one asymmetric CSS grid: decide
tile hierarchy first — one dominant tile (headline + CTA), one accent
tile, stat tiles with real mono numbers, the rest neutral. Space Grotesk
headings, Inter body, IBM Plex Mono labels. White tiles on #F4F4F2, 1px
#E2E2DE borders, 16px radius, tight 16px gaps, single teal accent #0D9488.
Every tile has exactly one job and real content (metrics, chart, copy) —
no filler tiles. One self-contained HTML file, dark mode via
prefers-color-scheme, reduced-motion reset. No gradients, no glass, no
emoji tiles, no invented statistics.
```

## Lovable
```
Create a bento-grid landing page for "Pulseboard" (SaaS analytics). Rules:
everything lives in ONE modular CSS grid (12-col, 16px gap, 1240px
container); tiles are white with 1px #E2E2DE borders, 16px radius; page bg
#F4F4F2; fonts Space Grotesk (headings) + Inter (body) + IBM Plex Mono
(labels); ONE accent #0D9488. Tile mix: large hero tile (8-col), stacked
stat tiles (4-col), chart tile with SVG sparkline, feature tiles, pricing
tile, CTA tile. Left/top-aligned text inside tiles. Responsive collapse:
2-col at 1024px, 1-col at 640px. No gradients, no glassmorphism, no
multi-color pastel tiles, no fake numbers.
```

## v0
```
Landing page, style: bento grid. Build the page as a single CSS grid with
asymmetric tile spans (8/4, 4/4/4, 6/6) — not stacked sections. Override
shadcn defaults: card radius 16px, 1px borders #E2E2DE, no shadows (hover
= 2px lift only), page bg #F4F4F2, ONE accent #0D9488. Fonts: Space
Grotesk headings / Inter body / IBM Plex Mono for tile labels and metric
numbers (uppercase 11px, +0.08em tracking). Include a sparkline chart tile
(inline SVG), stat tiles with real units, a pricing tile and a dark CTA
tile. Top-left align tile content. Lucide icons 1.5px stroke only. No
gradient tiles, no glass, no emoji.
```