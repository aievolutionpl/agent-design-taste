# Rendered Verification — code review is not visual review

A design fault is visible in a screenshot in one second and invisible in code
review for an hour. Reading your own CSS and concluding "this looks good" is
not verification. It is a guess with extra steps.

**Rule: you may not claim a design works until you have looked at it rendered.**

---

## When you have browser or screenshot capability

Playwright, Puppeteer, Chrome DevTools MCP, a headless screenshot tool, or a
preview URL you can fetch and view — any of these counts. The protocol:

```
1. RUN        start the project (dev server, static file, preview deploy)
2. RENDER     load the real page — not a fragment, not a component in isolation
3. DESKTOP    1440 × 900   — composition, hierarchy, rhythm
4. TABLET     768 × 1024   — where two-column layouts have to decide
5. MOBILE     390 × 844    — the canonical check; look here first if time is short
6. COMPARE    against the chosen style DNA: does this read as that style?
7. FIX        the two weakest visual areas — by weighted loss, not by ease
8. RENDER     again. A fix you did not re-render is a fix you did not verify
```

Steps 7–8 are one loop, not one pass. Exit when the render survives the
Design Taste Score thresholds — not when you are tired of looking.

This repository ships the loop as a script:

```bash
node scripts/screenshot.mjs http://localhost:3000   # a running dev server
node scripts/screenshot.mjs ./dist/index.html       # a built file
node scripts/screenshot.mjs 10                      # one style's example page
```

It renders all four canonical viewports, writes PNGs to `screenshots/`
(gitignored), and **fails with a non-zero exit code on horizontal overflow at a
mobile viewport** — the one blocker that is reliably machine-detectable. It also
reports touch targets under 44px.

The script is a floor, not a pass. It cannot see hierarchy, rhythm, or whether
the page looks like every other AI landing page. **Open the PNGs.**

### What to look for that code never shows you

- **Optical spacing.** Equal margins around unequal shapes look unequal.
- **Type collision.** A 64px display heading with default tracking collides.
- **Real content overflow.** A German compound noun, a 40-character surname,
  a 20-item list, an empty table.
- **The grey stack.** Three "different" greys that render identically.
- **Actual contrast.** Text over an image, over a gradient, over glass.
- **The scan path.** Where does the eye go first? Is that where you meant?

### Also check, at each viewport

- **States**: loading, empty, error, and extreme content.
- **Keyboard**: tab through everything — visible focus, logical order, no traps.
- **Reduced motion**: emulate `prefers-reduced-motion: reduce`; the page must be
  fully usable, not merely still.
- **Zoom**: 200% browser zoom without loss of content or function.

---

## When you have no rendering capability

Say so. Explicitly, in the delivery message. Then do the strongest available
substitute — and never upgrade the language beyond what you actually did.

| ✅ Honest | ❌ Not allowed |
|---|---|
| "I could not render this. Verified by code inspection only: token usage, breakpoint rules, focus styles, reduced-motion block. **Please check the 390px render before shipping.**" | "Looks great on all screen sizes!" |
| "Contrast computed from token values: `#555` on `#FFF` = 7.4:1 — passes. Not visually confirmed." | "Fully accessible and responsive." |

Substitutes worth doing without a browser:

1. Compute contrast ratios arithmetically from the token hex values.
2. Trace every breakpoint rule and state what the layout becomes at 390.
3. Grep for hard-coded values that bypass tokens.
4. Confirm a `prefers-reduced-motion` block exists and covers the animations.

---

## The two-prompt A/B test — did taste actually move?

Run the same brief twice: once bare, once with the style DNA and tokens loaded.
Render both. Diff them.

| Result | Reading |
|---|---|
| Only hex values and radii changed | The surface moved. Weak — the layer barely landed. |
| Structure, hierarchy and layout pattern changed | Something that matters moved. |
| Indistinguishable at a glance | The taste layer did not land. Fix that before shipping. |

---

## Score-inflation warning

If you keep iterating on the Design Taste Score number, past roughly 85 you are
optimizing the metric rather than the page — writing for the detector.

Use the score to find faults. **Make the ship decision after looking at the
screenshot.** If the number says 88 and the render looks wrong, the render wins.
