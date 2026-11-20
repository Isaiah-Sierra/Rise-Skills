const F = 1 / 30;
const tl = gsap.timeline({ paused: true });
const ft = (s, a, b, t) => tl.fromTo(s, a, b, t);
const to = (s, v, t) => tl.to(s, v, t);
// Scene exit: lift and fade, then hard-kill at the boundary.
const leave = (sel, end, d) => { d = d || 8 * F; to(sel, { opacity: 0, y: -24, duration: d, ease: "power2.in" }, end - d - 2 * F); tl.set(sel, { opacity: 0 }, end); };
const wipe = (sel, t) => ft(sel, { clipPath: "inset(0 100% 0 0)" }, { clipPath: "inset(0 0% 0 0)", duration: 14 * F, ease: "power3.out" }, t);
const press = (sel, t) => { to(sel, { scale: 0.95, duration: 4 * F, ease: "power2.in" }, t); to(sel, { scale: 1, duration: 10 * F, ease: "back.out(2.6)" }, t + 4 * F); };
const pulse = (sel, t) => { to(sel, { scale: 1.07, duration: 6 * F, ease: "power1.out" }, t); to(sel, { scale: 1, duration: 12 * F, ease: "power1.inOut" }, t + 6 * F); };
function opener(id, t) {
  ft(id + "num", { y: 50, opacity: 0 }, { y: 0, opacity: 1, duration: 18 * F, ease: "power4.out" }, t);
  wipe(id + "eye", t + 6 * F);
  ft(id + "title", { y: 30, opacity: 0 }, { y: 0, opacity: 1, duration: 16 * F, ease: "power3.out" }, t + 10 * F);
}

// Background: the Rise weighted circle drifts slowly the whole film.
to("#bgring", { scale: 1.06, x: -60, y: 30, rotation: 8, duration: @TOTAL - 0.4, ease: "sine.inOut" }, 0.2);

// S1 intro. Frame 0 shows the eyebrow (thumbnail).
ft("#s1head .w", { y: 46, opacity: 0 }, { y: 0, opacity: 1, duration: 18 * F, ease: "back.out(1.7)", stagger: 3 * F }, 0.25);
ft("#s1cm", { scale: 0.9, opacity: 0, rotation: -30 }, { scale: 1, opacity: 1, rotation: 0, duration: 20 * F, ease: "circ.out" }, @c(1, "Claude") - 0.4);
ft("#s1ul", { scaleX: 0 }, { scaleX: 1, duration: 20 * F, ease: "expo.out" }, @c(1, "Claude"));
to("#s1head, #s1eye", { opacity: 0, x: -40, duration: 9 * F, ease: "power2.in" }, @c(2) - 10 * F);
tl.set("#s1head, #s1eye", { opacity: 0 }, @c(2));
wipe("#s1beye", @c(2));
ft("#ag1", { x: -50, opacity: 0 }, { x: 0, opacity: 1, duration: 14 * F, ease: "power3.out" }, Math.min(@c(2, "what it is") - 3 * F, @c(2) + 0.5));
ft("#ag2", { x: -50, opacity: 0 }, { x: 0, opacity: 1, duration: 14 * F, ease: "power3.out" }, @c(2, "how it works") - 3 * F);
ft("#ag3", { x: -50, opacity: 0 }, { x: 0, opacity: 1, duration: 14 * F, ease: "power3.out" }, @c(3, "give us") - 3 * F);
ft("#s1people", { scale: 0.92, opacity: 0, y: 30 }, { scale: 1, opacity: 1, y: 0, duration: 18 * F, ease: "back.out(1.7)" }, @c(3, "people") - 3 * F);
leave("#s1i", @e(s1));

// S2 what it is
wipe("#s2eye", @s(s2) + 0.2);
ft("#s2cm", { scale: 0.92, opacity: 0 }, { scale: 1, opacity: 1, duration: 16 * F, ease: "circ.out" }, @s(s2) + 0.3);
ft("#s2wm", { x: -30, opacity: 0 }, { x: 0, opacity: 1, duration: 16 * F, ease: "power4.out" }, @s(s2) + 0.3 + 4 * F);
ft("#s2sub", { y: 24, opacity: 0 }, { y: 0, opacity: 1, duration: 14 * F, ease: "power3.out" }, @c(4, "made by") - 3 * F);
ft("#s2anth", { scale: 0.94, opacity: 0 }, { scale: 1, opacity: 1, duration: 12 * F, ease: "back.out(1.7)" }, @c(4, "Anthropic") - 2 * F);
ft("#s2bub", { y: 30, scale: 0.95, opacity: 0, transformOrigin: "right bottom" }, { y: 0, scale: 1, opacity: 1, duration: 16 * F, ease: "back.out(1.7)" }, @c(5) - 3 * F);
ft("#s2bcap", { opacity: 0 }, { opacity: 1, duration: 12 * F, ease: "power1.out" }, @c(5, "the way"));
[@c(6, "read"), @c(6, "write"), @c(6, "summarize"), @c(6, "plan"), @c(6, "organize")].forEach((t, i) => {
  ft("#v" + (i + 1), { y: 30, opacity: 0 }, { y: 0, opacity: 1, duration: 12 * F, ease: i % 2 ? "power3.out" : "back.out(1.7)" }, t - 3 * F);
});
to("#s2a", { opacity: 0, y: -24, duration: 8 * F, ease: "power2.in" }, @c(7) - 10 * F);
tl.set("#s2a", { opacity: 0 }, @c(7));
wipe("#s2beye", @c(7));
ft("#s2l1", { y: 40, opacity: 0 }, { y: 0, opacity: 1, duration: 18 * F, ease: "expo.out" }, @c(7, "your judgment") - 3 * F);
ft("#s2l2", { y: 40, opacity: 0 }, { y: 0, opacity: 1, duration: 18 * F, ease: "expo.out" }, @c(7, "your calling") - 3 * F);
ft("#s2dec", { x: -30, opacity: 0 }, { x: 0, opacity: 1, duration: 14 * F, ease: "power2.out" }, @c(8) - 3 * F);
pulse("#s2you", @c(8, "decides") - 3 * F);
leave("#s2i", @e(s2));

// S3 how it works: the sentence writes itself one word at a time (signature moment 1)
wipe("#s3eye", @s(s3) + 0.15);
ft("#s3title", { y: 36, opacity: 0 }, { y: 0, opacity: 1, duration: 18 * F, ease: "power4.out" }, @s(s3) + 0.3);
ft("#s3sub", { opacity: 0, y: 16 }, { opacity: 1, y: 0, duration: 14 * F, ease: "sine.out" }, @c(10) - 3 * F);
ft("#s3lib .libl", { scaleX: 0 }, { scaleX: 1, duration: 16 * F, ease: "circ.out", stagger: 2 * F }, @c(10) + 0.2);
to("#s3lib", { opacity: 0, duration: 10 * F, ease: "power1.in" }, @c(11) - 10 * F);
tl.set("#s3lib", { opacity: 0 }, @c(11));
ft("#s3panel", { x: 70, opacity: 0 }, { x: 0, opacity: 1, duration: 20 * F, ease: "expo.out" }, @c(11) - 4 * F);
ft("#s3ask", { y: 26, scale: 0.95, opacity: 0, transformOrigin: "right bottom" }, { y: 0, scale: 1, opacity: 1, duration: 14 * F, ease: "back.out(1.7)" }, @c(11) + 4 * F);
ft("#s3gen .gw", { opacity: 0, y: 8 }, { opacity: 1, y: 0, duration: 3 * F, ease: "none", stagger: 5 * F }, @c(11, "one word") - 0.2);
ft("#s3caret", { opacity: 0 }, { opacity: 1, duration: 2 * F, ease: "none" }, @c(11, "one word") - 0.3);
ft("#s3t1", { scale: 0.9, opacity: 0 }, { scale: 1, opacity: 1, duration: 10 * F, ease: "back.out(2.6)" }, @c(12, "first drafts") - 3 * F);
ft("#s3t2", { scale: 0.9, opacity: 0 }, { scale: 1, opacity: 1, duration: 10 * F, ease: "back.out(2.6)" }, @c(12, "summaries") - 3 * F);
ft("#s3t3", { x: 24, opacity: 0 }, { x: 0, opacity: 1, duration: 12 * F, ease: "power3.out" }, @c(13, "confidently") - 3 * F);
pulse("#s3t3", @c(13, "wrong"));
leave("#s3i", @e(s3));

// S4 check its work
wipe("#s4eye", @s(s4) + 0.15);
ft("#s4title", { y: 30, opacity: 0 }, { y: 0, opacity: 1, duration: 16 * F, ease: "back.out(1.7)" }, @s(s4) + 0.3);
ft("#s4card", { y: 50, opacity: 0 }, { y: 0, opacity: 1, duration: 18 * F, ease: "power3.out" }, @s(s4) + 0.4);
[@c(14, "names"), @c(14, "dates"), @c(14, "numbers"), @c(14, "scripture")].forEach((t, i) => {
  ft("#k" + (i + 1), { x: 30, opacity: 0 }, { x: 0, opacity: 1, duration: 12 * F, ease: "power2.out" }, t - 4 * F);
  ft("#tk" + (i + 1), { scale: 0.8 }, { scale: 1, duration: 10 * F, ease: "back.out(2.6)" }, t);
});
leave("#s4i", @e(s4));

// S5 layers (signature moment 2): rings wrap the Claude mark
wipe("#s5eye", @s(s5) + 0.15);
ft("#s5hub", { scale: 0.9, opacity: 0 }, { scale: 1, opacity: 1, duration: 18 * F, ease: "back.out(1.7)" }, @s(s5) + 0.3);
ft("#s5title", { y: 36, opacity: 0 }, { y: 0, opacity: 1, duration: 18 * F, ease: "power4.out" }, @c(16) - 3 * F);
[["#rg1", 0], ["#rg2", 1], ["#rg3", 2]].forEach(([r, i]) => {
  ft(r, { scale: 0.6, opacity: 0 }, { scale: 1, opacity: 1, duration: 22 * F, ease: "expo.out" }, @c(16, "wrapped") + i * 6 * F);
});
ft("#s5rings .rlab", { y: 16, opacity: 0 }, { y: 0, opacity: 1, duration: 12 * F, ease: "power3.out", stagger: 5 * F }, @c(16, "organization") );
ft("#s5three", { x: -30, opacity: 0 }, { x: 0, opacity: 1, duration: 14 * F, ease: "power2.out" }, @c(17) - 3 * F);
pulse("#s5rings", @c(17, "three"));
to("#s5rings", { rotation: 6, duration: @e(s5) - @s(s5) - 0.5, ease: "sine.inOut" }, @s(s5) + 0.3);
leave("#s5i", @e(s5));

// S6 three things
ft("#tr1", { y: 34, opacity: 0 }, { y: 0, opacity: 1, duration: 16 * F, ease: "power4.out" }, @s(s6) + 0.2);
ft("#tr2", { y: 34, opacity: 0 }, { y: 0, opacity: 1, duration: 16 * F, ease: "power4.out" }, @c(19) - 3 * F);
ft("#s6apps .app", { x: 40, opacity: 0 }, { x: 0, opacity: 1, duration: 12 * F, ease: "back.out(1.7)", stagger: 4 * F }, @c(19, "Gmail") - 3 * F);
ft("#tr2sub", { clipPath: "inset(0 100% 0 0)" }, { clipPath: "inset(0 0% 0 0)", duration: 16 * F, ease: "power2.inOut" }, @c(20, "not a back") - 3 * F);
ft("#tr3", { y: 34, opacity: 0 }, { y: 0, opacity: 1, duration: 16 * F, ease: "power4.out" }, @c(21) - 3 * F);
tl.set("#tr2sub", { clipPath: "inset(0 100% 0 0)" }, 0);
leave("#s6i", @e(s6));

// S7 Claude Duet
wipe("#s7eye", @s(s7) + 0.2);
ft("#s7title", { y: 36, opacity: 0 }, { y: 0, opacity: 1, duration: 18 * F, ease: "power4.out" }, @c(22, "chief") - 6 * F);
ft("#s7hub", { scale: 0.9, opacity: 0 }, { scale: 1, opacity: 1, duration: 18 * F, ease: "back.out(1.7)" }, @s(s7) + 0.4);
ft("#s7plate", { x: -30, opacity: 0 }, { x: 0, opacity: 1, duration: 14 * F, ease: "power3.out" }, @c(23, "keeps track") - 3 * F);
[[1, @c(24, "morning")], [2, @c(24, "check-ins")], [3, @c(25, "tasks")], [4, @c(26, "Bigger")], [5, @c(27, "learns")]].forEach(([i, t]) => {
  ft("#w7" + i, { strokeDasharray: 320, strokeDashoffset: 320 }, { strokeDashoffset: 0, duration: 14 * F, ease: "expo.out" }, t - 6 * F);
  ft("#o7" + i, { x: 50, opacity: 0 }, { x: 0, opacity: 1, duration: 14 * F, ease: "power2.out" }, t - 2 * F);
});
pulse("#s7hub", @c(26, "background"));
leave("#s7i", @e(s7));

// S8 proposals
wipe("#s8eye0", @s(s8) + 0.15);
ft("#s8head", { y: 50, opacity: 0 }, { y: 0, opacity: 1, duration: 18 * F, ease: "back.out(1.7)" }, @s(s8) + 0.3);
to("#s8a", { opacity: 0, y: -24, duration: 8 * F, ease: "power2.in" }, @c(28, "Start") - 10 * F);
tl.set("#s8a", { opacity: 0 }, @c(28, "Start"));
opener("#s8", @c(28, "Start"));
ft("#i81", { x: 40, opacity: 0 }, { x: 0, opacity: 1, duration: 12 * F, ease: "power3.out" }, @c(29, "ministry") - 3 * F);
ft("#i82", { x: 40, opacity: 0 }, { x: 0, opacity: 1, duration: 12 * F, ease: "power3.out" }, @c(29, "event") - 3 * F);
ft("#i83", { x: 40, opacity: 0 }, { x: 0, opacity: 1, duration: 12 * F, ease: "power3.out" }, @c(29, "request") - 3 * F);
ft("#s8blank", { scale: 0.94, opacity: 0 }, { scale: 1, opacity: 0.5, duration: 16 * F, ease: "sine.out" }, @c(30, "blank") - 3 * F);
to("#s8ideas", { opacity: 0, x: -30, duration: 8 * F, ease: "power2.in" }, @c(31) - 10 * F);
tl.set("#s8ideas", { opacity: 0 }, @c(31));
ft("#t81", { y: 34, opacity: 0 }, { y: 0, opacity: 1, duration: 16 * F, ease: "power3.out" }, @c(31, "notes") - 3 * F);
ft("#t82", { y: 34, opacity: 0 }, { y: 0, opacity: 1, duration: 16 * F, ease: "power3.out" }, @c(31, "goals") - 3 * F);
ft("#w81, #w82", { strokeDasharray: 300, strokeDashoffset: 300 }, { strokeDashoffset: 0, duration: 16 * F, ease: "expo.out", stagger: 2 * F }, @c(31, "you get") - 3 * F);
ft("#s8doc", { scale: 0.94, opacity: 0, transformOrigin: "center center" }, { scale: 1, opacity: 1, duration: 20 * F, ease: "expo.out" }, @c(31, "solid") - 3 * F);
ft("#s8doc .dl", { scaleX: 0 }, { scaleX: 1, duration: 12 * F, ease: "circ.out", stagger: 3 * F }, @c(31, "solid") + 0.2);
ft("#s8mark", { scaleX: 0 }, { scaleX: 1, duration: 18 * F, ease: "power2.inOut" }, @c(32, "making"));
ft("#s8right", { y: 16, opacity: 0 }, { y: 0, opacity: 1, duration: 12 * F, ease: "power4.out" }, @c(32, "making") + 4 * F);
leave("#s8i", @e(s8));

// S9 standardization: three mismatched docs snap onto the Rise template
opener("#s9", @s(s9) + 0.2);
const messy = [[900, 310, -7, "#3C4247"], [1170, 270, 5, "#12AEAB"], [1440, 330, -3, "#26334A"]];
const neat = [[900, 300], [1180, 300], [1460, 300]];
messy.forEach(([x, y, r, c], i) => {
  tl.set("#sd" + (i + 1), { x: x, y: y, rotation: r }, 0);
  tl.set("#sb" + (i + 1), { backgroundColor: c, scaleX: 0.55 + i * 0.15 }, 0);
  tl.set("#sl" + (i + 1), { opacity: 0 }, 0);
  ft("#sd" + (i + 1), { opacity: 0, scale: 0.93 }, { opacity: 1, scale: 1, duration: 12 * F, ease: "power2.out" }, [@c(34, "memo"), @c(34, "plan,"), @c(34, "handout")][i] - 3 * F);
});
ft("#s9fix", { opacity: 0, y: 14 }, { opacity: 1, y: 0, duration: 12 * F, ease: "sine.out" }, @c(35, "fixing") - 3 * F);
to("#s9fix", { opacity: 0, duration: 6 * F, ease: "power1.in" }, @c(36) - 6 * F);
tl.set("#s9fix", { opacity: 0 }, @c(36));
neat.forEach(([x, y], i) => {
  to("#sd" + (i + 1), { x: x, y: y, rotation: 0, duration: 18 * F, ease: "power3.inOut" }, @c(36, "Rise") + i * 3 * F);
  to("#sb" + (i + 1), { backgroundColor: "#EC0044", scaleX: 1, duration: 14 * F, ease: "power2.out" }, @c(36, "Rise") + 10 * F + i * 3 * F);
  to("#sl" + (i + 1), { opacity: 1, duration: 10 * F, ease: "power1.out" }, @c(36, "Rise") + 12 * F + i * 3 * F);
});
ft("#s9tpl", { clipPath: "inset(0 100% 0 0)" }, { clipPath: "inset(0 0% 0 0)", duration: 16 * F, ease: "power3.out" }, @c(36, "templates"));
tl.set("#s9tpl", { clipPath: "inset(0 100% 0 0)" }, 0);
[1, 2, 3].forEach((i) => pulse("#sd" + i, @c(37, "same look") + (i - 1) * 3 * F));
leave("#s9i", @e(s9));

// S10 AI folder
wipe("#s10eye", @s(s10) + 0.15);
ft("#s10title", { y: 36, opacity: 0 }, { y: 0, opacity: 1, duration: 18 * F, ease: "back.out(1.7)" }, @s(s10) + 0.3);
ft("#s10folder", { y: 40, opacity: 0 }, { y: 0, opacity: 1, duration: 18 * F, ease: "expo.out" }, @c(38, "AI folder") - 4 * F);
ft("#fi1", { y: 120, opacity: 0 }, { y: 0, opacity: 1, duration: 16 * F, ease: "back.out(1.7)" }, @c(38, "style") - 3 * F);
ft("#fi2", { y: 120, opacity: 0 }, { y: 0, opacity: 1, duration: 16 * F, ease: "back.out(1.7)" }, @c(38, "templates") - 3 * F);
ft("#s10sub", { opacity: 0 }, { opacity: 1, duration: 12 * F, ease: "power1.out" }, @c(38, "templates") + 0.3);
ft("#w101", { strokeDasharray: 260, strokeDashoffset: 260 }, { strokeDashoffset: 0, duration: 14 * F, ease: "expo.out" }, @c(39, "Claude project") - 6 * F);
ft("#de1", { x: 40, opacity: 0 }, { x: 0, opacity: 1, duration: 14 * F, ease: "power3.out" }, @c(39, "Claude project") - 2 * F);
ft("#w102", { strokeDasharray: 260, strokeDashoffset: 260 }, { strokeDashoffset: 0, duration: 14 * F, ease: "expo.out" }, @c(39, "memory") - 6 * F);
ft("#de2", { x: 40, opacity: 0 }, { x: 0, opacity: 1, duration: 14 * F, ease: "power3.out" }, @c(39, "memory") - 2 * F);
press("#s10folder", @c(39, "right from"));
ft("#s10one", { y: 30, opacity: 0 }, { y: 0, opacity: 1, duration: 16 * F, ease: "power4.out" }, @c(40, "less rework") - 3 * F);
leave("#s10i", @e(s10));

// S11 five apps
opener("#s11", @s(s11) + 0.2);
[["#ap11", @c(43, "Fellow")], ["#ap12", @c(44, "Ninety")], ["#ap13", @c(45, "email")], ["#ap14", @c(45, "calendar")], ["#ap15", @c(45, "Planning")]].forEach(([a, t], i) => {
  ft(a, { y: 30, scale: 0.95, opacity: 0 }, { y: 0, scale: 1, opacity: 1, duration: 14 * F, ease: i % 2 ? "power3.out" : "back.out(1.7)" }, t - 4 * F);
});
leave("#s11i", @e(s11));

// S12 just ask: questions, then tabs collapse into one answer
wipe("#s12eye", @s(s12) + 0.15);
ft("#s12ans", { x: 60, opacity: 0 }, { x: 0, opacity: 1, duration: 18 * F, ease: "expo.out" }, @s(s12) + 0.4);
[0, 1, 2, 3, 4].forEach((i) => tl.set("#tb" + (i + 1), { x: i * 92, backgroundColor: "#E7E4EA" }, 0));
ft("#s12tabs .tab", { y: 20, opacity: 0 }, { y: 0, opacity: 1, duration: 10 * F, ease: "power2.out", stagger: 2 * F }, @s(s12) + 0.6);
ft("#q1", { y: 26, scale: 0.96, opacity: 0, transformOrigin: "left bottom" }, { y: 0, scale: 1, opacity: 1, duration: 14 * F, ease: "back.out(1.7)" }, @c(47) - 3 * F);
ft("#q2", { y: 26, scale: 0.96, opacity: 0, transformOrigin: "left bottom" }, { y: 0, scale: 1, opacity: 1, duration: 14 * F, ease: "back.out(1.7)" }, @c(47, "Who owns") - 3 * F);
ft("#q3", { y: 26, scale: 0.96, opacity: 0, transformOrigin: "left bottom" }, { y: 0, scale: 1, opacity: 1, duration: 14 * F, ease: "back.out(1.7)" }, @c(48) - 3 * F);
[0, 1, 2, 3, 4].forEach((i) => to("#tb" + (i + 1), { x: 0, duration: 16 * F, ease: "power3.inOut" }, @c(49, "one answer") - 6 * F + (4 - i) * 2 * F));
to("#tb1", { backgroundColor: "#FFFFFF", duration: 8 * F, ease: "power1.out" }, @c(49, "one answer") + 0.3);
ft("#s12ans .dl", { scaleX: 0 }, { scaleX: 1, duration: 12 * F, ease: "circ.out", stagger: 3 * F }, @c(49, "one answer"));
to("#q1, #q2, #q3", { opacity: 0.35, duration: 12 * F, ease: "sine.inOut" }, @c(50, "jumping"));
pulse("#s12ans", @c(50, "piece"));
leave("#s12i", @e(s12));

// S13 follow-through
wipe("#s13eye", @s(s13) + 0.15);
ft("#s13title", { y: 30, opacity: 0 }, { y: 0, opacity: 1, duration: 16 * F, ease: "power4.out" }, @s(s13) + 0.3);
[["#f1", @c(52, "draft")], ["#f2", @c(53)], ["#f3", @c(54, "Find a time")], ["#f4", @c(54, "sermon")]].forEach(([f, t], i) => {
  ft(f, { y: 36, opacity: 0 }, { y: 0, opacity: 1, duration: 14 * F, ease: i % 2 ? "expo.out" : "power3.out" }, t - 3 * F);
  tl.set(f + "d", { scale: 0.6, backgroundColor: "#E7E4EA" }, 0);
  to(f + "d", { scale: 1, backgroundColor: "#12AEAB", duration: 10 * F, ease: "back.out(2.6)" }, @c(55) + i * 4 * F);
});
ft("#s13caught", { clipPath: "inset(0 100% 0 0)" }, { clipPath: "inset(0 0% 0 0)", duration: 18 * F, ease: "power2.inOut" }, @c(55) - 3 * F);
tl.set("#s13caught", { clipPath: "inset(0 100% 0 0)" }, 0);
leave("#s13i", @e(s13));

// S14 guardrails
wipe("#s14eye", @s(s14) + 0.15);
wipe("#s14beye", @c(58) - 6 * F);
ft("#s14head .line", { y: 50, opacity: 0 }, { y: 0, opacity: 1, duration: 18 * F, ease: "back.out(1.7)", stagger: 12 * F }, @c(57) - 3 * F);
press("#s14you", @c(57, "decide"));
to("#s14a", { opacity: 0, y: -24, duration: 8 * F, ease: "power2.in" }, @c(58) - 10 * F);
tl.set("#s14a", { opacity: 0 }, @c(58));
[["#g1", @c(58)], ["#g2", @c(59)], ["#g3", @c(60)], ["#g4", @c(61)]].forEach(([g, t], i) => {
  ft(g, { x: -40, opacity: 0 }, { x: 0, opacity: 1, duration: 14 * F, ease: i === 2 ? "expo.out" : "power3.out" }, t - 3 * F);
  ft(g + " .gico", { scale: 0.8 }, { scale: 1, duration: 10 * F, ease: "back.out(2.6)" }, t);
});
leave("#s14i", @e(s14));

// S15 invitation
wipe("#s15eye", @s(s15) + 0.15);
ft("#s15sub", { y: 20, opacity: 0 }, { y: 0, opacity: 1, duration: 14 * F, ease: "power3.out" }, @c(63) - 3 * F);
ft("#s15head", { y: 50, opacity: 0 }, { y: 0, opacity: 1, duration: 18 * F, ease: "back.out(1.7)" }, @c(64, "start small") - 3 * F);
ft("#s15p1", { x: 40, opacity: 0 }, { x: 0, opacity: 1, duration: 14 * F, ease: "power3.out" }, @c(65, "one task") - 3 * F);
ft("#w151", { strokeDasharray: 90, strokeDashoffset: 90 }, { strokeDashoffset: 0, duration: 12 * F, ease: "expo.out" }, @c(65, "let Claude") - 6 * F);
ft("#s15p2", { x: 40, opacity: 0 }, { x: 0, opacity: 1, duration: 14 * F, ease: "back.out(1.7)" }, @c(65, "let Claude") - 2 * F);
to("#s15a", { opacity: 0, y: -24, duration: 8 * F, ease: "power2.in" }, @c(66) - 10 * F);
tl.set("#s15a", { opacity: 0 }, @c(66));
ft("#s15l1", { y: 50, opacity: 0 }, { y: 0, opacity: 1, duration: 18 * F, ease: "power4.out" }, @c(67, "admin") - 3 * F);
ft("#s15l2", { y: 50, opacity: 0 }, { y: 0, opacity: 1, duration: 18 * F, ease: "back.out(1.7)" }, @c(67, "with people") - 6 * F);
leave("#s15i", @e(s15));

// S16 scripture
ft("#s16v", { y: 30, opacity: 0 }, { y: 0, opacity: 1, duration: 24 * F, ease: "sine.out" }, @s(s16) + 0.25);
ft("#s16ref", { letterSpacing: "0.4em", opacity: 0 }, { letterSpacing: "0.22em", opacity: 1, duration: 20 * F, ease: "power2.out" }, @c(69) - 4 * F);
leave("#s16i", @e(s16), 10 * F);

// S17 end card
ft("#s17logo", { scale: 0.94, opacity: 0, transformOrigin: "center bottom" }, { scale: 1, opacity: 1, duration: 24 * F, ease: "expo.out" }, @s(s17) + 0.2);
ft("#s17text", { y: 30, opacity: 0 }, { y: 0, opacity: 1, duration: 18 * F, ease: "power3.out" }, @s(s17) + 0.5);
ft("#s17foot", { opacity: 0 }, { opacity: 1, duration: 14 * F, ease: "power1.out" }, @s(s17) + 1.2);

// Captions: each line rises in, then cuts to the next.
document.querySelectorAll(".captext").forEach((el) => {
  const start = parseFloat(el.parentElement.dataset.start);
  tl.fromTo(el, { y: 10, opacity: 0 }, { y: 0, opacity: 1, duration: 6 * F, ease: "power2.out" }, start + 2 * F);
});

window.__timelines["main"] = tl;
tl.seek(0);
