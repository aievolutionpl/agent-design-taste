# 06 Brutalist Anti-Grid — ready prompts

## Codex
```
Build a single-file HTML landing page for "RIFTZINE" (independent music label
/ drop shop). Style: brutalist anti-grid — a 12-col grid that is DELIBERATELY
broken: cards overlap their neighbors by 20–80px with a z-index ladder, one
element per section rotated −2° to +2.5°, oversized headings overflowing
their column edge. Everything else is raw order: 0 radius, 2–3px solid black
borders, HARD shadows (8px 8px 0 #111, zero blur). Fonts: Archivo Black
uppercase H1/H2 (letter-spacing −0.02em), Space Grotesk body 16px/1.6,
Space Mono 12px uppercase meta labels with index numbers (01, 02, 03).
Palette: paper bg #F4F1EA, #111 text, ONE acid accent #CCFF00 used only for
CTA and stickers. Hero: giant headline, supporting card overlapping from
below-right, rotated badge pinned on top. Sections: broken card cluster for
releases, marquee strip, offset pricing cards, heavy-bordered footer. Hover:
120ms translate(−4px,−4px) + shadow grows. Include prefers-reduced-motion
reset (stop marquee, keep color hovers). No gradients, no pastels, no blur,
no centered text.
```

## Claude
```
Design a brutalist anti-grid landing page for RIFTZINE, an indie music label
selling limited drops. First define the underlying 12-col grid, then break
it on purpose in exactly 2–3 places per screen: intentional overlaps, a
couple of slight rotations, headlines that cross their column. Depth comes
only from hard offset shadows and 2px borders — no blur, no gradients, no
rounded corners. Archivo Black + Space Grotesk + Space Mono, paper-white bg,
single acid accent #CCFF00. Body copy and form fields stay in tidy columns;
the chaos lives in composition, not readability. Deliver one self-contained
HTML file with dark mode via prefers-color-scheme and reduced-motion reset.
Random chaos without the underlying grid is a failure — choreograph it.
```

## Lovable
```
Create a brutalist anti-grid landing page for "RIFTZINE" (indie music label,
limited vinyl/cassette drops). Rules: 0 border-radius everywhere, 2px solid
black borders, hard offset shadows 8px 8px 0 #111 (no blur, no gradients),
fonts Archivo Black (headings, uppercase) + Space Grotesk (body) + Space Mono
(labels). Paper bg #F4F1EA, text #111, one accent #CCFF00 on CTAs only.
Layout: broken 12-col grid — cards overlap by 20–80px, one rotated element
per section, oversized headlines. Sections: hero with overlap, releases card
cluster, marquee ticker, 3 offset pricing cards, heavy footer. No pastels,
no glass, no rounded corners, no centered paragraphs.
```

## v0
```
Landing page, style: neo-brutalist anti-grid. Override shadcn defaults:
radius 0, borders 2px solid #111 (heavy), shadows = hard offset 8px 8px 0
#111 with 0 blur (replace default shadows), primary = #111, accent = #CCFF00
CTA-only. Fonts: Archivo Black headings (uppercase) / Space Grotesk body /
Space Mono labels. Layout: intentional broken grid — overlapping cards with
z-index ladder, one element rotated ±2° per section, headlines overflowing
their column. Sections: hero, release cards, marquee, offset pricing, CTA.
Hover: translate(−4px,−4px) + bigger hard shadow, 120ms. No gradients, no
glass, no Lucide-rounded icons — use sharp/square icons or raw SVG lines.
```