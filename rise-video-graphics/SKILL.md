---
name: rise-video-graphics
description: Use when Rise Church staff want a branded video made or edited with motion graphics, such as an explainer, an announcement, a sermon or series bumper, a lower third, an event promo, kinetic text, a logo sting or captions over footage. Builds HTML and GSAP compositions in the Rise Church look and renders them to MP4 with the open-source HyperFrames engine on this machine, with no HeyGen account, connector or credits. Triggers include "Rise video", "make a video", "motion graphics", "explainer", "bumper", "lower third", "animate this", "render an MP4".
---

# Rise video graphics

Makes Rise Church videos as code: one HTML page per film, animated with GSAP, rendered frame by
frame to MP4 by the open-source HyperFrames CLI (Apache-2.0, `heygen-com/hyperframes`). Every
render is local and free. Nothing in this skill needs a HeyGen account.

## Hard rules

1. **Local only.** Never run `hyperframes auth login`, `cloud render`, `publish`, `media-use generate`
   or any HeyGen or HyperFrames connector tool (compose, render_video, render_project). Those are
   the paid, hosted paths. Set `HYPERFRAMES_NO_TELEMETRY=1` for every command.
2. **Brand from the guide, never invented.** Every color, font, logo use and phrase comes from
   `references/brand-card.md`. If a value you need isn't there, ask the person; don't make one up.
3. **Facts from a source.** Any claim on screen (a date, a number, a name, a feature) comes from
   the person's script or a source they gave. Placeholder shapes stand in for names you don't have.
4. **No em dashes on screen.** Use periods or commas. Typographic apostrophes (’).
5. **Other names get their real logos.** Whenever the video names another organization, event or
   product (another church, a conference, a ministry partner, a sponsor, Gmail, Planning Center),
   try to source its official logo and place it where the story puts that name
   (`references/logos.md`). Check `assets/logo/third-party/` first, then anything the person gave
   you, then the organization's own site or press kit, then the open CC0 logo sets
   (`scripts/get_logo.py`). Use it in its own colors, never redrawn, recolored, stretched or
   AI-generated, and record it in `SOURCES.md`. If you can't find it, tell the person and set the
   name as plain text in the Rise fonts until they send the file.
6. **The person approves before anything is shared.** Save the MP4 for them; never post or send it.

## Setup (once per machine)

```bash
export HYPERFRAMES_NO_TELEMETRY=1
npm install hyperframes            # or use: npx hyperframes@<pinned version>
npx hyperframes browser ensure     # downloads headless Chrome for rendering
npx hyperframes doctor --json      # confirms Chrome and FFmpeg are ready
```

Needs Node 20+ and FFmpeg. In Claude.ai this runs in the code-execution sandbox.

## Work loop

1. **Brief.** Get the script (or write it with the person), the length, the format (16:9 1920x1080
   by default, 9:16 1080x1920 for reels) and where it will play (lobby screen, Sunday service,
   social, staff email). Ask about voiceover: a staff recording, or silent with captions.
   **Logos:** list every organization, event and product the script names and source each
   official logo now (`references/logos.md`). Tell the person which ones you couldn't find.
2. **Plan scenes.** One scene per idea, 6 to 13 seconds each. Write a table: scene, seconds, the
   words on screen, the one visual, the one motion moment. Keep text to 1 or 2 lines per beat.
3. **Taste gate** (before code). Pick the treatment: *utilitarian* (staff and how-to videos, clean,
   lots of white) or *editorial* (series art, promos, bolder type and color). Name three generic
   defaults you are refusing (for example "centered title on a gradient", "icons in circles",
   "everything fades in"). Choose one signature moment per film.
4. **Build.** `npx hyperframes init <dir> --skip-skills`, copy `assets/fonts` and `assets/logo` into
   the project's `assets/`, then start from `examples/alise-explainer/index.html` or write fresh
   using the patterns in `references/hyperframes-local.md`.
5. **Check.** `npx hyperframes lint`, then `npx hyperframes check --json > check.json` and fix
   every error and weigh every warning (`references/qa-gates.md`).
6. **Look.** `npx hyperframes snapshot --review -o snaps` and read the contact sheets: every scene
   start and middle, every cut. Fix overlaps, clipped text and anything that reads off-brand.
   Every named organization shows its logo where its name is said, crisp and in its own colors.
7. **Render.** `npx hyperframes render --quality delivery -w <cores> -o out.mp4`. Then run the
   file checks in `references/qa-gates.md` (ffprobe, frame-0 keyframe, contact sheet every 3 to 6 s).
8. **Deliver.** Save the MP4 and the project folder for the person, with a one-line note on what
   is a substitute (fonts) and what still needs them (voice, music, approvals).

## Rise look in one screen

- Ground: white `#FFFFFF`, with the Rise weighted circle (logomark ring) large and faint in light
  gray `#E7E4EA` as a slow-drifting background element.
- Ink: navy `#26334A` for headlines, charcoal `#3C4247` for body and captions.
- Accent: Rise red `#EC0044`, sparingly: eyebrow labels, step numerals, one underline, the yes.
- Support: teal `#12AEAB` for small status dots and outlines only; mint `#CFE3D8` for soft fills.
- Type: titles in a slab (Nexa Slab in print, **Roboto Slab** here), labels and wordmarks in a
  geometric sans (Gotham in print, **Montserrat** here), body and captions in **Source Sans 3**
  (for Proxima Nova). All three ship in `assets/fonts` with their licenses.
- Small all-caps eyebrow labels with wide tracking above titles. Large numerals for steps.
- Generous white space; nothing important outside the 80% title-safe box.
- End card: the stacked Rise logo in navy, one line, then `risechurchtx.com`.

Full rules, with where each value came from, are in `references/brand-card.md`.

## Motion in one screen

- Write time in frames: `const F = 1/30;` and durations as `n * F`.
- Nothing moves at frame 0; first entrance at 0.1 to 0.3 s. Something readable is on screen at
  frame 0 anyway (it's the thumbnail).
- Entrances ease out, exits ease in, and an exit is no longer than 0.8 of its entrance.
- At least six different eases per film, none used for more than 30% of tweens.
- Scale entrances start at 0.90 to 0.97, never 0. Overshoot (`back.out(1.7)`) on 15 to 40% of
  entrances; the rest settle.
- Vary entrance directions; opacity-only on no more than a quarter of entrances.
- Offset related elements 2 to 4 frames; a parent's children follow 3 frames behind.
- A visual change every 2 to 3 s; no static full frame longer than 2 s.
- One ambient motion per scene (the drifting ring counts), one motivated event in the middle of
  any scene of 8 s or more (a pulse, a highlight, a press).
- Text holds at least 0.5 s plus 0.3 s per word before it changes.

Details and the full list of tells to avoid: `references/motion-rules.md`. Cuts, pacing and
transitions: `references/edit-grammar.md`.

## Files

- `references/brand-card.md`: Rise palette, type, logo rules, copy and voice, with sources.
- `references/hyperframes-local.md`: the composition format, local commands, and the lint traps.
- `references/motion-rules.md`: easing, timing and the motion tells that make video look generated.
- `references/edit-grammar.md`: pacing, text-as-percussion, safe zones and transitions.
- `references/qa-gates.md`: the checks to pass before calling a video done.
- `assets/fonts/`: Montserrat, Roboto Slab, Source Sans 3 (woff2) and their licenses.
- `assets/logo/`: official Rise logomark and stacked logo, traced from the brand guide PDF
  (`fill="currentColor"`, so color them with CSS `color:`).
- `references/logos.md`: how to find, check, record and place the logo of anyone a video names.
- `scripts/get_logo.py`: exports an official mark, unaltered, from the CC0 logo libraries.
- `assets/logo/third-party/`: official logos of tools Rise videos often name (Claude, Anthropic,
  Planning Center, Gmail, Google Drive, Calendar and Meet, Slack, Zoom, YouTube, Instagram,
  Facebook, Notion, Asana, Teams, Loom, Zapier), with where each came from in `SOURCES.md`.
- `examples/staff-claude-duet/`: a 4:20 staff explainer over a recorded voice, with outside logos
  placed where they're named.
- `examples/alise-explainer/`: a finished 70 s staff explainer built with this skill over an
  existing voiceover, with the Python script that generates it.
