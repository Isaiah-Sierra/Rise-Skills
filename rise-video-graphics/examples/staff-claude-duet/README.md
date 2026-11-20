# Staff explainer: Claude and Duet (4:20)

Rebuilt over Danny's existing voiceover, Nov 2026. Shows the logo step: Anthropic's wordmark,
and Gmail, Google Drive, Google Calendar and Planning Center logos placed where the voice names
them (in a pill row for "tools like Gmail, Drive, or Planning Center", and as equal cards in the
"five apps" grid). Fellow and Ninety stay as plain text because no official file was found.

- `align.py voice.m4a timing.json`: caption times from the voice's pauses (ffmpeg silencedetect).
- `gen_staff.py <project dir> timing.json`: writes `index.html` from `staff.css` and `staff.js`;
  cues like `@c(19, "Gmail")` become the time that word is spoken.
- The project needs `assets/fonts`, `assets/logo` (with `third-party/`) and `assets/voice.m4a`.
