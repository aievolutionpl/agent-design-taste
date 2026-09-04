# Motion Foundations

Motion communicates hierarchy and causality — never decoration for its own sake.

## Token system (use in every style, values vary per DNA)

```css
:root {
  --motion-duration-instant: 100ms;  /* presses, toggles */
  --motion-duration-fast: 150ms;     /* hover states */
  --motion-duration-normal: 250ms;   /* cards, panels */
  --motion-duration-slow: 400ms;     /* sections, modals */
  --motion-duration-page: 600ms;     /* hero reveals, max */
  --motion-ease-out: cubic-bezier(0.16, 1, 0.3, 1);
  --motion-ease-in-out: cubic-bezier(0.65, 0, 0.35, 1);
  --motion-ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1); /* only playful styles */
}
```

## Interaction budgets

| Interaction | Duration | Easing | Notes |
|---|---|---|---|
| Button hover | 150ms | ease-out | color/transform only, never layout |
| Button press | 100ms | ease-out | scale 0.97-0.98 |
| Card hover | 200-250ms | ease-out | lift ≤ 8px, shadow deepen |
| Modal in/out | 300-400ms | ease-in-out | fade+scale 0.96→1, backdrop separate |
| Nav drawer | 300ms | ease-out | slide ≤ 40% viewport width |
| Scroll reveal | 400-600ms | ease-out | once, threshold 20%, translateY ≤ 24px |
| Hero entrance | ≤ 600ms | ease-out | stagger 60-90ms per element |
| Tab switch | 200ms | ease-out | content crossfade only |

## Hard rules

1. **prefers-reduced-motion: every animated page handles it:**

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

2. Animate only `transform` and `opacity` (compositor-friendly). Animating
   width/height/top/left = jank.
3. Entrance animations run ONCE. Nothing re-animates on every scroll.
4. Stagger ≤ 6 elements; more feels like a screensaver.
5. Motion personality must match style DNA (Brutalist: snappy/no easing tricks;
   Claymorphism: spring; Swiss: near-none; Kinetic: it IS the point).

## Slop signals

- Everything floats/pulses infinitely.
- 900ms hover transitions (feels laggy, not premium).
- Parallax on dense content.
- Scroll-jacking (hijacking wheel to drive a "story").