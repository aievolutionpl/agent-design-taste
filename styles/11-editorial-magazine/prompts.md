# 11 Editorial Magazine — ready prompts

## Codex
```
Build a single-file HTML landing page for "Fieldnotes" (a slow-travel
journal and print subscription). Style: editorial magazine. Fonts: Fraunces
500–600 for H1/H2 (56px, high optical size feel), Source Serif 4 for body
18px/1.7 (measure 60–65ch), Inter for 12px uppercase kickers (+0.14em) and
13px captions. Palette: warm paper #FDFBF7 bg, #1A1815 ink text, #E3DCD0
hairlines, ONE deep red #8C2F1A accent. Layout: magazine-cover hero (kicker
→ oversized serif headline over a large photo → serif italic deck → sans
byline), asymmetric 7/5 feature sections, drop cap on the opening
paragraph (::first-letter, 3-line float), a wide pull quote in Fraunces
italic 32px breaking the column, image pairs with photographer credits,
editorial footer with colophon. Flush-left long-form text, never centered.
Hairline rules as section dividers. No gradients, no glass, no neon, no
rounded blobs, no fake testimonials. Hover: 150ms color shift or image
scale 1.02. Include prefers-reduced-motion reset.
```

## Claude
```
Design an editorial-magazine landing page for Fieldnotes, a slow-travel
journal. Decide the cover first: kicker, huge Fraunces headline, italic
serif deck, byline. Then long-form sections — 18px/1.7 Source Serif 4 body
with a 3-line drop cap opening each article block, asymmetric 7/5 splits,
one wide italic pull quote per screen. Warm paper bg (#FDFBF7), ink text,
hairline rules (#E3DCD0), one deep red #8C2F1A used like an ink stamp on
the CTA and accents. Inter only for kickers, captions and UI. Deliver as
one self-contained HTML file with dark mode via prefers-color-scheme and a
reduced-motion reset. No gradients, no glass, no centered body copy, no
invented statistics.
```

## Lovable
```
Create an editorial-magazine landing page for "Fieldnotes" (slow-travel
journal + print subscription). Strict rules: warm paper bg #FDFBF7, ink
text #1A1815, 1px hairlines #E3DCD0, one deep red accent #8C2F1B, no
gradients, no glassmorphism. Fonts: Fraunces headings + Source Serif 4
body (18px/1.7, drop cap on opening paragraphs) + Inter for uppercase
kickers and captions. Sections: cover-style hero with photo, 7/5
asymmetric features, wide italic pull quote, subscription plans as an
editorial table with hairline rows, colophon footer. Flush-left text,
never centered. No purple, no neon, no fake stats.
```

## v0
```
Landing page, style: editorial magazine. Override shadcn defaults: radius
0–4px, shadows OFF (use 1px hairlines #E3DCD0 on warm paper #FDFBF7),
primary = #1A1815, accent = #8C2F1A on CTA only. Font: Fraunces headings /
Source Serif 4 body 18px/1.7 with ::first-letter drop caps / Inter for
uppercase kickers + captions. Asymmetric 7/5 feature splits, one wide
italic Fraunces pull quote spanning 8 cols, hairline-row pricing table,
editorial colophon footer. Flush-left long-form text. No gradient meshes,
no glass cards, no emoji icons — photography carries the visuals. Never
center paragraphs.
```