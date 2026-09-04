# 14 3D Spatial UI — ready prompts

## Codex
```
Build a single-file HTML landing page for "Depthline" (a 3D asset-review
tool for game studios). Style: spatial/3D UI using ONLY vanilla CSS 3D
transforms (perspective, transform-style: preserve-3d, translateZ,
rotateY) — no Three.js, no WebGL, no libraries. One perspective per
section (perspective: 1200px on the section). Hero: a flat readable
product-UI plane straight-on, a supporting panel behind it rotated
rotateY(-14deg) translateZ(-120px), an ambient glow layer at
translateZ(-300px); slow cursor-parallax ±10px on the hero layers only.
Layers get mono micro-labels ("LAYER 02 · Z:-120PX", Space Mono 11px,
+0.12em uppercase). Fonts: Space Grotesk 700 for H1 (letter-spacing
-0.02em), Inter 17px/1.6 body, Space Mono labels. Palette: dark bg
#060608, planes #101014 with border #1F1F26, ONE accent #8B8BF5 for
CTA + layer edges, large soft shadows (0 24px 60px -20px rgb(0 0 0
/ .7)). 2–4 depth layers per section, max; keep pricing and footer
completely FLAT. Sections: spatial hero, layered feature cards that
fan out (adjacent cards rotateY ∓6deg on hover), flat 3-plan pricing,
CTA band. Hover lift: translateZ(8px) + stronger shadow, 350ms
cubic-bezier(.16,1,.3,1). Mobile (<900px): remove all rotateY and
parallax, keep soft-shadow layering. Include prefers-reduced-motion
that flattens all transforms to static layered shadows.
```

## Claude
```
Design a spatial 3D landing page for Depthline, a 3D asset-review tool.
Decide the depth logic first: every layer must answer "why is THIS in
front/behind?" — interactive content in front (translateZ 60–80px),
context behind (translateZ -120px to -300px), max 4 layers per section,
one perspective: 1200px per section. Use only vanilla CSS 3D transforms
and a small vanilla JS rAF loop for hero cursor-parallax (lerped, ±10px,
disabled on touch and reduced-motion). Space Grotesk + Inter + Space
Mono; dark palette (#060608 / #101014) with a single indigo accent
(#8B8BF5). Depth cues: real Z-position, large soft shadows, slight
desaturation/blur on far layers. Pricing and nav stay flat. Deliver one
self-contained HTML file with prefers-color-scheme support and a
complete prefers-reduced-motion fallback where the scene collapses to
flat, shadow-separated layers — that fallback must look good on its
own. No floating stock 3D blobs, no scroll-jacking, no WebGL.
```

## Lovable
```
Create a 3D spatial landing page for "Depthline" (3D asset review for
game studios). Use CSS 3D only: perspective 1200px on sections,
preserve-3d, translateZ layering (near +80px / mid 0 / far -160px),
max 4 layers per section. Dark theme: bg #060608, cards #101014,
borders #1F1F26, one accent #8B8BF5, big soft shadows. Fonts: Space
Grotesk headings, Inter body, Space Mono 11px uppercase layer labels
like "LAYER 02". Hero = straight-on product UI with a tilted panel
behind; features = cards that fan out slightly on hover; pricing and
footer flat. On hover cards lift translateZ(8px). Under 900px wide:
no rotation, no parallax, just shadow layering. Add a
prefers-reduced-motion block that disables all transforms and
parallax.
```

## v0
```
Landing page, style: spatial 3D UI (vanilla CSS transforms, no
three.js). Override shadcn defaults: dark bg #060608, card #101014,
radius 16px, border #1F1F26, accent #8B8BF5 (interactive elements
only). Add a Depth utility set: <div className="scene" style=
{{perspective: 1200}}> with preserve-3d children at translateZ
80/0/-160px; cards lift translateZ(8px) on hover with shadow
0 24px 60px -20px rgba(0,0,0,.7). Hero: flat UI screenshot plane +
one rotateY(-14deg) panel behind + cursor parallax ±10px (rAF,
lerped, off on touch/reduced-motion). Fonts: Space Grotesk / Inter /
Space Mono for uppercase coordinate labels. Keep pricing, nav and
footer flat. Include a reduced-motion variant that flattens all
transforms.
```