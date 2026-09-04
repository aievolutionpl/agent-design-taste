# 10 · Swiss International

**Overview:** The grid is the design. Rooted in Josef Müller-Brockmann's International Typographic Style: objective photography, flush-left ragged-right text, a mathematical grid, and a single loud accent — usually red — against near-monochrome.

**Visual principles:** strict modular grid · Helvetica-family grotesks · flush-left, ragged-right · red accent, used sparingly · asymmetric balance within the grid · objective, type-led hierarchy.

## Typography
- **Recommended families (Google Fonts):** Grotesk display: Inter Tight, Archivo (Helvetica surrogates). Text: Inter, Roboto. Mono (grid/annotation labels): IBM Plex Mono.
- **Pairing:** Inter Tight (H1–H2, 700, tight tracking) + Inter (H3–body) + IBM Plex Mono (12px uppercase grid labels, figure numbers).
- **Scale:** H1 64/68 (tight leading, -0.03em) · H2 40/44 · H3 28/34 · H4 22/28 · H5 18/24 · H6 16/22 · body 16/1.5 · small 13/1.4.
- **Body:** 16px, line-height 1.5, flush-left ragged-right, never justified. Measure 60–70ch.
- **Uppercase:** small mono labels and legend text only (+0.08em); headings stay sentence case but large.
- **CSS:**
```css
h1 { font: 700 64px/1.06 'Inter Tight'; letter-spacing: -0.03em; }
body { font: 400 16px/1.5 'Inter'; text-align: left; }
.grid-label { font: 500 12px/1 'IBM Plex Mono'; letter-spacing: 0.08em; text-transform: uppercase; }
```
- **Typical mistakes:** centered text (breaks the system); rounded friendly fonts; gradient accents; decorative weights of the same family; ignoring baseline alignment across columns.

## Layout & Frames
- **Grid:** 12-col (or 6-col), max-width 1280px, visible column logic — elements snap to columns, sometimes with thin vertical hairlines marking the grid.
- **Spacing:** derived from a base module (8px); sections 96–144px apart; whitespace is structural, not decorative.
- **Hero:** oversized headline filling the top band, flush left, often with a small index/figure number ("01/") in mono; image block locked to the grid on the right or below.
- **Frame patterns:** grid-hero with index numbers, multi-column text sections with hairline column rules, full-width image band, offset two-column content (wide text + narrow meta column).
- **Responsive:** 12→4 columns, H1→36px, hairline column rules drop first, meta columns stack under text.

## Visual hierarchy
- First seen: the huge headline, then the red accent element, then the image. Eye path: headline → accent CTA → body column → caption. Size does the ranking; weight rarely varies beyond 400/700.

## Color system
- **Light:** bg #FFFFFF · surface #F4F4F2 · text #111111 · secondary #5C5C5C · border #D9D9D6 · primary action #111111 · accent #E2231A (Swiss red — one only).
- **Dark:** bg #0C0C0C · surface #171717 · text #F2F2F0 · border #2A2A2A · accent same red.
- Near-monochrome everywhere except the red. Avoid: gradients, pastels, second accent, tinted section backgrounds.

## Components
Buttons: rectangular (radius 0–2px), solid black or red fill, uppercase mono label. Cards: flat rectangles separated by 1px hairlines or whitespace, no radius drama. Navbar: thin top bar, logo left, mono links, hairline bottom border. Inputs: 1px border, square corners, label above in mono caps. Tabs: underline indicator, flush left. Pricing: grid table with hairline rules, figures in mono. Dashboards: grid-locked panels, hairline dividers. Modals: plain white panel, sharp corners. Badges: outline rectangles. Tables: strict hairline rows, mono numerals. Captions: 12–13px mono, prefixed "Fig. 01".

## Shape language
Radius 0–2px — rectangles only. Hairlines (1px #D9D9D6) instead of shadows. Depth = position on the grid, never elevation. Icons: geometric line, 1.5px stroke, aligned to grid.

## Visual direction
Fits: black-and-white or duotone photography, cropped tight; geometric line icons; no illustration, no 3D. Breaks cohesion: gradients, glass, soft shadows, emoji, decorative blobs.

## Motion & Interaction
Nearly none: hover 120ms color/border swap, link underline appear, page-load fade of 8px translateY once. `prefers-reduced-motion`: disable all. The grid should feel printed, not animated.

## When to use
Design studios, architecture, exhibitions, cultural institutions, engineering/industrial, type foundries, portfolios. Audience expects rigor and objectivity.

## When NOT to use
Warm consumer brands, kids products, hospitality — the system reads austere; playful or editorial-soft styles land better there.

## Do
- Snap every element to the grid
- Flush-left, ragged-right text
- One red accent for actions/highlights
- Oversized grotesk headlines, tight leading
- Mono labels for indexes, figures, metadata
- Hairline rules as structure
- Rectangles, sharp corners

## Don't
- Centered paragraphs or headings
- Rounded radii > 4px
- Gradients or second accent
- Drop shadows
- Justified text with rivers
- Decorative illustration
- Mixing two display faces

## Anti AI-slop (Swiss edition)
Gradient hero text, purple CTAs, glass cards, floating blobs, "✨ premium" badges — all slop. If Müller-Brockmann wouldn't set it, cut it.

## Good vs Bad examples
- **Good:** Müller-Brockmann concert posters online — grid, Helvetica-scale grotesk, one red, index numbers, nothing floats.
- **Bad:** "Swiss-style" landing with rounded purple buttons, centered gradient hero and soft shadows — Swiss typography as decoration over a default template.
## 14 · Accessibility Notes
- Contrast targets: body 4.5:1, large text/UI 3:1 — verify every text/background pair in this style's palette.
- Focus states: strict 2px black outline, offset to the grid — focus is part of the system.
- Motion: this style tempts toward this style barely animates — if you're adding parallax you've left Swiss; fades ≤200ms max. Every animated surface needs a `prefers-reduced-motion` static fallback.
- Common a11y failure in this style: red accent on gray text; also justified text creating rivers — keep text ragged-right unless hyphenation is managed.

## 15 · Design Decisions Explained (why, not just what)
- **Why these fonts:** neo-grotesks (Helvetica family, Inter, Archivo) are the style — typography IS the design; a serif display would be a different style
- **Why this radius:** 0 radius: the grid and the rectangle are sacred — rounding corners softens the rigor into generic modern UI
- **Why this density:** structured medium-high density: whitespace is planned, not generous — every gap sits on the grid
- **Signature move:** the ONE element that makes a page instantly recognizable as this style — use once per page, deliberately.
- **When to break the rules:** break the grid only as an accent (one rotated element, one photo bleeding off-grid) — systematic Swiss with one rupture is the master move
