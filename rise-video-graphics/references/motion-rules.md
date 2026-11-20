# Motion rules

Generated video gives itself away through motion more than through layout. Run this list against
every film before rendering. Each line is a measurable test.

## Timing

1. No linear velocity on anything that enters or exits. Linear is for the ambient drift only if at all.
2. At least 6 distinct eases in a film; no single ease on more than 30% of tweens.
3. The slowest entrance is at least 3 times the fastest (for example 8 frames vs 24 frames).
4. Entrances use `.out` eases; exits use `.in` eases; moves between two positions use `.inOut`.
5. An exit lasts no more than 0.8 of its own entrance.
6. Related elements are offset by at least 2 frames. Children follow their parent by 2 to 4 frames.
7. Nothing moves at frame 0. The first entrance starts at 0.1 to 0.3 s.

## Shape of entrances

8. Scale entrances start between 0.90 and 0.97. Never from 0.
9. No single entrance direction on more than 55% of entrances (mix up, left, right, scale, wipe).
10. Opacity-only entrances on no more than 25% of entrances.
11. 15 to 40% of entrances overshoot (`back.out(1.7)` peaks about 10% past; `back.out(2.6)` about 20%,
    for small things like chips and ticks only).

## Life in a scene

12. One ambient motion per scene (slow drift, slow scale). Never a looping wiggle.
13. Any scene of 8 s or more has one motivated event between 30% and 70% of its length: a pulse,
    a highlight sweep, a button press, a sort. It should mean something in the script.
14. Hold frames: let a finished layout sit still for at least half a second before it changes.
15. Every entrance can be justified in one sentence ("the reply slides in from the right because
    it answers the bubble on the left"). If you can't, cut it.

## Banned

- Bounce, shake, spin and wobble presets.
- Typewriter text for anything longer than a few words.
- Every element fading in the same way at the same speed.
- Elements flying in from off-screen across the whole frame.
- Rotating the Rise logo or logomark.

## Frame math

- `const F = 1 / 30;` then write every duration as `n * F`.
- Quick UI pop: 8 to 12 F. Card or panel: 16 to 20 F. Hero title: 18 to 24 F. Logo: 24 F.
- Stagger: 2 to 4 F between siblings; 4 to 6 F between groups.
- Reading time: hold text for 0.5 s plus 0.3 s per word, at least 1.5 s.
