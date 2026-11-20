# Rise Church brand card for video

Sources: the Rise Church brand guide PDF and the "Brand Rules for Claude" doc in the Rise Church
Drive folder. Where a value was measured rather than printed, it says so. When something you
need is not here, ask; do not invent it.

## Color

| Role | Name in the guide | Hex for screen | Source |
| --- | --- | --- | --- |
| Accent | PMS 192 C (red) | `#EC0044` | Fill in the guide PDF's vector art |
| Headline ink | PMS 2380 C (deep blue / navy) | `#26334A` | Fill in the guide PDF's vector art |
| Body ink | 3C4247 charcoal | `#3C4247` | Printed in the guide |
| Support | PMS 326 C (teal) | `#12AEAB` | Measured from the guide's swatch, not printed |
| Light ground | PMS 663 C (light gray) | `#E7E4EA` | Measured from the guide's swatch, not printed |
| Soft fill | PMS 2295 C (shown as pale mint) | `#CFE3D8` | Measured from the guide's swatch, not printed |
| Paper | White | `#FFFFFF` | |

Use red sparingly: labels, numerals, one underline or highlight per scene, the action. Teal is for
small status marks. Body text never goes on red or teal. Check contrast with
`npx hyperframes check` (it measures every text element).

The three measured values should be confirmed with whoever owns the brand before a public video.

## Type

| Use | Brand font (print) | Screen substitute shipped here | Weight |
| --- | --- | --- | --- |
| Logotype | Gotham Bold | (the logo is art; never typeset it) | |
| Titles | Nexa Slab, with Gotham Bold | Roboto Slab | 700 |
| Labels, wordmarks, buttons | Gotham Bold | Montserrat | 700 to 800 |
| Body, captions | Proxima Nova | Source Sans 3 | 400 to 600 |

The substitutes are the ones the "Brand Rules for Claude" doc names as web fallbacks. If the
church licenses Gotham, Nexa Slab or Proxima Nova as web fonts, drop the files in `assets/fonts`
and swap the `@font-face` sources.

Sizes at 1080p: titles 64 to 140 px, labels 28 px with 0.2em tracking in caps, captions 38 px,
nothing a viewer must read under 28 px.

## Logo

- Files: `assets/logo/rise-logomark.svg` (the weighted circle with the peak) and
  `assets/logo/rise-logo-stacked.svg` (mark over RISE over CHURCH). Both use `currentColor`.
- Prefer the dark logo (navy) on a light background.
- The logomark alone is for small or familiar uses; the full logo on the end card.
- Minimum size 15 pt in print; on screen keep the mark at least 120 px tall.
- Never stretch, rotate, recolor outside the palette, add effects to, or redraw the logo.
- The weighted circle may be used as a design element (for example, large and faint behind
  scenes). Scale and drift it; don't rotate it.

## Other organizations in a Rise video

- Rise leads; another church, event, partner or product appears where the script names it, and
  then it appears as its real logo, not just its name.
- Use the other company's official logo file (its own site or press kit first, then the CC0 sets
  in `references/logos.md`), in its own colors.
  Don't recolor it to the Rise palette, redraw it, or put it inside a Rise shape.
- Give it clear space at least the height of its own mark's smallest part, and put it on white
  (or use the brand's own white version on navy).
- Type its product name in the Rise fonts; don't imitate its typeface.
- Record where the file came from in `assets/logo/third-party/SOURCES.md`.
- If the official file isn't available, ask the person for it, and use the plain name until then.

## Copy and voice

- Write "RISE Church" in running text (Rise Church only appears in the logo art).
- Mission: "Reaching People & Building Lives".
- Pathway: Know God → Find Family → Develop Purpose → Make a Difference. Use these words exactly.
- Voice: warm, coach-like, family language. Short sentences. Speak to one person.
- Footer and end cards: `risechurchtx.com`.
- No em dashes. Typographic apostrophes and quotes.

## Layout habits from the guide

- Generous leading and white space; one idea per frame.
- Small all-caps eyebrow label above each title.
- Large numerals for steps or a sequence.
- Left-aligned titles in the title-safe area, graphics on the right half.
