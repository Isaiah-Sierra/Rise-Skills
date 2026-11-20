#!/usr/bin/env python3
"""Estimate caption [start, end] times from a voice file and the caption list in gen_staff.py.

Speech is split by ffmpeg silencedetect; caption boundaries are placed proportionally to their
character counts across the speech time, then snapped to the nearest pause. Writes JSON.
usage: align.py voice.m4a out.json [noise_db] [min_pause]
"""
import json, re, subprocess, sys, pathlib, importlib.util

voice, out = sys.argv[1], sys.argv[2]
noise = sys.argv[3] if len(sys.argv) > 3 else "-35dB"
dmin = sys.argv[4] if len(sys.argv) > 4 else "0.25"

src = pathlib.Path(__file__).with_name("gen_staff.py").read_text()
caps_src = src[src.index("CAPS = ["):src.index("]\nNO_CAPTION")] + "]"
ns = {}; exec(caps_src, ns); CAPS = ns["CAPS"]

dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", voice],
                           capture_output=True, text=True).stdout)
log = subprocess.run(["ffmpeg", "-i", voice, "-af", f"silencedetect=n={noise}:d={dmin}", "-f", "null", "-"],
                     capture_output=True, text=True).stderr
starts = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", log)]
ends = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", log)]
sil = list(zip(starts, ends + [dur] * (len(starts) - len(ends))))
# speech segments
segs, t = [], 0.0
for a, b in sil:
    if a > t + 0.05:
        segs.append((t, a))
    t = b
if t < dur - 0.05:
    segs.append((t, dur))
speech = sum(b - a for a, b in segs)

def speech_to_real(x):
    acc = 0.0
    for a, b in segs:
        if x <= acc + (b - a):
            return a + (x - acc)
        acc += b - a
    return segs[-1][1]

# Paragraph breaks (pauses of 0.75 s or more) anchor these captions; align inside each block.
ANCHORS = [1, 4, 9, 15, 22, 28, 33, 41, 51, 56, 62, 68]
long_p = [b for a, b in sil if (b - a) >= 0.75 and b < dur - 0.05]
long_p = [segs[0][0]] + [x for x in long_p if x > segs[0][0] + 0.5]
assert len(long_p) == len(ANCHORS), (len(long_p), len(ANCHORS), long_p)
pauses = [((a + b) / 2, a, b) for a, b in sil if a > 0.05 and b < dur - 0.05]
times = []
for k, first in enumerate(ANCHORS):
    last = ANCHORS[k + 1] - 1 if k + 1 < len(ANCHORS) else len(CAPS)
    t0 = long_p[k]
    t1 = ([a for a, b in sil if abs(b - long_p[k + 1]) < 1e-6][0] if k + 1 < len(ANCHORS) else segs[-1][1])
    bsegs = [(max(a, t0), min(b, t1)) for a, b in segs if b > t0 and a < t1]
    sp = sum(b - a for a, b in bsegs)
    def s2r(x):
        acc = 0.0
        for a, b in bsegs:
            if x <= acc + (b - a): return a + (x - acc)
            acc += b - a
        return bsegs[-1][1]
    idx = list(range(first, last + 1))
    w = [len(CAPS[i - 1]) + 6 for i in idx]
    tot = sum(w)
    raw = [s2r(sum(w[:j]) / tot * sp) for j in range(len(idx) + 1)]
    cand = [p for p in pauses if t0 + 0.3 < p[0] < t1 - 0.3]
    bounds = [(t0, t0, t0)]
    used = set()
    for x in raw[1:-1]:
        best = min(((abs(m - x), i) for i, (m, a, b) in enumerate(cand) if i not in used), default=None)
        if best and best[0] < 1.2:
            used.add(best[1]); bounds.append(cand[best[1]])
        else:
            bounds.append((x, x, x))
    bounds.append((t1, t1, t1))
    for j in range(len(idx)):
        times.append([round(bounds[j][2], 2), round(bounds[j + 1][1], 2)])
for i in range(1, len(times)):  # keep order
    times[i][0] = max(times[i][0], times[i - 1][0] + 0.3)
json.dump(times, open(out, "w"))
print(f"duration {dur:.2f}s, speech {speech:.1f}s, {len(sil)} pauses")
for c, (a, b) in zip(CAPS, times):
    print(f"{a:7.2f} {b:7.2f}  {c[:60]}")
