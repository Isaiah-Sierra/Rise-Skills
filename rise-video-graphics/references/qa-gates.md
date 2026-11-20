# QA gates

A video is done when it passes all of these. Report any you couldn't run.

## Before render

1. `npx hyperframes lint`: 0 errors.
2. `npx hyperframes check --json`: 0 errors. Read every warning; fix overlaps, text under 28 px,
   text that leaves before it can be read, connector lines that miss their ends, contrast failures.
3. Timeline accounting: the scene durations add up to the root `data-duration`, and every caption
   sits inside its scene.
4. Read every word on screen against the script. No em dashes. Names spelled right.
5. Every factual claim (dates, numbers, names, what a product does) traces to the script or a
   source the person gave.
6. `npx hyperframes snapshot --review`: look at every scene start, middle and cut. Text fits its
   box; nothing clipped; full-bleed type under 88% of frame width; brand colors only.
7. Every organization, event or product named in the script shows its official logo (or is on the list you
   gave the person of logos you couldn't find). Logos are crisp, unstretched, in their own colors,
   on a background their brand allows, with clear space.

## After render

8. `ffprobe` shows h264, `yuv420p`, 1920x1080 (or the asked size), 30 fps, the expected duration,
   `start_time` 0. If there's audio: AAC stereo.
9. The first frame is a keyframe (no blank thumbnail on social players).
10. Pull a frame every 3 to 6 s into a contact sheet and read it:
   `ffmpeg -i out.mp4 -vf "fps=1/4,scale=480:-1,tile=4x5" sheet.png`
11. Never join clips with `-c:v copy` concat; re-encode so the timestamps are clean.

## Handoff note

Say in one line each: what the fonts substitute, which colors were measured rather than printed,
whether there's a voice or music, and what still needs a person's approval before it's shown.
