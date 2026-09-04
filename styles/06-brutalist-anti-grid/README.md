# 06 · Brutalist Anti-Grid

**Overview:** Deliberate disorder with intent. The grid exists to be broken: columns bleed past their edges, cards overlap, elements rotate a few degrees, and heavy borders + hard offset shadows replace softness. Loud, raw, unapologetic — but every break is choreographed, never accidental.

**Visual principles:** intentional broken grid · overlaps with z-index play · heavy 2–4px borders · hard offset shadows (solid, no blur) · acid accent · raw utility surfaces · tilt and misalignment as composition · typography as image.

## Typography
- **Recommended families (Google Fonts):** Display: Archivo Black, Anton, Space Grotesk. Text: Space Grotesk, Inter. Mono: Space Mono, JetBrains Mono.
- **Pairing:** Archivo Black (H1–H2, all-caps welcome) + Space Grotesk (H3–body) + Space Mono (labels, indexes, meta).
- **Scale:** H1 72/0.95 (tight, can exceed container) · H2 48/1.05 · H3 28/1.2 · body 16/1.6 · small 14/1.5. Headings may be wider than their column — that's the point.
- **Body:** 16px, line-height 1.6, max 55ch, left-aligned. No centered paragraphs.
- **Uppercase:** allowed on headings (tight tracking −0.01em to −0.03em); mono labels 12px uppercase +0.08em.
- **CSS:**
```css
h1 { font: 400 72px/0.95 'Archivo Black', sans-serif; letter-spacing: -0.02em; text-transform: uppercase; }
body { font: 400 16px/1.6 'Space Grotesk', sans-serif; }
.meta { font: 400 12px/1 'Space Mono', monospace; letter-spacing: 0.08em; text-transform: uppercase; }
```
- **Typical mistakes:** slight pastel softness (kills the style); centered layouts; many rotations making chaos; readable-but-boring grid that "sort of" breaks; kerning left untouched at huge sizes.

## Layout & Frames
- **Grid:** base 12-col grid is laid out, then intentionally broken — cards push past their column edge (negative margins), neighbors overlap 20–80px, one element per section is rotated −2° to 2.5°, some elements have a fixed z-index ladder (1/2/3).
- **Spacing:** irregular on purpose — pairs like 24/64 or 40/40/120. Never perfectly rhythmic.
- **Hero:** oversized headline overflowing its column, supporting block overlapping it from below-right, one rotated sticker/badge pinned on top (z-index 3).
- **Frame patterns:** broken hero, offset card clusters, full-bleed strip sections, misaligned footer columns.
- **Responsive:** collapse the overlaps to stacked blocks on mobile (overlap ≤ 8px or none), keep heavy borders and hard shadows, rotations simplify to 0–1°.

## Visual hierarchy
- First seen: giant headline, then the acid-accent CTA, then the overlapping proof card. Eye path is forced by size + offset, not whitespace. One primary CTA.

## Color system
- **Light:** bg #F4F1EA (paper) · surface #FFFFFF · text #111111 · secondary #444444 · border #111111 (heavy 2–3px) · primary action #111111 · accent #CCFF00 or #FF4D00 (one, brutal).
- **Dark:** bg #141414 · surface #1E1E1E · text #F2F2F2 · border #F2F2F2 · accent same, on dark prefer #CCFF00 for contrast.
- Saturation: everything near-monochrome except the single acid accent. Avoid: gradients, pastels, two accents.

## Components
Buttons: solid black block (white text) or accent block (black text), 0 radius, 2px border, hover = translate(−4px,−4px) + 4px offset shadow grows to 8px. Cards: white surface, 2px black border, 8px hard shadow (0 blur, offset 8px 8px 0 #111). Navbar: full-width bar with heavy bottom border, mono links, index numbers "01/02/03". Inputs: 0 radius, 2px border, label as mono uppercase. Tabs: square boxes with active = filled black. Pricing: cards at different vertical offsets, most expensive rotated +1°. Badges/stickers: rotated pills with 2px border, pinned corners. Tables: heavy 2px outer border, 1px inner lines. Modals: white panel, 2px border, 12px hard shadow, sharp corners.

## Shape language
Radius 0 everywhere (exception: pill stickers). Borders 2–4px solid. Shadows: hard, solid color, no blur — depth = offset distance, not softness. Rotation −2.5° to +2.5°, max 1–2 rotated elements per viewport.

## Visual direction
Fits: raw B&W photography with harsh contrast, photocopy/scan textures, index numbers, arrows drawn as SVG lines, marquee strips. Breaks cohesion: soft glass, gradients, pastel illustration, cute rounded 3D.

## Motion & Interaction
Snappy and mechanical: hover transforms 120ms steps or linear; offset-shadow press effect (element translates into its shadow). Marquee scroll 30–60s linear infinite. `prefers-reduced-motion`: stop marquee, remove transforms, keep color hovers.

## When to use
Streetwear/fashion drops, music labels, event sites, portfolios, indie tools, studios, zines. Audience expects attitude; brand is confident enough to look unfinished on purpose.

## When NOT to use
Fintech, health, government, enterprise, healthcare data, anything with dense reading or trust-sensitive conversions — broken composition reads as careless where users expect order. Also skip if the client wants "clean SaaS".

## Do
- Plan the grid, then break exactly 2–3 places per screen
- Overlap with a z-index ladder, not random z-indexes
- Hard offset shadows in the text color only
- One acid accent for CTAs and stickers
- Index/number your sections in mono ("01", "02")
- Keep body text in a tidy column — chaos needs an anchor
- Oversized type that crosses its column edge

## Don't
- Rotate everything ("chaos mode")
- Soft shadows, rounded corners, pastels — wrong universe
- Center the layout
- Gradients or glow
- Break the grid on form fields and body copy (usability lives here)
- More than one rotated element per viewport section

## Anti AI-slop (brutalist edition)
Random `rotate(-7deg)` on every card, blurred neon glows, mixed pastel blobs, "glitch" effects with no cause, Comic-Sans-irony — slop here = chaos without choreography. If you remove the grid underneath, the layout collapses: it wasn't brutalist, it was broken.

## Good vs Bad examples
- **Good:** Gumroad's 2023+ rebrand — heavy borders, hard shadows, acid pink accent, oversized type, controlled overlaps.
- **Bad:** "brutalist" page where every card is rotated a different direction, centered text, pastel shadows with blur — it's birthday-party chaos, not anti-grid.