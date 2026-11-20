#!/usr/bin/env python3
"""Builds alise-rise/index.html: the Alise explainer in the Rise Church look."""
import re, sys, pathlib

proj = pathlib.Path(sys.argv[1])
mark_svg = (proj / "assets/logo/rise-logomark.svg").read_text()
claude_svg = (proj / "assets/logo/claude-mark.svg").read_text()
stack_svg = (proj / "assets/logo/rise-logo-stacked.svg").read_text()

def inline(svg, cls):
    return svg.replace("<svg ", f'<svg class="{cls}" aria-hidden="true" ', 1)

TOTAL = 70
# Timed to the voiceover (assets/voice.m4a, 68.2 s), sentence by sentence.
SCENES = [("s1", 0, 9), ("s2", 9, 13), ("s3", 22, 8.4), ("s4", 30.4, 7.1),
          ("s5", 37.5, 8.1), ("s6", 45.6, 8.2), ("s7", 53.8, 10), ("s8", 63.8, 6.2)]
CAPS = [
    ("c1", 3.0, 8.9, "Claude Duet is a personal Claude you simply text, like a teammate who already knows your week."),
    ("c2", 9.0, 12.6, "It reads your connected Gmail, calendar and Drive."),
    ("c3", 12.6, 16.9, "It keeps your tasks in one list and sends you a morning brief."),
    ("c4", 16.9, 21.9, "It checks in when something needs you, and handles the longer work in the background while you keep moving."),
    ("c5", 22.0, 24.95, "Text it: who still owes receipts this month?"),
    ("c6", 24.95, 30.35, "It pulls the answer from your mail and sheets, and drafts a friendly nudge for each department."),
    ("c7", 30.4, 37.45, "Before each department budget meeting, it hands you a one-page brief built from the emails and spreadsheets you already have."),
    ("c8", 37.5, 40.45, "For events like the serve team Christmas party,"),
    ("c9", 40.45, 45.55, "it tracks the to-dos, holds the dates, and drafts the follow-up email for you to send."),
    ("c10", 45.6, 51.3, "And before Tuesday’s staff meeting, it turns your updates into ready proposals and FYIs,"),
    ("c11", 51.3, 53.75, "so the meeting stays about decisions."),
    ("c12", 53.9, 58.5, "Every step that sends, pays, or can’t be undone waits for your yes."),
    ("c13", 58.5, 63.7, "And money always goes to a person for approval. Claude never buys anything on its own."),
]

def words(text, cls="w"):
    return " ".join(f'<span class="{cls}">{w}</span>' for w in text.split())

scene_html = {}

scene_html["s1"] = f"""
  <div class="eyebrow" id="s1eye">Rise Church staff</div>
  <h1 class="slab hero" id="s1head"><span class="line">{words("Alise, meet your")}</span><span class="line">{words("new")} <span class="hl" id="s1hl">{words("chief of staff.")}<i class="uline" id="s1ul"></i></span></span></h1>
  <div id="s1duet">
    <div class="duetrow"><div class="cmark" id="s1cm">{inline(claude_svg, "claudemark")}</div><div class="wordmark" id="s1wm">Claude Duet</div></div>
    <div class="sub" id="s1sub">A personal Claude you simply text.</div>
  </div>
  <div id="s1week">
    <div class="eyebrow small" id="s1weye">Already knows your week</div>
    <div class="days">
      <div class="day">M</div><div class="day" id="s1tue">T<i class="dot" id="s1dot"></i></div><div class="day">W</div><div class="day">T</div><div class="day">F</div>
    </div>
  </div>"""

scene_html["s2"] = f"""
  <div class="eyebrow" id="s2eye">What it does</div>
  <h2 class="slab title s2t" id="s2title">Connected to your work.</h2>
  <div class="src" id="src1" style="top:420px">Gmail</div>
  <div class="src" id="src2" style="top:540px">Calendar</div>
  <div class="src" id="src3" style="top:660px">Drive</div>
  <svg class="wires" viewBox="0 0 1920 1080" width="1920" height="1080">
    <path class="wire" id="wi1" d="M 432 452 C 600 452 620 572 760 572"/>
    <path class="wire" id="wi2" d="M 432 572 L 760 572"/>
    <path class="wire" id="wi3" d="M 432 692 C 600 692 620 572 760 572"/>
    <path class="wire" id="wo1" d="M 980 572 C 1080 572 1080 330 1160 330"/>
    <path class="wire" id="wo2" d="M 980 572 C 1080 572 1080 460 1160 460"/>
    <path class="wire" id="wo3" d="M 980 572 C 1080 572 1080 590 1160 590"/>
    <path class="wire" id="wo4" d="M 980 572 C 1080 572 1080 720 1160 720"/>
  </svg>
  <div id="s2hub"><div class="hubdisc">{inline(claude_svg, "claudemark")}</div><div class="hublabel" id="s2hl">Claude Duet</div></div>
  <div class="out" id="out1" style="top:292px"><b>One task list</b></div>
  <div class="out" id="out2" style="top:422px"><b>Morning brief</b></div>
  <div class="out" id="out3" style="top:552px"><b>Check-ins when you’re needed</b></div>
  <div class="out" id="out4" style="top:682px"><b>Longer work, in the background</b></div>"""

def numbered(n, sid, eyebrow, title):
    return f"""
  <div class="num slab" id="{sid}num">{n}</div>
  <div class="eyebrow" id="{sid}eye" style="top:470px">{eyebrow}</div>
  <h2 class="slab title side" id="{sid}title">{title}</h2>"""

rows = "".join(
    f'<div class="row" id="r{i}"><i class="av"></i><i class="bar" style="width:{w}px"></i><span class="chip" id="ch{i}">Nudge drafted</span></div>'
    for i, w in zip(range(1, 5), (210, 260, 180, 240)))
scene_html["s3"] = numbered("1", "s3", "Receipts", "Friendly nudges, drafted.") + f"""
  <div class="panel" id="s3panel">
    <div class="ask" id="s3ask">Who still owes receipts this month?</div>
    <div class="from" id="s3from">From your mail and sheets</div>
    {rows}
  </div>"""

bars = "".join(f'<i class="dl" id="dl{i}" style="width:{w}px"></i>' for i, w in zip(range(1, 8), (300, 340, 260, 320, 220, 330, 280)))
scene_html["s4"] = numbered("2", "s4", "Budget meetings", "A one-page brief, ready.") + f"""
  <div class="tile" id="t1" style="top:300px"><svg viewBox="0 0 48 36" width="64" height="48"><rect x="2" y="2" width="44" height="32" rx="4"/><path d="M4 5 L24 20 L44 5"/></svg><span>Emails</span></div>
  <div class="tile" id="t2" style="top:540px"><svg viewBox="0 0 48 36" width="64" height="48"><rect x="2" y="2" width="44" height="32" rx="4"/><path d="M2 13 H46 M2 24 H46 M17 2 V34 M32 2 V34"/></svg><span>Spreadsheets</span></div>
  <svg class="wires" viewBox="0 0 1920 1080" width="1920" height="1080"><path class="wire" id="s4w1" d="M 1220 360 C 1260 360 1260 520 1300 520"/><path class="wire" id="s4w2" d="M 1220 600 C 1260 600 1260 520 1300 520"/></svg>
  <div class="doc" id="s4doc"><div class="dochead">One-page brief</div><div class="docsub">Department budget meeting</div>{bars}<i class="mark" id="s4mark"></i></div>"""

checks = "".join(
    f'<div class="check" id="k{i}"><i class="tick" id="tk{i}"><svg viewBox="0 0 24 24" width="30" height="30"><path d="M5 12.5 L10 17 L19 7"/></svg></i><span>{t}</span></div>'
    for i, t in zip(range(1, 4), ("To-dos tracked", "Dates held", "Follow-up email drafted")))
scene_html["s5"] = numbered("3", "s5", "Events", "Tracked, held, drafted.") + f"""
  <div class="card" id="s5card">
    <div class="cardhead"><span>Serve team Christmas party</span><span class="date" id="s5date">Dec 14</span></div>
    {checks}
    <div class="tag" id="s5tag">Ready for you to send</div>
  </div>"""

notes = "".join(f'<div class="note" id="n{i}"><i style="width:{w}px"></i><i style="width:{w2}px"></i></div>'
                for i, w, w2 in zip(range(1, 7), (220, 180, 240, 200, 160, 230), (140, 200, 120, 170, 190, 110)))
scene_html["s6"] = numbered("4", "s6", "Tuesday staff meeting", "Ready for decisions.") + f"""
  <div class="colhead" id="h1" style="left:960px">Proposals<i class="uline" id="h1ul"></i></div>
  <div class="colhead" id="h2" style="left:1380px">FYIs</div>
  {notes}"""

scene_html["s7"] = """
  <div class="eyebrow" id="s7eye">You stay in charge</div>
  <h2 class="slab hero mid" id="s7head">It waits for your yes.</h2>
  <div id="s7a">
    <div class="pill" id="p1">Sends</div><div class="pill" id="p2">Pays</div><div class="pill" id="p3">Can’t be undone</div>
    <div class="yes" id="s7yes">Yes</div>
  </div>
  <div id="s7b">
    <div class="person" id="s7person"><i class="head"></i><i class="body"></i></div>
    <div class="money" id="s7money">Money always goes to a person for approval.</div>
    <div class="never" id="s7never">Claude never buys anything on its own.</div>
  </div>"""

scene_html["s8"] = f"""
  <div id="s8a">
    <div class="slab big" id="s8l1">Less busy work.</div>
    <div class="slab big red" id="s8l2">More time for people.</div>
  </div>
  <div id="s8b">
    <div id="s8logo">{inline(stack_svg, "stackmark")}</div>
    <div class="closer" id="s8text"><span class="cmark sm">{inline(claude_svg, "claudemark")}</span><span>That’s Claude Duet.</span></div>
    <div class="footer" id="s8foot">risechurchtx.com</div>
  </div>"""

scenes = "\n".join(
    f'    <section id="{sid}" class="clip scene" data-start="{st}" data-duration="{du}" data-track-index="1" data-track-kind="graphics">\n'
    f'      <div class="inner" id="{sid}i">{scene_html[sid]}\n      </div>\n    </section>'
    for sid, st, du in SCENES)

caps = "\n".join(
    f'    <div id="{cid}" class="clip cap" data-start="{a}" data-duration="{round(b - a, 2)}" data-track-index="2" data-track-kind="captions"><span class="captext" id="{cid}t">{text}</span></div>'
    for cid, a, b, text in CAPS)

CSS = r"""
@font-face { font-family: "Rise Display"; src: url('assets/fonts/Montserrat-latin.woff2') format('woff2'); font-weight: 100 900; }
@font-face { font-family: "Rise Slab"; src: url('assets/fonts/RobotoSlab-latin.woff2') format('woff2'); font-weight: 100 900; }
@font-face { font-family: "Rise Text"; src: url('assets/fonts/SourceSans3-latin.woff2') format('woff2'); font-weight: 200 900; }
:root {
  --paper: #FFFFFF; --mist: #E7E4EA; --navy: #26334A; --charcoal: #3C4247;
  --red: #EC0044; --teal: #12AEAB; --mint: #CFE3D8;
  --display: "Rise Display", sans-serif; --slab: "Rise Slab", serif; --text: "Rise Text", sans-serif;
}
* { margin: 0; padding: 0; box-sizing: border-box; }
html, body { width: 1920px; height: 1080px; overflow: hidden; background: var(--paper); }
#root { position: relative; width: 1920px; height: 1080px; background: var(--paper); font-family: var(--text); color: var(--navy); }
#bg { position: absolute; inset: 0; overflow: hidden; }
#bgring { position: absolute; left: 1080px; top: -170px; width: 1180px; height: 1180px; color: var(--mist); opacity: 0.55; }
#bgring svg { width: 100%; height: 100%; }
.scene { position: absolute; inset: 0; }
.inner { position: absolute; inset: 0; }
.slab { font-family: var(--slab); font-weight: 700; letter-spacing: -0.01em; }
.eyebrow { position: absolute; left: 192px; top: 250px; font-family: var(--display); font-weight: 700; font-size: 28px; letter-spacing: 0.2em; text-transform: uppercase; color: var(--red); }
.eyebrow.small { position: static; font-size: 28px; color: var(--charcoal); }
.hero { position: absolute; left: 192px; top: 300px; font-size: 116px; line-height: 1.12; color: var(--navy); }
.hero .line { display: block; }
.w { display: inline-block; }
.hl { position: relative; display: inline-block; }
.uline { position: absolute; left: 0; right: 0; bottom: -6px; height: 10px; background: var(--red); transform-origin: left center; }
#s1duet { position: absolute; left: 192px; top: 250px; width: 1100px; }
.duetrow { display: flex; align-items: center; gap: 40px; }
.cmark { width: 150px; height: 150px; flex: none; }
.cmark svg { width: 100%; height: 100%; display: block; }
.cmark.sm { width: 92px; height: 92px; }
.wordmark { font-family: var(--display); font-weight: 800; font-size: 140px; letter-spacing: -0.03em; color: var(--navy); line-height: 1; }
.sub { margin-top: 26px; font-family: var(--text); font-size: 46px; color: var(--charcoal); }
#s1week { position: absolute; left: 192px; top: 650px; }
.days { display: flex; gap: 18px; margin-top: 22px; }
.day { position: relative; width: 84px; height: 84px; border-radius: 42px; border: 3px solid var(--navy); display: flex; align-items: center; justify-content: center; font-family: var(--display); font-weight: 700; font-size: 32px; color: var(--navy); background: var(--paper); }
.dot { position: absolute; right: -4px; top: -4px; width: 26px; height: 26px; border-radius: 13px; background: var(--red); }
.title { position: absolute; left: 192px; top: 296px; font-size: 76px; line-height: 1.12; color: var(--navy); }
.title.s2t { font-size: 64px; width: 860px; }
.title.side { top: 520px; width: 620px; font-size: 66px; }
.num { position: absolute; left: 180px; top: 150px; font-size: 300px; line-height: 1; color: var(--red); }
.src { position: absolute; left: 192px; width: 240px; height: 64px; justify-content: center; border-radius: 32px; background: var(--navy); color: var(--paper); font-family: var(--display); font-weight: 700; font-size: 28px; display: flex; align-items: center; }
.wires { position: absolute; left: 0; top: 0; }
.wire { fill: none; stroke: var(--navy); stroke-width: 3; stroke-linecap: round; opacity: 0.45; }
#s2hub { position: absolute; left: 760px; top: 462px; width: 220px; height: 220px; }
.hubdisc { width: 220px; height: 220px; border-radius: 110px; background: var(--paper); border: 4px solid var(--mist); display: flex; align-items: center; justify-content: center; }
.hubdisc svg { width: 130px; height: 130px; }
.hublabel { position: absolute; left: -40px; width: 300px; top: 236px; text-align: center; font-family: var(--display); font-weight: 700; font-size: 28px; color: var(--navy); }
.out { position: absolute; left: 1160px; width: 580px; height: 76px; border-radius: 14px; background: var(--paper); border: 3px solid var(--mist); display: flex; align-items: center; padding: 0 26px; font-family: var(--display); font-size: 28px; color: var(--navy); }
.out b { font-weight: 700; white-space: nowrap; }
.out::before { content: ""; width: 16px; height: 16px; border-radius: 8px; background: var(--teal); margin-right: 20px; flex: none; }
.panel { position: absolute; left: 900px; top: 190px; width: 830px; height: 640px; border-radius: 28px; background: var(--paper); border: 3px solid var(--mist); padding: 40px; }
.ask { margin-left: auto; width: fit-content; max-width: 620px; padding: 22px 32px; border-radius: 30px 30px 6px 30px; background: var(--navy); color: var(--paper); font-family: var(--text); font-size: 36px; font-weight: 600; }
.from { margin-top: 34px; font-family: var(--display); font-weight: 700; font-size: 28px; letter-spacing: 0.14em; text-transform: uppercase; color: var(--charcoal); }
.row { display: flex; align-items: center; gap: 22px; margin-top: 26px; height: 64px; }
.av { width: 56px; height: 56px; border-radius: 28px; background: var(--mist); flex: none; }
.bar { height: 18px; border-radius: 9px; background: var(--charcoal); opacity: 0.22; }
.chip { margin-left: auto; padding: 10px 22px; border-radius: 24px; border: 3px solid var(--red); color: var(--red); font-family: var(--display); font-weight: 700; font-size: 28px; }
.tile { position: absolute; left: 920px; width: 300px; height: 120px; border-radius: 20px; background: var(--paper); border: 3px solid var(--mist); display: flex; align-items: center; gap: 22px; padding: 0 28px; font-family: var(--display); font-weight: 700; font-size: 28px; color: var(--navy); }
.tile svg { fill: none; stroke: var(--navy); stroke-width: 3; stroke-linejoin: round; }
.doc { position: absolute; left: 1300px; top: 190px; width: 430px; height: 660px; border-radius: 18px; background: var(--paper); border: 3px solid var(--navy); padding: 44px 40px; }
.dochead { font-family: var(--slab); font-weight: 700; font-size: 40px; color: var(--navy); }
.docsub { margin-top: 8px; margin-bottom: 30px; font-family: var(--text); font-size: 28px; color: var(--charcoal); }
.dl { display: block; height: 16px; border-radius: 8px; background: var(--charcoal); opacity: 0.2; margin-top: 30px; transform-origin: left center; }
.mark { position: absolute; left: 40px; top: 238px; width: 340px; height: 30px; border-radius: 6px; background: var(--red); opacity: 0.18; transform-origin: left center; }
.card { position: absolute; left: 900px; top: 210px; width: 830px; height: 600px; border-radius: 28px; background: var(--paper); border: 3px solid var(--mist); padding: 48px; }
.cardhead { display: flex; align-items: center; justify-content: space-between; font-family: var(--display); font-weight: 700; font-size: 36px; color: var(--navy); margin-bottom: 26px; }
.date { padding: 10px 22px; border-radius: 12px; background: var(--navy); color: var(--paper); font-size: 28px; }
.check { display: flex; align-items: center; gap: 26px; margin-top: 30px; font-family: var(--text); font-size: 38px; color: var(--charcoal); }
.tick { width: 54px; height: 54px; border-radius: 27px; background: var(--red); display: flex; align-items: center; justify-content: center; flex: none; }
.tick svg { fill: none; stroke: var(--paper); stroke-width: 3.4; stroke-linecap: round; stroke-linejoin: round; }
.tag { position: absolute; left: 48px; bottom: 44px; padding: 14px 26px; border-radius: 26px; border: 3px solid var(--teal); color: var(--navy); font-family: var(--display); font-weight: 700; font-size: 28px; }
.colhead { position: absolute; top: 250px; font-family: var(--display); font-weight: 800; font-size: 40px; color: var(--navy); }
.note { position: absolute; left: 0; top: 0; width: 360px; height: 104px; border-radius: 16px; background: var(--paper); border: 3px solid var(--mist); padding: 26px 28px; }
.note i { display: block; height: 14px; border-radius: 7px; background: var(--charcoal); opacity: 0.22; margin-bottom: 20px; }
.hero.mid { top: 300px; font-size: 104px; }
#s7a { position: absolute; left: 0; top: 0; width: 1920px; height: 1080px; }
.pill { position: absolute; top: 560px; height: 80px; padding: 0 36px; border-radius: 40px; border: 3px solid var(--navy); display: flex; align-items: center; font-family: var(--display); font-weight: 700; font-size: 32px; color: var(--navy); }
#p1 { left: 192px; } #p2 { left: 412px; } #p3 { left: 610px; }
.yes { position: absolute; left: 1250px; top: 520px; width: 360px; height: 160px; border-radius: 80px; background: var(--red); color: var(--paper); font-family: var(--display); font-weight: 800; font-size: 72px; display: flex; align-items: center; justify-content: center; }
#s7b { position: absolute; left: 192px; top: 520px; width: 1500px; }
.person { position: absolute; left: 0; top: 0; width: 120px; height: 150px; }
.person .head { position: absolute; left: 32px; top: 0; width: 56px; height: 56px; border-radius: 28px; background: var(--navy); }
.person .body { position: absolute; left: 6px; top: 66px; width: 108px; height: 76px; border-radius: 54px 54px 12px 12px; background: var(--navy); }
.money { position: absolute; left: 170px; top: 26px; font-family: var(--display); font-weight: 700; font-size: 54px; color: var(--navy); white-space: nowrap; }
.never { position: absolute; left: 170px; top: 140px; padding-left: 28px; border-left: 8px solid var(--red); font-family: var(--text); font-size: 48px; color: var(--charcoal); white-space: nowrap; }
#s8a { position: absolute; left: 192px; top: 340px; }
.big { font-size: 140px; line-height: 1.12; color: var(--navy); }
.big.red { color: var(--red); }
#s8b { position: absolute; inset: 0; }
#s8logo { position: absolute; left: 870px; top: 170px; width: 180px; height: 279px; color: var(--navy); }
#s8logo svg { width: 100%; height: 100%; }
.closer { position: absolute; left: 0; width: 1920px; top: 520px; display: flex; align-items: center; justify-content: center; gap: 30px; font-family: var(--display); font-weight: 800; font-size: 96px; letter-spacing: -0.02em; color: var(--navy); }
.footer { position: absolute; left: 0; width: 1920px; top: 700px; text-align: center; font-family: var(--display); font-weight: 600; font-size: 30px; letter-spacing: 0.16em; color: var(--charcoal); }
.cap { position: absolute; left: 192px; top: 878px; width: 1536px; height: 104px; display: flex; align-items: center; justify-content: center; }
.captext { display: inline-block; max-width: 1480px; text-align: center; font-family: var(--text); font-weight: 600; font-size: 38px; line-height: 1.3; color: var(--charcoal); }
"""

JS = r"""
const F = 1 / 30;
const tl = gsap.timeline({ paused: true });
// Scene beats were designed on a 77 s silent cut; R() moves each beat onto the voiceover.
const A = [[0,0],[0.5,0.4],[3.65,2.6],[4.1,3.05],[6.3,6.9],[8.65,8.65],[9,9],
  [13.1,12.7],[15.0,15.0],[17.4,17.0],[19.2,18.6],[21.65,21.65],[22,22],
  [22.8,22.8],[25.6,25.0],[27.3,27.4],[30.65,30.05],[31,30.4],
  [31.25,30.65],[33.2,32.6],[35.6,35.0],[38.65,37.15],[39,37.5],
  [39.25,37.75],[43.4,40.5],[44.3,41.5],[45.2,43.0],[45.6,43.6],[47.65,45.25],[48,45.6],
  [48.25,45.85],[50.7,49.3],[51.3,49.8],[53.2,52.6],[56.65,53.45],[57,53.8],
  [57.2,54.0],[58.0,54.6],[59.2,57.0],[60.6,57.9],[61.7,58.35],[62.0,58.65],[62.1,58.7],[64.3,61.15],[67.65,63.45],[68,63.8],
  [68.3,64.0],[69.4,65.4],[71.7,66.5],[72.05,66.85],[72.15,66.9],[72.5,67.0],[73.3,67.6],[77,70]];
const R = (t) => { for (let i = 1; i < A.length; i++) { const [a0, b0] = A[i - 1], [a1, b1] = A[i]; if (t <= a1) return b0 + (t - a0) * (b1 - b0) / (a1 - a0); } return t; };
const T = { to: (s, v, p) => tl.to(s, v, R(p)), fromTo: (s, a, b, p) => tl.fromTo(s, a, b, R(p)), set: (s, v, p) => tl.set(s, v, R(p)) };
const out = (sel, at, d) => { T.to(sel, { opacity: 0, y: -24, duration: d, ease: "power2.in" }, at); };

// Background: the Rise weighted circle, drifting slowly the whole film.
tl.to("#bgring", { scale: 1.05, x: -40, y: 20, duration: 69.6, ease: "sine.inOut" }, 0.2);

// S1: intro (0 to 9)
T.fromTo("#s1head .w", { y: 46, opacity: 0 }, { y: 0, opacity: 1, duration: 18 * F, ease: "back.out(1.7)", stagger: 3 * F }, 0.5);
T.fromTo("#s1ul", { scaleX: 0 }, { scaleX: 1, duration: 20 * F, ease: "expo.out" }, 1.7);
T.to("#s1head", { opacity: 0, y: -30, duration: 10 * F, ease: "power2.in" }, 3.65);
T.to("#s1eye", { opacity: 0, duration: 8 * F, ease: "power1.in" }, 3.7);
T.set("#s1head", { opacity: 0 }, 4.0);
T.set("#s1eye", { opacity: 0 }, 4.0);
T.fromTo("#s1cm", { scale: 0.92, opacity: 0 }, { scale: 1, opacity: 1, duration: 16 * F, ease: "circ.out" }, 4.1);
T.fromTo("#s1wm", { scale: 0.93, opacity: 0, transformOrigin: "left center" }, { scale: 1, opacity: 1, duration: 16 * F, ease: "back.out(1.7)" }, 4.3);
T.fromTo("#s1sub", { x: -40, opacity: 0 }, { x: 0, opacity: 1, duration: 16 * F, ease: "power3.out" }, 4.3 + 6 * F);
T.fromTo("#s1weye", { opacity: 0 }, { opacity: 1, duration: 10 * F, ease: "power1.out" }, 6.3);
T.fromTo("#s1week .day", { y: 26, opacity: 0 }, { y: 0, opacity: 1, duration: 12 * F, ease: "power4.out", stagger: 2 * F }, 6.4);
T.fromTo("#s1dot", { scale: 0.9, opacity: 0 }, { scale: 1, opacity: 1, duration: 10 * F, ease: "back.out(2.6)" }, 7.2);
T.to("#s1tue", { backgroundColor: "#26334A", color: "#FFFFFF", duration: 8 * F, ease: "power2.out" }, 7.2);
out("#s1i", 8.65, 8 * F);
T.set("#s1i", { opacity: 0 }, 9);

// S2: what it does (9 to 22)
T.fromTo("#s2eye", { clipPath: "inset(0 100% 0 0)" }, { clipPath: "inset(0 0% 0 0)", duration: 14 * F, ease: "power3.out" }, 9.2);
T.fromTo("#s2title", { y: 36, opacity: 0 }, { y: 0, opacity: 1, duration: 18 * F, ease: "power4.out" }, 9.3);
T.fromTo(".src", { x: -60, opacity: 0 }, { x: 0, opacity: 1, duration: 16 * F, ease: "power3.out", stagger: 4 * F }, 9.6);
T.fromTo("#s2hub", { scale: 0.9, opacity: 0 }, { scale: 1, opacity: 1, duration: 18 * F, ease: "back.out(1.7)" }, 10.3);
T.fromTo("#wi1, #wi2, #wi3", { strokeDasharray: 400, strokeDashoffset: 400 }, { strokeDashoffset: 0, duration: 20 * F, ease: "expo.out", stagger: 3 * F }, 10.8);
const outs = [["#out1", "#wo1", 13.1], ["#out2", "#wo2", 15.0], ["#out3", "#wo3", 17.4], ["#out4", "#wo4", 19.2]];
outs.forEach(([o, w, t]) => {
  T.fromTo(w, { strokeDasharray: 320, strokeDashoffset: 320 }, { strokeDashoffset: 0, duration: 14 * F, ease: "expo.out" }, t);
  T.fromTo(o, { x: 50, opacity: 0 }, { x: 0, opacity: 1, duration: 14 * F, ease: "power2.out" }, t + 4 * F);
  T.fromTo(o + " b", { x: 14 }, { x: 0, duration: 14 * F, ease: "power2.out" }, t + 7 * F);
});
T.to("#s2hub", { scale: 1.07, duration: 6 * F, ease: "power1.out" }, 16.3);
T.to("#s2hub", { scale: 1, duration: 12 * F, ease: "power1.inOut" }, 16.3 + 6 * F);
out("#s2i", 21.65, 8 * F);
T.set("#s2i", { opacity: 0 }, 22);

// Numbered scenes share an opening: numeral, label, title.
function opener(id, t) {
  T.fromTo(id + "num", { y: 50, opacity: 0 }, { y: 0, opacity: 1, duration: 18 * F, ease: "power4.out" }, t);
  T.fromTo(id + "eye", { clipPath: "inset(0 100% 0 0)" }, { clipPath: "inset(0 0% 0 0)", duration: 14 * F, ease: "power3.out" }, t + 6 * F);
  T.fromTo(id + "title", { y: 30, opacity: 0 }, { y: 0, opacity: 1, duration: 16 * F, ease: "power3.out" }, t + 10 * F);
}

// S3: receipts (22 to 31)
opener("#s3", 22.25);
T.fromTo("#s3panel", { x: 70, opacity: 0 }, { x: 0, opacity: 1, duration: 20 * F, ease: "expo.out" }, 22.35);
T.fromTo("#s3ask", { y: 30, scale: 0.95, opacity: 0, transformOrigin: "right bottom" }, { y: 0, scale: 1, opacity: 1, duration: 16 * F, ease: "back.out(1.7)" }, 22.8);
T.fromTo("#s3from", { opacity: 0 }, { opacity: 1, duration: 10 * F, ease: "power1.out" }, 25.6);
T.fromTo("#s3panel .row", { x: 40, opacity: 0 }, { x: 0, opacity: 1, duration: 12 * F, ease: "power3.out", stagger: 4 * F }, 25.9);
T.fromTo("#s3panel .chip", { scale: 0.9, opacity: 0 }, { scale: 1, opacity: 1, duration: 10 * F, ease: "back.out(2.6)", stagger: 5 * F }, 27.3);
out("#s3i", 30.65, 8 * F);
T.set("#s3i", { opacity: 0 }, 31);

// S4: budget meetings (31 to 39)
opener("#s4", 31.25);
T.fromTo("#t1, #t2", { y: 34, opacity: 0 }, { y: 0, opacity: 1, duration: 16 * F, ease: "power3.out", stagger: 4 * F }, 31.6);
T.fromTo("#s4w1, #s4w2", { strokeDasharray: 300, strokeDashoffset: 300 }, { strokeDashoffset: 0, duration: 16 * F, ease: "expo.out", stagger: 2 * F }, 32.9);
T.fromTo("#s4doc", { scale: 0.94, opacity: 0, transformOrigin: "center center" }, { scale: 1, opacity: 1, duration: 20 * F, ease: "expo.out" }, 33.2);
T.fromTo("#s4doc .dl", { scaleX: 0 }, { scaleX: 1, duration: 14 * F, ease: "circ.out", stagger: 3 * F }, 33.7);
T.fromTo("#s4mark", { scaleX: 0 }, { scaleX: 1, duration: 18 * F, ease: "power2.inOut" }, 35.6);
out("#s4i", 38.65, 8 * F);
T.set("#s4i", { opacity: 0 }, 39);

// S5: events (39 to 48)
opener("#s5", 39.25);
T.fromTo("#s5card", { y: 50, opacity: 0 }, { y: 0, opacity: 1, duration: 18 * F, ease: "power3.out" }, 39.5);
T.fromTo("#s5date", { scale: 0.9, opacity: 0 }, { scale: 1, opacity: 1, duration: 10 * F, ease: "back.out(1.7)" }, 40.3);
[43.4, 44.3, 45.2].forEach((t, i) => {
  T.fromTo("#k" + (i + 1), { x: 30, opacity: 0 }, { x: 0, opacity: 1, duration: 12 * F, ease: "power2.out" }, t);
  T.fromTo("#tk" + (i + 1), { scale: 0.9 }, { scale: 1, duration: 10 * F, ease: "back.out(2.6)" }, t + 3 * F);
});
T.fromTo("#s5tag", { y: 20, opacity: 0 }, { y: 0, opacity: 1, duration: 12 * F, ease: "power4.out" }, 45.6);
out("#s5i", 47.65, 8 * F);
T.set("#s5i", { opacity: 0 }, 48);

// S6: Tuesday staff meeting (48 to 57)
opener("#s6", 48.25);
const pile = [[1240, 330, -4], [1270, 360, 3], [1220, 390, -2], [1260, 420, 5], [1230, 450, -3], [1250, 480, 2]];
const dest = [[960, 340], [1380, 340], [960, 480], [1380, 480], [960, 620], [1380, 620]];
pile.forEach(([x, y, r], i) => {
  T.set("#n" + (i + 1), { x: x, y: y, rotation: r }, 48);
  T.fromTo("#n" + (i + 1), { opacity: 0, scale: 0.93 }, { opacity: 1, scale: 1, duration: 12 * F, ease: "power2.out" }, 48.6 + i * 3 * F);
});
T.fromTo("#h1, #h2", { y: -20, opacity: 0 }, { y: 0, opacity: 1, duration: 14 * F, ease: "power3.out", stagger: 4 * F }, 50.7);
dest.forEach(([x, y], i) => {
  T.to("#n" + (i + 1), { x: x, y: y, rotation: 0, duration: 18 * F, ease: "power3.inOut" }, 51.3 + i * 3 * F);
});
T.fromTo("#h1ul", { scaleX: 0 }, { scaleX: 1, duration: 18 * F, ease: "expo.out" }, 53.2);
out("#s6i", 56.65, 8 * F);
T.set("#s6i", { opacity: 0 }, 57);

// S7: guardrail (57 to 68)
T.fromTo("#s7eye", { clipPath: "inset(0 100% 0 0)" }, { clipPath: "inset(0 0% 0 0)", duration: 14 * F, ease: "power3.out" }, 57.2);
T.fromTo("#s7head", { y: 40, opacity: 0 }, { y: 0, opacity: 1, duration: 18 * F, ease: "back.out(1.7)" }, 57.35);
T.fromTo("#s7a .pill", { y: 24, opacity: 0 }, { y: 0, opacity: 1, duration: 12 * F, ease: "power4.out", stagger: 3 * F }, 58.0);
T.fromTo("#s7yes", { scale: 0.9, opacity: 0 }, { scale: 1, opacity: 1, duration: 16 * F, ease: "back.out(1.7)" }, 59.2);
T.to("#s7yes", { scale: 0.95, duration: 4 * F, ease: "power2.in" }, 60.6);
T.to("#s7yes", { scale: 1, duration: 10 * F, ease: "back.out(2.6)" }, 60.6 + 4 * F);
T.to("#s7a", { opacity: 0, y: -24, duration: 8 * F, ease: "power2.in" }, 61.7);
T.set("#s7a", { opacity: 0 }, 62.0);
T.fromTo("#s7person", { y: 30, opacity: 0 }, { y: 0, opacity: 1, duration: 16 * F, ease: "power3.out" }, 62.1);
T.fromTo("#s7money", { x: -36, opacity: 0 }, { x: 0, opacity: 1, duration: 16 * F, ease: "power3.out" }, 62.1 + 3 * F);
T.fromTo("#s7never", { clipPath: "inset(0 100% 0 0)" }, { clipPath: "inset(0 0% 0 0)", duration: 22 * F, ease: "power2.inOut" }, 64.3);
out("#s7i", 67.65, 8 * F);
T.set("#s7i", { opacity: 0 }, 68);

// S8: close (68 to 77)
T.fromTo("#s8l1", { y: 50, opacity: 0 }, { y: 0, opacity: 1, duration: 18 * F, ease: "back.out(1.7)" }, 68.3);
T.fromTo("#s8l2", { y: 50, opacity: 0 }, { y: 0, opacity: 1, duration: 18 * F, ease: "power4.out" }, 69.4);
T.to("#s8a", { opacity: 0, y: -24, duration: 10 * F, ease: "power2.in" }, 71.7);
T.set("#s8a", { opacity: 0 }, 72.05);
T.fromTo("#s8logo", { scale: 0.94, opacity: 0, transformOrigin: "center bottom" }, { scale: 1, opacity: 1, duration: 24 * F, ease: "expo.out" }, 72.15);
T.fromTo("#s8text", { y: 30, opacity: 0 }, { y: 0, opacity: 1, duration: 18 * F, ease: "power3.out" }, 72.5);
T.fromTo("#s8foot", { opacity: 0 }, { opacity: 1, duration: 14 * F, ease: "power1.out" }, 73.3);

// Captions: each line rises in, then cuts to the next.
document.querySelectorAll(".captext").forEach((el) => {
  const start = parseFloat(el.parentElement.dataset.start);
  tl.fromTo(el, { y: 10, opacity: 0 }, { y: 0, opacity: 1, duration: 6 * F, ease: "power2.out" }, start + 2 * F);
});

window.__timelines["main"] = tl;
tl.seek(0);
"""

html = f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1920, height=1080" />
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>
    <style>{CSS}</style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{TOTAL}" data-width="1920" data-height="1080">
    <div id="bg" class="clip" data-start="0" data-duration="{TOTAL}" data-track-index="0"><div id="bgring">{inline(mark_svg, "ring")}</div></div>
{scenes}
{caps}
    <audio id="voice" class="clip" src="assets/voice.m4a" data-start="0" data-track-index="3" data-volume="1"></audio>
    </div>
    <script>{JS}</script>
  </body>
</html>
"""
(proj / "index.html").write_text(html)
print("wrote", proj / "index.html", len(html))
