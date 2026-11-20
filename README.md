# Rise Skills

Claude skills built for Rise Church staff.

## rise-video-graphics

Makes branded Rise Church videos (explainers, announcements, bumpers, lower thirds, captions over
a voiceover) as HTML and GSAP, and renders them to MP4 on your own machine with the free,
open-source HyperFrames engine. No HeyGen account or credits needed.

What it does:

- Uses the Rise brand guide's colors, fonts and logo, and the motion rules in its references.
- Finds the official logo of any app, church, event or partner a video names and places it where
  the narration mentions that name.
- Checks every video against QA gates before it's handed over, and never shares anything without
  your approval.

### Add it to Claude

- **Claude.ai or the desktop app:** add a skill from Claude's settings and upload
  `rise-video-graphics.zip` from this repo.
- **Claude Code:** copy the `rise-video-graphics/` folder into `~/.claude/skills/`.

Then ask Claude for "a Rise video" or "motion graphics in the Rise look".

`rise-video-graphics/` is the source. `rise-video-graphics.zip` is the same skill, packaged for upload.
