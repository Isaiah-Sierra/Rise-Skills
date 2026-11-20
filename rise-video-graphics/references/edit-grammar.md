# Edit grammar

How the film moves from beat to beat.

## Pacing

- A visual change every 2 to 3 seconds. A full-frame graphic never sits still longer than 2 s.
- Text is percussion: 1 or 2 lines at a time, each held long enough to read once.
- Captions carry the full sentence; the headline carries the idea in 3 to 6 words. When the
  headline is the sentence, drop the caption for that beat.
- Scale-settle on arrivals (1.05 to 1.0) reads as confident; avoid big zooms.

## Transitions

- Hard cut on a beat between related moments.
- Short dissolve (0.3 to 0.5 s) or exit-up then enter between scenes in the same topic.
- Dip to white or to the ground color at a topic boundary.
- No wipes with patterns, no spins, no glitch, no whip pans unless the piece is a high-energy
  youth promo and the person asks.

## Safe zones (1920x1080)

- Action-safe: inside 96 to 1824 px wide, 54 to 1026 px tall. Nothing important outside it.
- Title-safe: inside 192 to 1728 px wide, 108 to 972 px tall. All reading text inside it.
- Captions sit in the bottom band (about 878 to 982 px), centered, max two lines.
- Keep the top strip clear on social formats; platforms put UI there.
- 9:16 reels: the same ratios on 1080x1920, captions above the bottom 20%.

## Sound

- A film over 15 s that tells something should have a voice, music, or both. Options, in order:
  a staff member records the script (phone voice memo is fine, then clean it), or a licensed
  music bed the church already owns. Don't use AI voices or stock music without the person's OK.
- If it ships silent, captions must carry every word.

## Putting graphics over a voice you already have

When a voiceover exists (a staff recording, or the audio of an earlier render):

1. Pull the audio without re-encoding the voice twice:
   `ffmpeg -i source.mp4 -vn -ac 2 -ar 48000 -c:a aac -b:a 192k assets/voice.m4a`
2. Find where each line starts: `ffmpeg -i assets/voice.m4a -af silencedetect=n=-35dB:d=0.35 -f null -`
   gives the pauses; match them to the script's sentences.
3. Set each scene's `data-start` and `data-duration` to its lines, and each caption to its sentence.
   Land each scene's key visual on the word it illustrates, 2 to 4 frames early.
4. Add the voice as its own clip: `<audio id="voice" class="clip" src="assets/voice.m4a"
   data-start="0" data-track-index="3" data-volume="1"></audio>`, and set the root's
   `data-duration` to the voice's length plus about 1.5 s for the end card.
5. After render, check the MP4 has AAC stereo audio and that the voice and the captions agree.
