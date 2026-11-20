# HyperFrames, locally

HyperFrames renders an HTML page to video by pausing a GSAP timeline and seeking it frame by
frame in headless Chrome, then encoding the frames with FFmpeg. Same input, same video, every time.

## Commands

```bash
export HYPERFRAMES_NO_TELEMETRY=1
npx hyperframes init my-video --skip-skills      # new project folder
npx hyperframes lint                             # static rules, seconds
npx hyperframes check --json > check.json        # lint + layout, contrast, craft (a few minutes)
npx hyperframes snapshot --review -o snaps       # contact sheets of every scene and cut
npx hyperframes snapshot --at 4.5,12 -o snaps    # exact moments
npx hyperframes render --quality draft -w 4 -o draft.mp4      # fast look
npx hyperframes render --quality delivery -w 4 -o final.mp4   # the one to share
```

`-w` is the number of render workers: use the machine's physical core count. Never use `auth`,
`cloud`, `publish` or `media-use generate`; they need a HeyGen account and spend credits.

## Composition skeleton

```html
<div id="root" data-composition-id="main" data-start="0" data-duration="60"
     data-width="1920" data-height="1080">
  <div id="bg" class="clip" data-start="0" data-duration="60" data-track-index="0">...</div>
  <section id="s1" class="clip" data-start="0" data-duration="9" data-track-index="1">
    <div class="inner" id="s1i">...scene...</div>
  </section>
  <div id="c1" class="clip" data-start="0.3" data-duration="4" data-track-index="2">caption</div>
</div>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>
<script>
  const F = 1 / 30;
  const tl = gsap.timeline({ paused: true });
  // tweens...
  window.__timelines["main"] = tl;
  tl.seek(0);
</script>
```

- A clip shows over `[start, start + duration)`. Land end states before the end.
- The root's `data-duration` is the film's length.
- Fonts: `@font-face { font-family: "Rise Slab"; src: url('assets/fonts/RobotoSlab-latin.woff2'); font-weight: 100 900; }`.
  Asset paths are relative, no leading slash.

## Traps (each one has broken a render)

- **One root composition per project.** Don't leave a second `index.html`-style file with
  `data-composition-id` lying around.
- **Hard-kill every exit.** If a tween fades something out at a scene boundary, add
  `tl.set(sameSelector, { opacity: 0 }, boundary)` with the identical selector.
- **Never tween `display`, `visibility` or `autoAlpha` on a `.clip`.** Animate a child wrapper
  (`.inner`).
- **Never put a CSS `transform` on an element GSAP moves.** Position with `left`/`top`, move with GSAP.
- **No `tl.call()`, timers, `Date.now()`, unseeded random, or DOM changes in script.** Everything
  visible must be a function of timeline time, or seeking breaks.
- **No `repeat: -1`.** Write the ambient motion as one long tween across the scene.
- **Text widths:** add `white-space: nowrap` to labels in fixed-width boxes, then check they fit.
- **Connector lines** must start and end on the shapes they join, or `check` flags them.
- **Frame 0 is the thumbnail.** Have the background and a label already on screen.
- Lint warns that one big file should be split into sub-compositions (`compositions/*.html`).
  That only matters for editing in the HyperFrames desktop app; a single file renders fine.

## Scene recipes

- **Eyebrow wipe:** `tl.fromTo(sel, {clipPath:"inset(0 100% 0 0)"}, {clipPath:"inset(0 0% 0 0)", duration:14*F, ease:"power3.out"}, t)`.
- **Word stagger:** wrap words in `<span class="w" style="display:inline-block">`, then
  `fromTo(".w", {y:46, opacity:0}, {y:0, opacity:1, duration:18*F, ease:"back.out(1.7)", stagger:3*F})`.
- **Underline draw:** a `<i>` bar with `transform-origin:left`, `scaleX` 0 to 1, `expo.out`.
- **Line draw:** SVG path with `strokeDasharray: L, strokeDashoffset: L` tweened to 0.
- **Press:** scale to 0.95 over 4 frames (`power2.in`), back to 1 over 10 (`back.out(2.6)`).
- **Pulse:** scale to 1.07 over 6 frames, back over 12 (`power1.inOut`).
- **Sort:** place cards with `tl.set(card, {x, y, rotation})`, then tween to column positions
  with `power3.inOut`, 3 frames apart.
- **Ambient ring:** `tl.to("#bgring", {scale:1.05, x:-40, y:20, duration: filmLength, ease:"sine.inOut"}, 0.2)`.
