# 07 Neumorphism — ready prompts

## Codex
```
Build a single-file HTML landing page for "HavenPod" (smart-home companion
app). Style: neumorphism — surfaces share the background hue (#ECF0F3), depth
comes ONLY from matched shadow pairs: raised = 6px 6px 12px #C8D0E0 +
-6px -6px 12px #FFF; inset (pressed states, input wells) = inset 4px 4px 8px
#C8D0E0 + inset -4px -4px 8px #FFF. Radius 12–24px, no borders, no hard
shadows. Fonts: Manrope 800 H1/H2, Nunito Sans body 16px/1.65. Text colors
must keep 4.5:1 contrast (#111827 / #4B5563 on light). ONE accent #4F6AF0 —
the filled CTA and the active toggle are the only high-contrast controls.
a11y rules (mandatory): visible 3px accent focus ring on :focus-visible, a
1px fallback border on hover for icon buttons, no shadow-only interactivity.
Hero: extruded device widget with inset stats wells. Sections: card trio,
inset thermostat demo, pricing with raised cards. Include dark theme
(prefers-color-scheme: #23272E bg, shadows #14161B/#3B424D) and a
prefers-reduced-motion reset. No gradients behind panels, no sharp corners.
```

## Claude
```
Design a soft neumorphic landing page for HavenPod, a smart-home companion.
The core mechanic: UI surfaces extruded from one background color via dual
soft shadows (light top-left, dark bottom-right); pressed = inset. Manrope +
Nunito Sans, near-monochrome palette with a single #4F6AF0 accent on the
primary CTA. IMPORTANT: neumorphism has a built-in accessibility problem —
surface≈background means component boundaries can fail WCAG 1.4.11 (3:1).
Compensate: all interactive elements get a visible focus ring and a contrast
fallback (border or filled state), body text ≥ 4.5:1, and the design must
survive losing its shadows entirely. Sections: hero with extruded widget,
3 feature cards, inset control demo, simple pricing. One self-contained
HTML file, dark mode via prefers-color-scheme, reduced-motion reset. Do not
use it for anything resembling banking or dense data — keep it ambient.
```

## Lovable
```
Create a neumorphic landing page for "HavenPod" (smart-home app). Rules:
background #ECF0F3, surfaces SAME color, depth only via shadow pairs —
raised: 6px 6px 12px #C8D0E0 / -6px -6px 12px #FFF; inset: inset 4px 4px 8px
#C8D0E0 / inset -4px -4px 8px #FFF. Radius 12–24px, no borders, no hard
shadows, no gradients. Fonts: Manrope (headings) + Nunito Sans (body 16px).
Text #111827 and #4B5563 only (keep 4.5:1 contrast). One accent #4F6AF0 for
the main CTA and active states. Buttons press INTO the surface (raised →
inset) on click. a11y: visible focus rings, don't rely on shadows alone to
mark buttons. Sections: hero widget, 3 cards, control demo, pricing.
```

## v0
```
Landing page, style: neumorphism / Soft UI. Override shadcn defaults:
radius 18px+, background = surface = #ECF0F3, replace shadows with dual soft
pairs (6px 6px 12px #C8D0E0, -6px -6px 12px #FFF; inset variant for pressed
and inputs), borders OFF except a 1px #C8D0E0 hover fallback on icon
buttons. Primary button = filled #4F6AF0 (the only high-contrast control),
dark text #111827, secondary #4B5563. Font: Manrope headings / Nunito Sans
body 16px/1.65. Hero with extruded device widget + inset stat wells, 3
raised feature cards, inset thermostat demo, pricing. Dark theme: bg
#23272E, shadows #14161B / #3B424D. Focus rings must be visible 3px accent
— never shadow-only. No gradients, no sharp corners, no extra accent colors.
```