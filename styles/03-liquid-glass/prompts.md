# 03 Liquid Glass — ready prompts

## Codex
```
Build a single-file HTML landing page for "Halo" (a smart-home app).
Style: Apple Liquid Glass — translucent, refractive floating controls
over rich media; glass is for CONTROLS ONLY (nav pill, floating dock,
segmented capsule), never content cards. Background: dark #0B1120 with
three slowly drifting radial glows (#0EA5E9, #8B5CF6, #F472B6, 90s
loop). Liquid glass recipe: rgb(255 255 255 / 0.14) tint,
backdrop-filter blur(14px) saturate(180%) brightness(1.08), inset
specular highlight (inset 0 1px 0 rgb(255 255 255 / .4)), border
rgb(255 255 255 / .22), pill radius, shadow 0 12px 40px rgb(0 0 0/.18).
Fonts: Figtree 700 H1/H2 (-0.015em), Inter body 17px/1.6, Geist Mono
12px uppercase labels. Text white / rgb(255 255 255/.65). Primary CTA
solid iOS blue #0A84FF capsule; secondary = tinted glass capsule.
Sections: full-bleed hero with floating pill nav + glass dock (3 solid
feature cards below), spring-y segmented control, stats row, big CTA,
footer. Springs: cubic-bezier(.34,1.56,.64,1) 350ms; scroll parallax
±8px on floating elements. Guard @supports backdrop-filter with solid
fallback; prefers-reduced-motion freezes drift/parallax → fades only.
No fake iPhone notch, no glass card grids, no translucent primary CTA.
```

## Claude
```
Design a Liquid Glass (Apple 2025) landing page for Halo, a smart-home
app. Understand the material: glass bends light from the moving media
beneath it — so give every glass element a top specular highlight and
springy, physical motion. Glass is for floating controls (nav pill,
action dock, segmented control); feature content sits on solid rounded
surfaces over the rich background. Dark scene with drifting color
glows, Figtree/Inter/Geist Mono, one iOS-blue accent, solid primary
CTA. Every interaction uses spring easing with slight overshoot; press
feedback scales to 0.97. Deliver one self-contained HTML file,
responsive, with solid fallbacks where backdrop-filter is unsupported
and a full prefers-reduced-motion path. Do not clone iOS chrome (no
fake notch/status bar) and do not put long-form text on glass.
```

## Lovable
```
Create a landing page for "Halo" (smart-home app) in Apple Liquid Glass
style. Rules: dark #0B1120 background with three drifting colored glows;
glass elements ONLY for floating controls — centered pill navbar, a
glass dock with 4 icon buttons, one segmented control capsule. Recipe:
rgba(255,255,255,0.14) + backdrop-blur 14px + saturate 180% + inset top
highlight rgba(255,255,255,0.4) + border rgba(255,255,255,0.22) + pill
radius. Feature cards SOLID #141C2F, radius 24px. Fonts Figtree
(headings) + Inter (body 17px/1.6). CTA solid #0A84FF, never glass.
All motion springy cubic-bezier(0.34,1.56,0.64,1); hover lifts shadow;
press scales 0.97. Sections: hero + dock, 3 features, stats, CTA band.
No glass text panels, no iPhone clone chrome, no glass card grids.
Mobile: dock becomes bottom bar; reduced-motion = fades only.
```

## v0
```
Landing page, style: Apple Liquid Glass (consumer, tactile). Override
shadcn defaults: dark bg #0B1120 with 3 slowly drifting radial glows
(#0EA5E9/#8B5CF6/#F472B6). Floating pill navbar + glass dock (backdrop-
blur-2xl saturate-[1.8], bg-white/[0.14], ring-1 ring-white/[0.22],
shadow-[inset_0_1px_0_rgba(255,255,255,0.4),0_12px_40px_rgba(0,0,0,0.18)],
rounded-full). Content cards stay SOLID (#141C2F, rounded-3xl). Primary
button solid #0A84FF rounded-full; secondary = tinted glass capsule.
Fonts: Figtree headings / Inter body. Feature grid, stats row, big CTA.
Motion: springs (overshoot ~1.56) on all controls, press scale-[0.97],
subtle scroll parallax on floating elements, everything disabled under
prefers-reduced-motion. Max 3 floating glass elements per view. No
translucent buttons, no glass inputs, no fake iOS status bar.
```