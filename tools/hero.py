#!/usr/bin/env python3
"""The hero picture for the public repository: the vobuda window, drawn in its
own palette. Dark and light, from one description."""

import pathlib

MONO = "ui-monospace, 'SF Mono', SFMono-Regular, Menlo, Consolas, monospace"
UI = "system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif"

DARK = dict(
    page="#0b0c0e", win="#17191d", bar="#232529", tab="#333539", term="#0f1115",
    fg="#d6d9de", dim="#8b9099", faint="#5d636c", line="#2f3135", accent="#90caf9",
    green="#66bb6a", blue="#42a5f5", magenta="#ab47bc", yellow="#ffca28",
    red="#ef5350", cyan="#26c6da", dock="#1c1f26", panel="#1b1e23", shadow="0.38",
)
LIGHT = dict(
    page="#eef0f3", win="#ffffff", bar="#e8e8e9", tab="#d6d6d7", term="#ffffff",
    fg="#1c1e21", dim="#6b7076", faint="#9aa0a6", line="#dbdbdb", accent="#1565c0",
    green="#2e7d32", blue="#1565c0", magenta="#7b1fa2", yellow="#a06a00",
    red="#c62828", cyan="#00838f", dock="#f2f2f3", panel="#fafafa", shadow="0.14",
)


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def text(x, y, s, fill, size=13, family=MONO, weight="400", anchor="start", opacity=None):
    o = f' opacity="{opacity}"' if opacity else ""
    return (f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" '
            f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}"{o} '
            f'xml:space="preserve">{esc(s)}</text>')


def draw(c):
    p = []
    W, H = 1600, 940
    p.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
             f'viewBox="0 0 {W} {H}" role="img" aria-label="The vobuda window: '
             'tabs, a terminal, an agent block with its control bar, the system '
             'monitor, and the dictation strip">')
    p.append('<defs>'
             '<filter id="sh" x="-20%" y="-20%" width="140%" height="150%">'
             f'<feDropShadow dx="0" dy="20" stdDeviation="30" flood-color="#000" flood-opacity="{c["shadow"]}"/>'
             '</filter>'
             f'<linearGradient id="spark" x1="0" y1="0" x2="0" y2="1">'
             f'<stop offset="0%" stop-color="{c["blue"]}" stop-opacity="0.5"/>'
             f'<stop offset="100%" stop-color="{c["blue"]}" stop-opacity="0"/>'
             '</linearGradient>'
             '<clipPath id="win"><rect x="60" y="50" width="1480" height="840" rx="14"/></clipPath>'
             '</defs>')
    p.append(f'<rect width="{W}" height="{H}" fill="{c["page"]}"/>')
    p.append(f'<rect x="60" y="50" width="1480" height="840" rx="14" fill="{c["win"]}" '
             f'stroke="{c["line"]}" filter="url(#sh)"/>')
    p.append('<g clip-path="url(#win)">')

    # ── tab bar ───────────────────────────────────────────────────────────
    p.append(f'<rect x="60" y="50" width="1480" height="46" fill="{c["bar"]}"/>')
    p.append(f'<line x1="60" y1="96" x2="1540" y2="96" stroke="{c["line"]}"/>')
    for i, col in enumerate(["#ff5f57", "#febc2e", "#28c840"]):
        p.append(f'<circle cx="{86 + i * 20}" cy="73" r="6" fill="{col}"/>')
    x = 176
    for name, active, badge in [("~/vobuda", True, None),
                                ("shifton-com", False, None),
                                ("release", False, c["yellow"])]:
        w = 154
        if active:
            p.append(f'<rect x="{x}" y="57" width="{w}" height="32" rx="7" fill="{c["tab"]}"/>')
        p.append(text(x + 16, 78, name, c["fg"] if active else c["dim"], 13, UI, "500"))
        if badge:
            p.append(f'<circle cx="{x + w - 18}" cy="73" r="4.5" fill="{badge}"/>')
        x += w + 6
    p.append(text(x + 14, 79, "+", c["faint"], 19, UI, "300"))

    # ── dock ──────────────────────────────────────────────────────────────
    p.append(f'<rect x="60" y="96" width="58" height="794" fill="{c["dock"]}"/>')
    p.append(f'<line x1="118" y1="96" x2="118" y2="890" stroke="{c["line"]}"/>')
    y = 136
    for kind in ["term", "files", "monitor", "agent", "voice", "gear"]:
        col = c["accent"] if kind == "term" else c["dim"]
        cx, cy = 89, y
        if kind == "term":
            p.append(f'<rect x="{cx-11}" y="{cy-9}" width="22" height="18" rx="4" fill="none" '
                     f'stroke="{col}" stroke-width="1.5"/>')
            p.append(f'<path d="M{cx-6} {cy-3.5} l3.5 3.5 -3.5 3.5" fill="none" stroke="{col}" '
                     'stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>')
            p.append(f'<line x1="{cx+1}" y1="{cy+3.5}" x2="{cx+6}" y2="{cy+3.5}" stroke="{col}" '
                     'stroke-width="1.5" stroke-linecap="round"/>')
        elif kind == "files":
            p.append(f'<path d="M{cx-10} {cy-9} h7 l3 4 h10 v14 h-20 z" fill="none" stroke="{col}" '
                     'stroke-width="1.5" stroke-linejoin="round"/>')
        elif kind == "monitor":
            for i, h in enumerate([6, 13, 9, 16]):
                p.append(f'<rect x="{cx-11+i*6}" y="{cy+8-h}" width="3.6" height="{h}" rx="1.6" fill="{col}"/>')
        elif kind == "agent":
            p.append(f'<path d="M{cx} {cy-10.5} l2.7 6.6 6.6 2.7 -6.6 2.7 -2.7 6.6 -2.7 -6.6 '
                     f'-6.6 -2.7 6.6 -2.7 z" fill="none" stroke="{col}" stroke-width="1.5" '
                     'stroke-linejoin="round"/>')
        elif kind == "voice":
            p.append(f'<rect x="{cx-4}" y="{cy-10}" width="8" height="12" rx="4" fill="none" '
                     f'stroke="{col}" stroke-width="1.5"/>')
            p.append(f'<path d="M{cx-7} {cy-0.5} a7 7 0 0 0 14 0" fill="none" stroke="{col}" '
                     'stroke-width="1.5" stroke-linecap="round"/>')
            p.append(f'<line x1="{cx}" y1="{cy+6.5}" x2="{cx}" y2="{cy+10}" stroke="{col}" '
                     'stroke-width="1.5" stroke-linecap="round"/>')
        else:
            p.append(f'<circle cx="{cx}" cy="{cy}" r="4" fill="none" stroke="{col}" stroke-width="1.5"/>')
            p.append(f'<circle cx="{cx}" cy="{cy}" r="9.5" fill="none" stroke="{col}" '
                     'stroke-width="1.5" stroke-dasharray="3.2 3.6"/>')
        y += 58

    # ── layout of the blocks ──────────────────────────────────────────────
    L, T = 134, 112                     # content origin
    GAP = 12
    left_w = 706
    right_x = L + left_w + GAP
    right_w = 1540 - 16 - right_x

    def block(x, y, w, h, title, active=False):
        out = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" fill="{c["term"]}" '
               f'stroke="{c["accent"] if active else c["line"]}" '
               f'stroke-opacity="{0.9 if active else 1}"/>',
               f'<path d="M{x} {y+30} h{w}" stroke="{c["line"]}"/>',
               text(x + 14, y + 20, title, c["dim"], 11.5, UI, "500"),
               text(x + w - 16, y + 21, "×", c["faint"], 14, UI, "400", "end")]
        return "".join(out)

    # terminal block
    th = 706
    p.append(block(L, T, left_w, th, "zsh — ~/vobuda", True))
    ty = T + 58
    lines = [
        [("gary", c["green"]), (" ~/vobuda ", c["blue"]), ("$ ", c["dim"]), ("npm run check", c["fg"])],
        [("  tsc --noEmit", c["dim"]), ("                 clean", c["green"])],
        [("  vitest", c["dim"]), ("                      1031 passed", c["green"])],
        [("  cargo test", c["dim"]), ("                   215 passed", c["green"])],
        [("  failure-modes.py", c["dim"]), ("             443 of 443 have a check", c["green"])],
        [("", c["fg"])],
        [("gary", c["green"]), (" ~/vobuda ", c["blue"]), ("$ ", c["dim"]), ("vobuda do block.split-down", c["fg"])],
        [("  the same name the key presses", c["faint"])],
        [("", c["fg"])],
        [("gary", c["green"]), (" ~/vobuda ", c["blue"]), ("$ ", c["dim"]), ("vobuda theme catppuccin-mocha", c["fg"])],
        [("  the window redraws; the file is yours to edit", c["faint"])],
        [("", c["fg"])],
        [("gary", c["green"]), (" ~/vobuda ", c["blue"]), ("$ ", c["dim"]), ("git log --oneline -3", c["fg"])],
        [("  56f96bd", c["yellow"]), (" 0.2.2 built, and the file every copy reads", c["fg"])],
        [("  4e2e4a9", c["yellow"]), (" a setting survives an update", c["fg"])],
        [("  a4f2934", c["yellow"]), (" the command-line check blamed the run", c["fg"])],
        [("", c["fg"])],
        [("gary", c["green"]), (" ~/vobuda ", c["blue"]), ("$ ", c["dim"]), ("./scripts/release.sh --mac", c["fg"])],
        [("  ▸ notarising vobuda-0.2.2-macos.dmg", c["dim"])],
        [("     status: ", c["dim"]), ("Accepted", c["green"]), ("  stapled", c["dim"])],
        [("", c["fg"])],
        [("gary", c["green"]), (" ~/vobuda ", c["blue"]), ("$ ", c["dim"])],
    ]
    for row in lines:
        cx = L + 16
        for s, col in row:
            p.append(text(cx, ty, s, col, 13.5))
            cx += len(s) * 8.12
        ty += 26
    p.append(f'<rect x="{L + 16 + 20 * 8.12}" y="{ty - 37}" width="8" height="16" fill="{c["accent"]}" opacity="0.9"/>')

    # agent block
    ah = 330
    p.append(block(right_x, T, right_w, ah, "Claude Code — ~/vobuda"))
    # control bar
    by = T + 42
    p.append(f'<rect x="{right_x + 12}" y="{by}" width="{right_w - 24}" height="34" rx="7" '
             f'fill="{c["panel"]}" stroke="{c["line"]}"/>')
    bx = right_x + 22
    for label, wide in [("Opus 5", 78), ("thinking", 88), ("Sessions", 88), ("Skills", 68), ("Attach", 70)]:
        p.append(f'<rect x="{bx}" y="{by + 7}" width="{wide}" height="20" rx="5" fill="{c["tab"]}"/>')
        p.append(text(bx + wide / 2 - 4, by + 21, label, c["fg"], 11, UI, "500", "middle"))
        p.append(f'<path d="M{bx + wide - 12} {by + 15} l3 3.4 3 -3.4" fill="none" stroke="{c["faint"]}" '
                 'stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"/>')
        bx += wide + 8
    p.append(f'<circle cx="{right_x + right_w - 30}" cy="{by + 17}" r="4.5" fill="{c["green"]}"/>')

    ay = by + 62
    for s, col, size in [
        ("● working — the strip names the language it hears", c["accent"], 12.5),
        ("", c["fg"], 12.5),
        ("  Added two letters to the voice strip and a check", c["fg"], 12.5),
        ("  that the migration touches nothing else.", c["fg"], 12.5),
        ("", c["fg"], 12.5),
        ("  src/voice.ts        letters(locale)", c["dim"], 12.5),
        ("  src/VoiceStrip.tsx  draws them", c["dim"], 12.5),
        ("  config.rs           FM-CONFIG-53", c["dim"], 12.5),
    ]:
        p.append(text(right_x + 18, ay, s, col, size))
        ay += 24

    # monitor block
    my = T + ah + GAP
    mh = th - ah - GAP
    p.append(block(right_x, my, right_w, mh, "monitor — istat"))
    px = right_x + 12
    pw = (right_w - 24 - 2 * 10) / 3
    card_h = 150
    for i, (title, big, sub) in enumerate([
        ("PROCESSOR", "18%", "user 11 · sys ≈7"),
        ("MEMORY", "21.4 GB", "of 32.0 GB"),
        ("NETWORK ADDRESS", "", ""),
    ]):
        bxp = px + i * (pw + 10)
        top = my + 42
        p.append(f'<rect x="{bxp}" y="{top}" width="{pw}" height="{card_h}" rx="7" '
                 f'fill="{c["panel"]}" stroke="{c["line"]}"/>')
        p.append(text(bxp + 12, top + 20, title, c["dim"], 9.5, UI, "600"))
        if title == "NETWORK ADDRESS":
            p.append(text(bxp + 12, top + 48, "203.0.113.42", c["fg"], 14.5, MONO, "500"))
            gx, gy = bxp + pw - 30, top + 36
            p.append(f'<rect x="{gx}" y="{gy}" width="9" height="11" rx="2" fill="none" '
                     f'stroke="{c["dim"]}" stroke-width="1.2"/>')
            p.append(f'<rect x="{gx + 3.5}" y="{gy + 3.5}" width="9" height="11" rx="2" fill="none" '
                     f'stroke="{c["dim"]}" stroke-width="1.2"/>')
            p.append(text(bxp + 12, top + 78, "on this network", c["faint"], 10, UI))
            p.append(text(bxp + 12, top + 100, "192.168.1.24", c["dim"], 13, MONO))
            gx, gy = bxp + pw - 30, top + 88
            p.append(f'<rect x="{gx}" y="{gy}" width="9" height="11" rx="2" fill="none" '
                     f'stroke="{c["dim"]}" stroke-width="1.2"/>')
            p.append(f'<rect x="{gx + 3.5}" y="{gy + 3.5}" width="9" height="11" rx="2" fill="none" '
                     f'stroke="{c["dim"]}" stroke-width="1.2"/>')
            p.append(text(bxp + 12, top + 130, "hostname  airgar.local", c["faint"], 10.5, UI))
        else:
            p.append(text(bxp + 12, top + 50, big, c["fg"], 21, MONO, "500"))
            p.append(text(bxp + 12, top + 70, sub, c["faint"], 10.5, UI))
            p.append(f'<rect x="{bxp + 12}" y="{top + 82}" width="{pw - 24}" height="6" rx="3" fill="{c["tab"]}"/>')
            frac = 0.18 if title == "PROCESSOR" else 0.67
            p.append(f'<rect x="{bxp + 12}" y="{top + 82}" width="{(pw - 24) * frac}" height="6" rx="3" '
                     f'fill="{c["blue"] if title == "PROCESSOR" else c["magenta"]}"/>')
            pts = ([12, 18, 14, 26, 41, 33, 22, 17, 24, 38, 52, 44, 31, 26, 19, 22, 30, 27, 21, 18]
                   if title == "PROCESSOR" else
                   [58, 60, 59, 62, 66, 64, 63, 67, 68, 66, 65, 67, 70, 68, 66, 67, 66, 68, 67, 67])
            base = top + card_h - 12
            w0 = (pw - 24) / (len(pts) - 1)
            colour = c["blue"] if title == "PROCESSOR" else c["magenta"]
            path = " ".join(
                f'{"M" if i == 0 else "L"}{bxp + 12 + i * w0:.1f} {base - v * 0.62:.1f}'
                for i, v in enumerate(pts))
            p.append(f'<path d="{path}" fill="none" stroke="{colour}" stroke-width="1.6" '
                     'stroke-linejoin="round"/>')
            if title == "PROCESSOR":
                p.append(f'<path d="{path} L{bxp + pw - 12:.1f} {base} L{bxp + 12} {base} Z" '
                         'fill="url(#spark)"/>')

    # processes, under the cards
    ly = my + 42 + card_h + 16
    p.append(text(right_x + 24, ly, "PROCESSES", c["dim"], 9.5, UI, "600"))
    p.append(text(right_x + right_w - 24, ly, "CPU", c["dim"], 9.5, UI, "600", "end"))
    ly += 20
    for name, cpu, col in [("node (vite)", "14.2", c["fg"]), ("cargo", "9.8", c["fg"]),
                           ("claude", "6.1", c["fg"]), ("vobuda", "2.4", c["fg"]),
                           ("WindowServer", "1.9", c["dim"])]:
        p.append(text(right_x + 24, ly, name, col, 12.5, MONO))
        p.append(text(right_x + right_w - 24, ly, cpu, c["dim"], 12.5, MONO, "400", "end"))
        ly += 23

    # ── voice strip ───────────────────────────────────────────────────────
    vy = T + th + GAP
    p.append(f'<rect x="{L}" y="{vy}" width="{1540 - 16 - L}" height="44" rx="9" '
             f'fill="{c["panel"]}" stroke="{c["line"]}"/>')
    p.append(f'<circle cx="{L + 22}" cy="{vy + 22}" r="5" fill="{c["red"]}"/>')
    p.append(text(L + 40, vy + 27, "listening", c["fg"], 12.5, UI, "500"))
    p.append(f'<rect x="{L + 110}" y="{vy + 13}" width="30" height="18" rx="4" '
             f'fill="{c["tab"]}"/>')
    p.append(text(L + 125, vy + 26, "RU", c["fg"], 10.5, UI, "600", "middle"))
    p.append(text(L + 152, vy + 27, "AirPods Max", c["dim"], 11.5, UI))
    p.append(text(L + 258, vy + 27, "открой настройки и найди диктовку", c["fg"], 12.5, MONO))
    p.append(text(1540 - 16 - 40, vy + 27, "typed into the block, never run", c["faint"], 11, UI, "400", "end"))

    p.append('</g>')
    p.append('</svg>')
    return "".join(p)


root = pathlib.Path("/Users/gary/Claude_memory/проекты/vobuda-public/assets")
(root / "hero.svg").write_text(draw(DARK))
(root / "hero-light.svg").write_text(draw(LIGHT))
print("hero.svg", (root / "hero.svg").stat().st_size, "bytes")
print("hero-light.svg", (root / "hero-light.svg").stat().st_size, "bytes")
