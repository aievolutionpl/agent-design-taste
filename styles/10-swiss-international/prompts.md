# 10 Swiss International — ready prompts

## Codex
```
Build a single-file HTML landing page for "Rasterwerk" (an architecture and
spatial-planning studio in Zürich). Style: Swiss International — strict
12-col grid, flush-left ragged-right text, rectangles only (radius 0–2px),
hairline 1px rules (#D9D9D6) instead of shadows. Fonts: Inter Tight 700 for
H1/H2 (64px, letter-spacing -0.03em, line-height 1.06), Inter for body
16px/1.5, IBM Plex Mono for 12px uppercase index/figure labels (+0.08em,
e.g. "01/", "Fig. 02"). Palette: white bg, #111 text, #5C5C5C secondary,
ONE accent #E2231A (Swiss red) for the CTA and small highlights only.
Layout: oversized flush-left hero headline, grid-locked image block,
two-column text sections with narrow meta column, hairline-separated
project list, plain footer. No centered text, no gradients, no rounded
pill buttons, no drop shadows, no illustration. Hover: 120ms color/border
change only. Include prefers-reduced-motion reset.
```

## Claude
```
Design a Swiss International landing page for Rasterwerk, an architecture
studio. The grid is the design: decide column structure first, then place
content — flush-left only, never centered. Use Inter Tight (700, 64px H1,
-0.03em) + Inter body + IBM Plex Mono for uppercase index labels ("01/",
"Fig. 01"). Near-monochrome with one Swiss red #E2231A on the primary CTA.
Hairline rules instead of shadows, sharp corners, rectangles only. Sections
96–144px apart. Deliver as one self-contained HTML file with dark mode via
prefers-color-scheme and a reduced-motion reset. If an element isn't
structural — grid, type, or red accent — remove it. No gradients, no glass,
no invented testimonials.
```

## Lovable
```
Create a Swiss International style landing page for "Rasterwerk" (Zürich
architecture studio). Strict rules: 12-col grid, flush-left text, radius
0–2px, 1px hairlines (#D9D9D6), no shadows, no gradients, ONE red accent
(#E2231A) for CTA only. Fonts: Inter Tight headings (64px, tight) + Inter
body + IBM Plex Mono uppercase labels. Sections: oversized hero headline,
grid-locked image, two-column features with mono index numbers ("01"),
hairline project list, CTA band, minimal footer. No centered text, no
rounded pills, no glassmorphism, no fake stats.
```

## v0
```
Landing page, style: Swiss International. Override shadcn defaults: radius
0–2px, shadows OFF (use 1px borders #D9D9D6), primary = #111, accent =
#E2231A used only on the primary CTA. Font: Inter Tight headings / Inter
body / IBM Plex Mono for uppercase index labels. Flush-left ragged-right
text, 12-col grid, oversized H1 (64px, -0.03em tracking). Two-column
features with mono "01/" index numbers + hairline project table + CTA
band. No gradient meshes, no glass cards, no emoji icons — geometric line
icons at 1.5px stroke. Body 16px/1.5. Never center paragraphs.
```