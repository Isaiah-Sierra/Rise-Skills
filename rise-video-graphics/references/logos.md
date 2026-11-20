# Logos of anyone the video names

Rise videos name all kinds of outside groups: another church, a conference or event, a ministry
partner, a school, a sponsor, a city program, and the apps staff use. Whenever a video names one,
try to source its real logo and show it where it makes sense. It reads faster and looks finished.
This is a standard step for every video, not an extra. You won't know ahead of time who will come
up, so the method below works for anyone, not only the starter files.

## 1. List everyone named

Read the script, captions and any notes. List each organization, event, product or brand named,
on screen or in the voiceover: churches and campuses, events and conferences, ministries and
nonprofits, schools, businesses and sponsors, apps and platforms. Generic words count when the
real one is known (Rise uses Google Workspace, so "email" is Gmail).

For each, pin down exactly which one is meant (full name, city, website, the event's year).
Names repeat: "Fellow" is a meeting app and a coffee brand; "Grace Church" is hundreds of
churches. If the script doesn't settle it, ask the person.

## 2. Find the official file

Try these in order and stop at the first that gives the official mark:

1. **Already here.** `assets/logo/third-party/` and its `SOURCES.md`.
2. **From the person.** If they mentioned a file, a Drive folder or an email with the logo, use it.
   Event and partner logos often live in the event's own media kit or a planning email.
3. **The organization's own site.** Search "<name> logo", "<name> press kit", "<name> brand
   assets", "<event> media kit". Look for an SVG or a large PNG on the organization's own domain:
   a brand or press page, the header logo on its home page, or its social profile image. For an
   event, the event's own site or the host church's page for it. Read any usage rules
   (backgrounds, clear space, minimum size, "don't alter") and follow them.
4. **Open logo libraries** (apps and big brands only), both CC0, in a scratch folder:
   ```bash
   npm install --ignore-scripts @iconify-json/logos simple-icons
   python3 scripts/get_logo.py node_modules search <word>
   python3 scripts/get_logo.py node_modules logos <name> out.svg     # full color, preferred
   python3 scripts/get_logo.py node_modules simple <slug> out.svg    # one color, official hex
   ```
   Use the current version where a set also has an old one (`google-gmail`, not `google-gmail-2020`).

Check what you found really is that organization's current logo (right city, not an old version,
not a fan-made or look-alike). Prefer SVG; a PNG must be at least twice the size it will show at.
If nothing official turns up, tell the person which ones you couldn't find and ask for the file.
Until then, set the name as plain text in the Rise fonts. Never draw, trace, rebuild or AI-generate
a logo, and never imitate an organization's typeface.

Copy each new file into `assets/logo/third-party/` with a row in `SOURCES.md`: file, what it is,
where it came from, the date, and which backgrounds it suits.

## 3. Place it where it makes sense

The logo goes where the story puts that name. Think about what the video is saying about it:

- **Named in passing** (a tool in a list, "our friends at Grace Church"): a small mark beside the
  name, shown as the voice says it, then gone with the line.
- **The subject of the beat** (the event being promoted, the partner being thanked, the app being
  explained): the logo carries the beat, larger, alone or with one line of text, and it can be the
  scene's signature moment.
- **A group of them** (five apps, three partner churches): give each one the same slot size and
  treatment, in a row or grid, revealed in the order they're said.
- **An event Rise is hosting or joining:** the event's logo with the date and place in Rise type
  beside it; Rise's own logo still closes the video.
- **Sponsors or partners:** together on one card, equal size, after the main message, not
  competing with it.

Then make it sit well in the Rise look:

- Use `<img src="assets/logo/third-party/<file>">`, not inline SVG (gradient ids can clash).
- Size by height only, never stretch. A mark beside a label is 0.9 to 1.2 times the label's cap
  height; a full logo with its own wordmark replaces the name instead of repeating it.
- Full-color logos go on white or very light fills. On navy, use the organization's white version
  if it has one; otherwise put the logo on a white card or pill.
- Clear space of at least the mark's own height. Never recolor, rotate, crop, outline or add
  effects; animate the card or box it sits in, not the logo itself.
- Rise stays the host: outside logos are guests, never larger than the Rise mark on the same
  frame, and never on the Rise end card unless the person asks (a co-hosted event, for example).

## 4. Check

In the snapshots, look at every logo: right organization, crisp, right colors, nothing clipped or
touching, shown when its name is said. In your handoff, list where each logo came from and any you
couldn't find.
