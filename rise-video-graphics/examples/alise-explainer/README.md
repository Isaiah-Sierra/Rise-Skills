# Alise explainer (example)

A 70-second, 1920x1080 staff explainer made with this skill: eight scenes, captions and the Rise
look laid over an existing voiceover, rendered locally with HyperFrames in about a minute on 4 cores.

`assets/voice.m4a` is not included. It was pulled from the person's own earlier recording
(see "Putting graphics over a voice you already have" in `references/edit-grammar.md`). Without it,
delete the `<audio id="voice">` line and the film renders silent with captions.

To rebuild it:

1. `npx hyperframes init alise --skip-skills`
2. Copy `../../assets/fonts` to `alise/assets/fonts`, the two Rise SVGs in `../../assets/logo` to `alise/assets/logo`, and `../../assets/logo/third-party/claude-mark.svg` to `alise/assets/logo/claude-mark.svg`.
3. Put the voiceover at `alise/assets/voice.m4a`.
4. `python3 gen_alise.py alise` (writes `alise/index.html`), or copy `index.html` in directly.
5. `cd alise && HYPERFRAMES_NO_TELEMETRY=1 npx hyperframes render --quality delivery -w 4 -o alise.mp4`

The scene list, captions and timings live at the top of `gen_alise.py`; edit them there. The `A` table in its script maps each beat from the original 77 s silent cut onto the voice.
