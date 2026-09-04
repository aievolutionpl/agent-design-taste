# 01 Minimalism — ready prompts

## Codex
```
Build a single-file HTML landing page for "Ledgerly" (bookkeeping SaaS for
freelancers). Style: strict minimalism — flat surfaces, hairline borders,
no shadows, no gradients. Fonts: Archivo 600 for H1/H2 (letter-spacing
-0.02em), Inter for body 17px/1.6, IBM Plex Mono for 12px uppercase
eyebrow labels (+0.1em). Palette: white bg, #111 text, #E5E5E2 borders,
ONE accent #2563EB for links/CTA only. Layout: 12-col grid, 1200px
container, split hero (text left, product screenshot right), alternating
feature sections, plain 3-plan pricing separated by whitespace, final CTA
band, minimal footer. Left-align body text. No glassmorphism, no gradient
blobs, no floating cards, no fake statistics or testimonials. Hover:
150ms ease-out border/opacity only. Include prefers-reduced-motion reset.
```

## Claude
```
Design a minimal, typography-led landing page for Ledgerly, a bookkeeping
tool for freelancers. Decide hierarchy first: H1 → primary CTA → screenshot
→ proof. Use Archivo + Inter + IBM Plex Mono, a single blue accent
(#2563EB), hairline borders instead of shadows, 96px+ section spacing.
Every element must justify its existence; if a section doesn't add trust
or clarity, remove it. Deliver as one self-contained HTML file with dark
mode via prefers-color-scheme and a reduced-motion reset. Do not add
gradients, glass, illustrations, or invented numbers.
```

## Lovable
```
Create a minimalist landing page for "Ledgerly" (freelancer bookkeeping
SaaS). Strict rules: flat design, 1px borders (#E5E5E2), no shadows, no
gradients, one accent color (#2563EB), fonts Archivo (headings) + Inter
(body). Sections: split hero, 2 alternating features, pricing (3 plans,
whitespace-separated), CTA band. Left-aligned text, generous 96px section
spacing. No glassmorphism, no purple, no fake stats.
```

## v0
```
Landing page, style: Swiss-minimal. Override shadcn defaults: radius 8px
max, shadows OFF (use 1px borders #E5E5E2), primary = #111, accent =
#2563EB used only on interactive elements. Font: Archivo headings / Inter
body. Split hero + alternating features + pricing table + CTA band.
No gradient meshes, no glass cards, no emoji icons — use Lucide outline
icons at 1.5px stroke, single family. Body 17px/1.6, left-aligned.
```
