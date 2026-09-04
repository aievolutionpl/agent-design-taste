# 08 Claymorphism — ready prompts

## Codex
```
Build a single-file HTML landing page for "Piggo" (pocket-money banking app
for kids & parents). Style: claymorphism — puffy inflated surfaces, soft
pastels, toy-like but structured. Fonts: Baloo 2 600/700 for headings
(H1 52px), Nunito Sans for body 16px/1.6. Palette: lilac bg #F5F1FA, white
puffy cards, deep plum text #2D2438, ONE saturated primary #7C5CFC for
CTAs, pink accent #FF8FA3 used sparingly. Signature effect: dual shadows —
box-shadow: 8px 8px 24px rgba(124,92,252,.18), -8px -8px 24px #fff, inset
0 2px 0 rgba(255,255,255,.7). Radii 24–32px on cards, 999px pill buttons
with inset 0 -4px 0 shadow and press-down active state (translateY 2px).
Layout: 1140px container, centered hero with puffy phone mockup card,
3-card feature grid (min 24px gaps so shadows don't collide), 3 pricing
cards with popular plan lifted, pill CTA band, soft footer. Rounded filled
icons only — no line icons, no hairline borders, no glass, no photography.
Motion 300ms cubic-bezier(.34,1.56,.64,1), one overshoot pop-in, no
infinite bounces. Include prefers-color-scheme dark variant (deep purple
#1E1830, dimmed surfaces, same hues) and prefers-reduced-motion reset.
```

## Claude
```
Design a claymorphism landing page for Piggo, a pocket-money banking app
for kids. The whole page should feel like soft clay you could pinch:
inflated white surfaces on a lilac #F5F1FA background, 24–32px radii,
dual shadows (tinted drop + white inner top highlight), pill buttons that
visually press down on click. Baloo 2 headings + Nunito Sans body, deep
plum text #2D2438, one saturated violet #7C5CFC reserved for actions.
Hierarchy: playful H1 → phone mockup card → CTA → 3 feature cards →
pricing → CTA band. Keep gaps generous so shadows never collide. No
glassmorphism, no line icons, no photography, no neon. One self-contained
HTML file, dark mode via prefers-color-scheme, reduced-motion reset.
```

## Lovable
```
Create a claymorphism landing page for "Piggo" (kids pocket-money app).
Strict rules: pastel lilac bg #F5F1FA, white cards with radius 24–32px and
dual soft shadows (purple-tinted drop + white top highlight), pill buttons
(999px) in violet #7C5CFC with 3D press effect, fonts Baloo 2 (headings) +
Nunito Sans (body). Sections: centered hero with puffy phone mockup, 3
feature cards, pricing (3 plans, middle one elevated), CTA band. Text
plum #2D2438, pink accent #FF8FA3 sparingly. No glassmorphism, no hairline
borders, no sharp corners, no line icons — rounded filled icons only.
```

## v0
```
Landing page, style: claymorphism (puffy 3D, soft pastels). Override
shadcn defaults: radius 24px cards / full-round buttons, replace border
separation with dual shadows — box-shadow: 8px 8px 24px rgba(124,92,252,.18),
-8px -8px 24px #fff, inset 0 2px 0 rgba(255,255,255,.7). Primary =
#7C5CFC (CTAs only), bg #F5F1FA, text #2D2438, accent #FF8FA3. Fonts:
Baloo 2 headings / Nunito Sans body 16px. Centered hero with puffy phone
card + 3 feature cards + pricing (middle plan lifted) + pill CTA band.
Buttons: inset 0 -4px 0 dark bottom edge, active translateY(2px). Motion:
300ms spring ease, single pop-in overshoot. No glass, no line icons
(use rounded filled icons), no photography, no neon gradients. Dark mode
variant: bg #1E1830, surfaces #2A2142, deep shadows. Include
prefers-reduced-motion reset.
```