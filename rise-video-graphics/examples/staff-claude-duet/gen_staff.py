#!/usr/bin/env python3
"""Builds staff/index.html: "RISE Staff: Claude and Duet" in the Rise Church look.

Every beat is keyed to a caption cue, so retiming to the real voice only needs caption
start/end times: pass a JSON file of [[start, end], ...] (one pair per caption) as argv[2].
Without it, times are estimated from word counts.
"""
import json, re, sys, pathlib

proj = pathlib.Path(sys.argv[1])
timing_file = sys.argv[2] if len(sys.argv) > 2 else None
mark_svg = (proj / "assets/logo/rise-logomark.svg").read_text()
claude_svg = (proj / "assets/logo/claude-mark.svg").read_text()
stack_svg = (proj / "assets/logo/rise-logo-stacked.svg").read_text()

def inline(svg, cls):
    return svg.replace("<svg ", f'<svg class="{cls}" aria-hidden="true" ', 1)

# Captions: the narration, line by line (from Drive's transcript, cleaned).
# A third field of False means the line is on screen already, so no caption is drawn.
CAPS = [
    "Team, over the next few weeks, every one of us is getting set up with Claude.",  # 1
    "In the next few minutes, here’s what it is, how it works,",
    "and how it can give us back time for the work that matters most, people.",
    "Claude is an AI assistant made by a company called Anthropic.",
    "You talk to it in plain English, the way you’d message a coworker.",  # 5
    "It can read, write, summarize, plan, and organize.",
    "It doesn’t replace your judgment or your calling.",
    "It’s a tool, and you’re still the one who decides.",
    "How does it work?",
    "Claude learned the patterns of language from a huge amount of writing.",  # 10
    "When you ask it something, it builds the most helpful answer it can, one word at a time.",
    "That’s why it’s so good at first drafts and summaries.",
    "It’s also why it can sometimes be confidently wrong.",
    "So we always check its work, especially names, dates, numbers, and scripture references.",
    "A recent walkthrough on how Claude works inside organizations made one simple point.",  # 15
    "At work, it’s the same Claude, wrapped in layers that the organization controls.",
    "For us, that means three things.",
    "You use it through your Rise account, so church work stays in the church’s account.",
    "When it connects to tools like Gmail, Drive, or Planning Center,",
    "it can only see what you already have access to. It’s not a back door.",  # 20
    "And Anthropic says chats on business plans aren’t used to train its models by default.",
    "Now, Duet. Claude Duet is the app where Claude works like a chief of staff for each of us.",
    "Instead of starting from a blank chat every time, it keeps track of what’s on your plate.",
    "You get a morning brief, check-ins through the day when something needs you,",
    "and a tasks list that stays current.",  # 25
    "Bigger jobs run in the background while you keep working,",
    "and over time, it learns how you like things done.",
    "Here’s where the time comes back. Start with proposals.",
    "Whether it’s a new ministry idea, an event budget, or a request to leadership,",
    "most of us start from a blank page and dig through old files.",  # 30
    "With Claude, you give it your notes and goals, and you get a solid first draft in minutes.",
    "Your time goes into making it right, not getting it started.",
    "Next, standardization.",
    "Right now, every memo, plan, and handout looks a little different,",
    "and we spend time fixing logos, fonts, and layouts.",  # 35
    "Claude can build from our Rise templates,",
    "so staff memos, proposals, and checklists come out with the same look and the same sections.",
    "And we’ve already built an AI folder with our style guides and templates,",
    "ready to add to a Claude project or to its memory, so it gets our look and voice right from the start.",
    "That’s less rework for you, and documents that look like one team made them.",  # 40
    "Third, one place for our data.",
    "Today, the answer to a simple question can live in five different apps.",
    "Meeting notes and action items are in Fellow.",
    "Scorecards, rocks, and to-do lists are in Ninety.",
    "Then there’s email, the calendar, and Planning Center.",  # 45
    "Once those tools are connected, you can just ask,",
    "“What did we decide in Tuesday’s meeting? Who owns what?",
    "And are our numbers on track this week?”",
    "Claude pulls it together in one answer,",
    "so you’re not jumping between tabs to piece it together.",  # 50
    "And it helps with the everyday follow-through.",
    "Ask it to draft Sunday’s reminder to the serve teams.",
    "Summarize a meeting and list who owes what.",
    "Find a time next week for two busy leads, or turn sermon notes into a small group guide.",
    "Things that used to slip between meetings get caught.",  # 55
    "A few simple guardrails.",
    "Duet drafts, and you decide.",
    "It asks before it sends anything in your name, pays for anything, or deletes anything.",
    "A person reviews everything before it goes public.",
    "Keep pastoral care conversations, counseling details, and anyone’s private information out of it.",  # 60
    "And if something looks off or doesn’t sound like you, fix it or ask.",
    "So here’s the invitation.",
    "We’ll get each of you set up in the coming weeks, with help along the way.",
    "When you’re in, start small.",
    "Pick one task that eats your time, and let Claude take the first pass.",  # 65
    "The goal isn’t to do more busy work faster.",
    "It’s to spend less of our week on admin and more of it with people.",
    "And whatever you do, do it heartily, as to the Lord and not to men.",
    "Colossians 3:23.",
    "Questions? Ask Danny or Isaiah.",  # 70
]
NO_CAPTION = {68, 69, 70}  # the scripture and the end card carry these words on screen

# ---- timing -------------------------------------------------------------------------
if timing_file:
    TIMES = json.loads(pathlib.Path(timing_file).read_text())
    assert len(TIMES) == len(CAPS), (len(TIMES), len(CAPS))
    VOICE_END = TIMES[-1][1]
else:
    TIMES, t = [], 0.4
    for line in CAPS:
        d = len(line.split()) / 2.55
        TIMES.append([round(t, 2), round(t + d, 2)])
        t += d + (0.55 if line.rstrip("”").endswith((".", "?")) else 0.2)
    VOICE_END = TIMES[-1][1]
TOTAL = round(VOICE_END + 3.0, 2)

def cue(n, word=None):
    a, b = TIMES[n - 1]
    if word is None:
        return a
    text = CAPS[n - 1]
    i = text.find(word)
    assert i >= 0, (n, word)
    return round(a + (b - a) * i / max(len(text), 1), 3)

# Scenes: id -> first caption. Each scene runs until the next one starts.
SCENE_FIRST = [("s1", 1), ("s2", 4), ("s3", 9), ("s4", 14), ("s5", 15), ("s6", 18), ("s7", 22),
               ("s8", 28), ("s9", 33), ("s10", 38), ("s11", 41), ("s12", 46), ("s13", 51),
               ("s14", 56), ("s15", 62), ("s16", 68), ("s17", 70)]
SCENES = []
for i, (sid, n) in enumerate(SCENE_FIRST):
    st = 0.0 if i == 0 else round(cue(n) - 0.25, 2)
    SCENES.append([sid, st])
for i in range(len(SCENES)):
    end = SCENES[i + 1][1] if i + 1 < len(SCENES) else TOTAL
    SCENES[i].append(round(end - SCENES[i][1], 2))
SSTART = {s: a for s, a, d in SCENES}
SEND = {s: round(a + d, 2) for s, a, d in SCENES}

def words(text, cls="w"):
    return " ".join(f'<span class="{cls}">{w}</span>' for w in text.split())

H = {}

# S1: intro
H["s1"] = f"""
  <div class="eyebrow" id="s1eye">Rise Church staff</div>
  <h1 class="slab hero" id="s1head"><span class="line">{words("Every one of us")}</span><span class="line">{words("is getting set up with")}</span><span class="line"><span class="cmark inl" id="s1cm">{inline(claude_svg, "claudemark")}</span> <span class="hl" id="s1hl">{words("Claude.")}<i class="uline" id="s1ul"></i></span></span></h1>
  <div id="s1b">
    <div class="eyebrow" style="top:250px" id="s1beye">The next few minutes</div>
    <div class="agenda" id="ag1" style="top:330px"><span class="anum">01</span>What it is</div>
    <div class="agenda" id="ag2" style="top:460px"><span class="anum">02</span>How it works</div>
    <div class="agenda" id="ag3" style="top:590px"><span class="anum">03</span>Where time comes back</div>
    <div class="people slab" id="s1people">People.</div>
  </div>"""

# S2: what it is
verbs = "".join(f'<div class="verb" id="v{i}">{v}</div>' for i, v in enumerate(["Read", "Write", "Summarize", "Plan", "Organize"], 1))
H["s2"] = f"""
  <div id="s2a">
    <div class="eyebrow" id="s2eye">What it is</div>
    <div class="duetrow" id="s2row" style="position:absolute;left:192px;top:310px"><div class="cmark" id="s2cm">{inline(claude_svg, "claudemark")}</div><div class="wordmark" id="s2wm">Claude</div></div>
    <div class="sub" id="s2sub" style="position:absolute;left:192px;top:480px">An AI assistant made by <img class="blogo anth" id="s2anth" src="assets/logo/third-party/anthropic-wordmark.svg" alt="Anthropic"></div>
    <div class="bubble" id="s2bub">Can you help me write this week’s update?</div>
    <div class="bubcap" id="s2bcap">Plain English, like messaging a coworker</div>
    <div class="verbs" id="s2verbs">{verbs}</div>
  </div>
  <div id="s2b">
    <div class="eyebrow" id="s2beye">It doesn’t replace</div>
    <div class="slab big2" id="s2l1">Your judgment.</div>
    <div class="slab big2" id="s2l2">Your calling.</div>
    <div class="decide" id="s2dec"><span>It’s a tool.</span> <span class="red" id="s2you">You decide.</span></div>
  </div>"""

# S3: how it works
lib = "".join(f'<i class="libl" style="top:{220 + i * 46}px;left:{1010 + (i % 3) * 18}px;width:{w}px"></i>'
              for i, w in enumerate([560, 620, 500, 600, 540, 640, 580, 520, 610, 470, 590, 560]))
draft = "Here’s a first draft of Sunday’s welcome for our guests"
H["s3"] = f"""
  <div class="eyebrow" id="s3eye">How it works</div>
  <h2 class="slab title side3" id="s3title">One word<br>at a time.</h2>
  <div class="sub3" id="s3sub">It learned the patterns of language from a huge amount of writing.</div>
  <div id="s3lib">{lib}</div>
  <div class="panel3" id="s3panel">
    <div class="ask small" id="s3ask">Draft a welcome for Sunday</div>
    <div class="gen" id="s3gen">{words(draft, "gw")}<i class="caret" id="s3caret"></i></div>
    <div class="tags">
      <span class="tag3 good" id="s3t1">First drafts</span><span class="tag3 good" id="s3t2">Summaries</span><span class="tag3 warn" id="s3t3">Sometimes confidently wrong</span>
    </div>
  </div>"""

# S4: check its work
checks = "".join(
    f'<div class="check" id="k{i}"><i class="tick" id="tk{i}"><svg viewBox="0 0 24 24" width="30" height="30"><path d="M5 12.5 L10 17 L19 7"/></svg></i><span>{t}</span></div>'
    for i, t in enumerate(["Names", "Dates", "Numbers", "Scripture references"], 1))
H["s4"] = f"""
  <div class="eyebrow" id="s4eye" style="top:400px">So we always</div>
  <h2 class="slab title side" id="s4title" style="top:450px">Check its work.</h2>
  <div class="card" id="s4card"><div class="cardhead"><span>Before it goes anywhere</span></div>{checks}</div>"""

# S5: layers (signature moment)
H["s5"] = f"""
  <div class="eyebrow" id="s5eye">Claude at work</div>
  <h2 class="slab title side" id="s5title" style="top:300px">The same Claude, wrapped in layers we control.</h2>
  <div class="three" id="s5three"><span class="red">3</span> things that means for us</div>
  <div id="s5rings">
    <div class="ring r3" id="rg3"></div><div class="ring r2" id="rg2"></div><div class="ring r1" id="rg1"></div>
    <div class="hubdisc big" id="s5hub">{inline(claude_svg, "claudemark")}</div>
    <div class="rlab" id="rl1" style="left:530px;top:118px">Rise account</div>
    <div class="rlab" id="rl2" style="left:560px;top:250px">Your access</div>
    <div class="rlab" id="rl3" style="left:600px;top:382px">Business plan</div>
  </div>"""

# S6: three things
H["s6"] = """
  <div class="trow" id="tr1" style="top:200px"><div class="tnum slab">1</div><div><div class="thead slab">Your Rise account</div><div class="tsub">Church work stays in the church’s account.</div></div></div>
  <div class="trow" id="tr2" style="top:400px"><div class="tnum slab">2</div><div><div class="thead slab">Only what you can already see</div><div class="tsub apps" id="s6apps"><span class="app" id="ap1"><img src="assets/logo/third-party/gmail.svg" alt="">Gmail</span><span class="app" id="ap2"><img src="assets/logo/third-party/google-drive.svg" alt="">Drive</span><span class="app pco" id="ap3"><img src="assets/logo/third-party/planning-center-full-color.svg" alt="Planning Center"></span><span id="tr2sub">It’s not a back door.</span></div></div></div>
  <div class="trow" id="tr3" style="top:630px"><div class="tnum slab">3</div><div><div class="thead slab">Not used to train its models</div><div class="tsub">By default on business plans, Anthropic says.</div></div></div>"""

# S7: Claude Duet
outs7 = [("o71", "Morning brief"), ("o72", "Check-ins when something needs you"), ("o73", "A tasks list that stays current"),
         ("o74", "Bigger jobs in the background"), ("o75", "Learns how you like things done")]
oy = [224, 340, 456, 572, 688]
H["s7"] = f"""
  <div class="eyebrow" id="s7eye">Claude Duet</div>
  <h2 class="slab title" id="s7title" style="width:520px;font-size:62px">A chief of staff for each of us.</h2>
  <div class="plate" id="s7plate">Keeps track of what’s on your plate</div>
  <svg class="wires" viewBox="0 0 1920 1080" width="1920" height="1080">
    {''.join(f'<path class="wire" id="w7{i}" d="M 990 500 C 1060 500 1060 {y + 38} 1130 {y + 38}"/>' for i, y in enumerate(oy, 1))}
  </svg>
  <div id="s7hub"><div class="hubdisc">{inline(claude_svg, "claudemark")}</div><div class="hublabel">Claude Duet</div></div>
  {''.join(f'<div class="out" id="{o}" style="top:{y}px"><b>{t}</b></div>' for (o, t), y in zip(outs7, oy))}"""

# S8: proposals
bars8 = "".join(f'<i class="dl" id="d8{i}" style="width:{w}px"></i>' for i, w in enumerate((300, 340, 260, 320, 220, 330, 280), 1))
H["s8"] = f"""
  <div id="s8a"><div class="eyebrow" id="s8eye0">Part two</div><div class="slab hero" id="s8head">Where the time<br>comes back.</div></div>
  <div id="s8b">
    <div class="num slab" id="s8num">1</div>
    <div class="eyebrow" id="s8eye" style="top:470px">Proposals</div>
    <h2 class="slab title side" id="s8title">A solid first draft in minutes.</h2>
    <div class="ideas" id="s8ideas"><div class="idea" id="i81">New ministry idea</div><div class="idea" id="i82">Event budget</div><div class="idea" id="i83">Request to leadership</div><div class="blank" id="s8blank">Blank page</div></div>
    <div class="tile" id="t81" style="top:330px"><svg viewBox="0 0 48 36" width="64" height="48"><rect x="6" y="2" width="36" height="32" rx="4"/><path d="M13 12 H35 M13 19 H35 M13 26 H27"/></svg><span>Your notes</span></div>
    <div class="tile" id="t82" style="top:560px"><svg viewBox="0 0 48 36" width="64" height="48"><circle cx="24" cy="18" r="15"/><circle cx="24" cy="18" r="8"/><circle cx="24" cy="18" r="2"/></svg><span>Your goals</span></div>
    <svg class="wires" viewBox="0 0 1920 1080" width="1920" height="1080"><path class="wire" id="w81" d="M 1220 390 C 1260 390 1260 520 1300 520"/><path class="wire" id="w82" d="M 1220 620 C 1260 620 1260 520 1300 520"/></svg>
    <div class="doc" id="s8doc"><div class="dochead">First draft</div><div class="docsub">Proposal</div>{bars8}<i class="mark" id="s8mark"></i></div>
    <div class="right" id="s8right">Your time: making it right</div>
  </div>"""

# S9: standardization
def doc9(i, label):
    return f'<div class="sdoc" id="sd{i}"><div class="sbar" id="sb{i}"></div><div class="slogo" id="sl{i}">{inline(mark_svg, "smark")}</div><div class="slab9">{label}</div><i></i><i></i><i></i><i></i></div>'
H["s9"] = f"""
  <div class="num slab" id="s9num">2</div>
  <div class="eyebrow" id="s9eye" style="top:470px">Standardization</div>
  <h2 class="slab title side" id="s9title">Same look.<br>Same sections.</h2>
  {doc9(1, "Memo")}{doc9(2, "Proposal")}{doc9(3, "Checklist")}
  <div class="fix" id="s9fix">Fixing logos, fonts and layouts</div>
  <div class="tpl" id="s9tpl">Built from our Rise templates</div>"""

# S10: AI folder
H["s10"] = f"""
  <div class="eyebrow" id="s10eye">Already built</div>
  <h2 class="slab title side" id="s10title" style="top:300px">Our AI folder.</h2>
  <div class="sub10" id="s10sub">Style guides and templates, ready for Claude.</div>
  <div class="folder" id="s10folder"><i class="ftab"></i><i class="fbody"></i><span class="flab">AI folder</span></div>
  <div class="fitem" id="fi1">Style guides</div><div class="fitem" id="fi2">Templates</div>
  <svg class="wires" viewBox="0 0 1920 1080" width="1920" height="1080"><path class="wire" id="w101" d="M 1300 440 C 1380 440 1380 360 1450 360"/><path class="wire" id="w102" d="M 1300 440 C 1380 440 1380 540 1450 540"/></svg>
  <div class="dest" id="de1" style="top:322px">A Claude project</div><div class="dest" id="de2" style="top:502px">Its memory</div>
  <div class="oneteam" id="s10one"><span>Less rework.</span> <span class="red">One team’s look.</span></div>"""

# S11: five apps
apps11 = [("ap11", "Fellow", "Meeting notes, action items"), ("ap12", "Ninety", "Scorecards, rocks, to-dos"),
          ("ap13", '<img src="assets/logo/third-party/gmail.svg" alt="">Email', ""), ("ap14", '<img src="assets/logo/third-party/google-calendar.svg" alt="">Calendar', ""),
          ("ap15", '<img class="pco" src="assets/logo/third-party/planning-center-full-color.svg" alt="Planning Center">', "")]
pos11 = [(900, 200), (1320, 200), (900, 380), (1320, 380), (1110, 560)]
H["s11"] = f"""
  <div class="num slab" id="s11num">3</div>
  <div class="eyebrow" id="s11eye" style="top:470px">One place for our data</div>
  <h2 class="slab title side" id="s11title">Five apps.<br>One question.</h2>
  {''.join(f'<div class="acard" id="{a}" style="left:{x}px;top:{y}px"><b>{n}</b>{f"<span>{s}</span>" if s else ""}</div>' for (a, n, s), (x, y) in zip(apps11, pos11))}"""

# S12: just ask
tabs = "".join(f'<i class="tab" id="tb{i}"></i>' for i in range(1, 6))
abars = "".join(f'<i class="dl" id="a12{i}" style="width:{w}px"></i>' for i, w in enumerate((420, 380, 440, 300, 400), 1))
H["s12"] = f"""
  <div class="eyebrow" id="s12eye">Once they’re connected, just ask</div>
  <div class="q" id="q1" style="top:320px">What did we decide in Tuesday’s meeting?</div>
  <div class="q" id="q2" style="top:440px">Who owns what?</div>
  <div class="q" id="q3" style="top:560px">Are our numbers on track this week?</div>
  <div class="answer" id="s12ans"><div class="tabs" id="s12tabs">{tabs}</div><div class="anshead"><span class="cmark xs">{inline(claude_svg, "claudemark")}</span>One answer</div>{abars}</div>"""

# S13: follow-through
tasks13 = [("f1", "Sunday’s reminder to the serve teams"), ("f2", "Meeting summary and who owes what"),
           ("f3", "A time next week for two busy leads"), ("f4", "Sermon notes into a small group guide")]
pos13 = [(860, 230), (1300, 230), (860, 470), (1300, 470)]
H["s13"] = f"""
  <div class="eyebrow" id="s13eye" style="top:400px">Everyday</div>
  <h2 class="slab title side" id="s13title" style="top:450px;width:560px">Follow-through.</h2>
  {''.join(f'<div class="fcard" id="{f}" style="left:{x}px;top:{y}px"><i class="fdot" id="{f}d"><svg viewBox="0 0 24 24" width="26" height="26"><path d="M5 12.5 L10 17 L19 7"/></svg></i><span>{t}</span></div>' for (f, t), (x, y) in zip(tasks13, pos13))}
  <div class="caught" id="s13caught">What used to slip gets caught.</div>"""

# S14: guardrails
rows14 = [("g1", "Asks before it sends, pays, or deletes anything", "tick"),
          ("g2", "A person reviews everything before it goes public", "tick"),
          ("g3", "Keep pastoral care, counseling and private information out", "stop"),
          ("g4", "Looks off or doesn’t sound like you? Fix it or ask.", "tick")]
def gicon(kind):
    if kind == "stop":
        return '<i class="gico stop"><svg viewBox="0 0 24 24" width="30" height="30"><circle cx="12" cy="12" r="8"/><path d="M6.5 17.5 L17.5 6.5"/></svg></i>'
    return '<i class="gico"><svg viewBox="0 0 24 24" width="30" height="30"><path d="M5 12.5 L10 17 L19 7"/></svg></i>'
H["s14"] = f"""
  <div id="s14a">
    <div class="eyebrow" id="s14eye">A few simple guardrails</div>
    <h2 class="slab hero" id="s14head"><span class="line">It drafts.</span><span class="line red" id="s14you">You decide.</span></h2>
  </div>
  <div id="s14b">
    <div class="eyebrow" id="s14beye" style="top:140px">Guardrails</div>
    {''.join(f'<div class="grow" id="{g}" style="top:{220 + i * 150}px">{gicon(k)}<span>{t}</span></div>' for i, (g, t, k) in enumerate(rows14))}
  </div>"""

# S15: invitation
H["s15"] = f"""
  <div id="s15a">
    <div class="eyebrow" id="s15eye">So here’s the invitation</div>
    <div class="sub15" id="s15sub">We’ll get each of you set up, with help along the way.</div>
    <h2 class="slab hero" id="s15head" style="top:380px">Start small.</h2>
    <div class="pick" id="s15p1">One task that eats your time</div>
    <svg class="wires" viewBox="0 0 1920 1080" width="1920" height="1080"><path class="wire solid" id="w151" d="M 712 640 L 792 640"/></svg>
    <div class="pick claude" id="s15p2"><span class="cmark xs">{inline(claude_svg, "claudemark")}</span>Claude takes the first pass</div>
  </div>
  <div id="s15b">
    <div class="slab big" id="s15l1">Less admin.</div>
    <div class="slab big red" id="s15l2">More time with people.</div>
  </div>"""

# S16: scripture
H["s16"] = """
  <div class="verse slab" id="s16v">“And whatever you do, do it <span class="red">heartily</span>,<br>as to the Lord and not to men.”</div>
  <div class="ref" id="s16ref">Colossians 3:23</div>"""

# S17: end card
H["s17"] = f"""
  <div id="s17logo">{inline(stack_svg, "stackmark")}</div>
  <div class="closer" id="s17text">Questions? Ask Danny or Isaiah.</div>
  <div class="footer" id="s17foot">risechurchtx.com</div>"""

scenes = "\n".join(
    f'    <section id="{sid}" class="clip scene" data-start="{st}" data-duration="{du}" data-track-index="1" data-track-kind="graphics">\n'
    f'      <div class="inner" id="{sid}i">{H[sid]}\n      </div>\n    </section>'
    for sid, st, du in SCENES)

def cap_span(n):
    a, b = TIMES[n - 1]
    nxt = TIMES[n][0] if n < len(TIMES) else b + 0.6
    end = min(b + 0.6, nxt)  # hold a beat after the words, never past the next line
    # keep each caption inside its scene
    for sid, st, du in SCENES:
        if st <= a < st + du:
            end = min(end, st + du - 0.05)
    return a, round(end, 2)

caps = "\n".join(
    f'    <div id="c{n}" class="clip cap" data-start="{cap_span(n)[0]}" data-duration="{round(cap_span(n)[1] - cap_span(n)[0], 2)}" data-track-index="2" data-track-kind="captions"><span class="captext" id="c{n}t">{CAPS[n - 1]}</span></div>'
    for n in range(1, len(CAPS) + 1) if n not in NO_CAPTION)

CSS = (pathlib.Path(__file__).parent / "staff.css").read_text()
JS = (pathlib.Path(__file__).parent / "staff.js").read_text()

def sub_cues(js):
    def rc(m):
        n = int(m.group(1)); w = m.group(2)
        return f"{cue(n, w):.3f}"
    js = re.sub(r'@c\((\d+)(?:,\s*"([^"]*)")?\)', rc, js)
    js = re.sub(r'@s\((s\d+)\)', lambda m: f"{SSTART[m.group(1)]:.3f}", js)
    js = re.sub(r'@e\((s\d+)\)', lambda m: f"{SEND[m.group(1)]:.3f}", js)
    js = js.replace("@TOTAL", f"{TOTAL:.3f}")
    assert "@" not in re.sub(r"//.*", "", js), "unreplaced cue"
    return js

voice = '    <audio id="voice" class="clip" src="assets/voice.m4a" data-start="0" data-track-index="3" data-volume="1"></audio>\n' if (proj / "assets/voice.m4a").exists() else ""
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
{voice}    </div>
    <script>{sub_cues(JS)}</script>
  </body>
</html>
"""
(proj / "index.html").write_text(html)
print("wrote", proj / "index.html", "total", TOTAL)
for sid, st, du in SCENES:
    print(sid, st, du)
