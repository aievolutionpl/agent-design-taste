# Rendered Verification — never trust code alone

A design fault is visible in a screenshot in one second and invisible in code
review for an hour. Code inspection is NOT visual verification.

## Mandatory checks before claiming "done"

1. **Real render** — load the page in a real browser (Playwright, Chrome
   DevTools MCP, or headless screenshot). Look at it.
2. **390px first** — most traffic is mobile; most layout faults surface there.
   A design that only holds at 1440 has not been designed.
3. **States** — check loading, empty, error, and extreme content (very long
   German compound word, 20-item list, empty table).
4. **Keyboard** — tab through: every interactive element visible focus, logical
   order, no traps.
5. **Motion sanity** — with `prefers-reduced-motion: reduce` emulated, the page
   must be fully usable.

## The two-prompt A/B test (did taste move?)

Run the same brief twice: once bare, once with the style DNA + tokens.
Diff the results:
- Changed hex values and radii only → the surface moved (weak).
- Changed structure and hierarchy → something that matters moved (strong).
- Indistinguishable at a glance → the taste layer did not land; fix before shipping.

## Score-inflation warning

If you iterate on the DESIGN-TASTE-SCORE number, past ~85 you may be optimizing
the metric, not the page ("writing for the detector"). Use the score to FIND
faults. The decision to ship is made **after looking at the screenshot**.
