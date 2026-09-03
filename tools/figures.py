#!/usr/bin/env python3
"""The rest of the pictures for the page: what the program actually offers.

One description, two themes. Everything on them is English and belongs to
nobody: no home folders, no machine names, no device a person owns.
"""

import pathlib

MONO = "ui-monospace, 'SF Mono', SFMono-Regular, Menlo, Consolas, monospace"
UI = "system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif"

DARK = dict(
    page="#0b0c0e", win="#17191d", bar="#232529", tab="#333539", term="#0f1115",
    fg="#d6d9de", dim="#8b9099", faint="#5d636c", line="#2f3135", accent="#90caf9",
    green="#66bb6a", blue="#42a5f5", magenta="#ab47bc", yellow="#ffca28", red="#ef5350",
    cyan="#26c6da", menu="#1f2226", hover="#2a2d33", panel="#1b1e23", shadow="0.45",
)
LIGHT = dict(
    page="#eef0f3", win="#ffffff", bar="#f1f1f2", tab="#e2e2e3", term="#ffffff",
    fg="#1c1e21", dim="#6b7076", faint="#9aa0a6", line="#dbdbdb", accent="#1565c0",
    green="#2e7d32", blue="#1565c0", magenta="#7b1fa2", yellow="#a06a00", red="#c62828",
    cyan="#00838f", menu="#ffffff", hover="#f0f1f3", panel="#fafafa", shadow="0.16",
)


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def T(x, y, s, fill, size=13, family=UI, weight="400", anchor="start"):
    return (f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" '
            f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" '
            f'xml:space="preserve">{esc(s)}</text>')


def head(w, h, c, label):
    return ([f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
             f'viewBox="0 0 {w} {h}" role="img" aria-label="{esc(label)}">',
             '<defs><filter id="m" x="-30%" y="-30%" width="160%" height="180%">'
             f'<feDropShadow dx="0" dy="10" stdDeviation="16" flood-color="#000" '
             f'flood-opacity="{c["shadow"]}"/></filter></defs>',
             f'<rect width="{w}" height="{h}" fill="{c["page"]}"/>'])


def card(x, y, w, h, c, fill=None):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" '
            f'fill="{fill or c["win"]}" stroke="{c["line"]}" filter="url(#m)"/>')


# ── 1. Everything it can do, in one list ──────────────────────────────────
def commands(c):
    W, H = 1400, 700
    p = head(W, H, c, "The command list: type to narrow it, every line showing its own shortcut")
    x, y, w = 60, 60, W - 120
    p.append(card(x, y, w, H - 120, c))
    p.append(f'<rect x="{x}" y="{y}" width="{w}" height="62" rx="10" fill="{c["bar"]}"/>')
    p.append(f'<rect x="{x}" y="{y + 40}" width="{w}" height="22" fill="{c["bar"]}"/>')
    p.append(f'<path d="M{x} {y + 62} h{w}" stroke="{c["line"]}"/>')
    p.append(T(x + 26, y + 39, "spld", c["fg"], 20, MONO, "500"))
    p.append(f'<rect x="{x + 84}" y="{y + 22}" width="2" height="22" fill="{c["accent"]}"/>')
    p.append(T(x + w - 26, y + 39, "8 of 214", c["faint"], 12.5, UI, "400", "end"))

    rows = [
        ("Split down", [("S", 1), ("p", 1), ("l", 0), ("i", 0), ("t", 0), (" ", 0), ("d", 1), ("o", 0), ("w", 0), ("n", 0)], "⌘⇧D", "block", True),
        ("Split down and open an agent", None, "", "block", False),
        ("Split left", None, "⌘⇧←", "block", False),
        ("Speed up the scrollback", None, "", "terminal", False),
        ("Spelling of the interface language", None, "", "window", False),
        ("Send the phrase as it is dictated", None, "", "voice", False),
        ("Save the settings to a file", None, "⌘⌥S", "settings", False),
        ("Show the dock", None, "⌘⇧B", "window", False),
    ]
    ry = y + 84
    for label, marks, key, group, active in rows:
        if active:
            p.append(f'<rect x="{x + 10}" y="{ry - 20}" width="{w - 20}" height="40" rx="8" fill="{c["hover"]}"/>')
        if marks:
            spans = "".join(
                f'<tspan fill="{c["accent"]}" font-weight="700">{esc(ch)}</tspan>'
                if hit else f'<tspan>{esc(ch)}</tspan>' for ch, hit in marks)
            p.append(f'<text x="{x + 28}" y="{ry + 5}" font-family="{UI}" font-size="15" '
                     f'fill="{c["fg"]}" xml:space="preserve">{spans}</text>')
        else:
            p.append(T(x + 28, ry + 5, label, c["fg"], 15, UI))
        p.append(T(x + w - 140, ry + 5, group, c["faint"], 12, UI, "400", "end"))
        if key:
            kw = len(key) * 11 + 16
            p.append(f'<rect x="{x + w - 26 - kw}" y="{ry - 11}" width="{kw}" height="22" rx="5" '
                     f'fill="{c["tab"]}"/>')
            p.append(T(x + w - 26 - kw / 2, ry + 5, key, c["dim"], 12.5, MONO, "500", "middle"))
        ry += 58
    p.append(T(x + 26, H - 82, "A button, a key, the menu bar, this list and the command line "
                               "name the same action in one dictionary.", c["dim"], 13, UI))
    p.append('</svg>')
    return "".join(p)


# ── 2. Settings: eight sections, and a theme that says whether it can be read ─
def settings(c):
    W, H = 1400, 700
    p = head(W, H, c, "The settings screen: sections down the side, and a theme picker that states "
                      "its contrast and colour-blind distinguishability")
    x, y, w, h = 60, 60, W - 120, H - 120
    p.append(card(x, y, w, h, c))
    p.append(f'<rect x="{x}" y="{y}" width="{w}" height="52" rx="10" fill="{c["bar"]}"/>')
    p.append(f'<rect x="{x}" y="{y + 30}" width="{w}" height="22" fill="{c["bar"]}"/>')
    p.append(f'<path d="M{x} {y + 52} h{w}" stroke="{c["line"]}"/>')
    p.append(T(x + 20, y + 33, "Settings", c["fg"], 14, UI, "600"))
    p.append(T(x + w - 20, y + 33, "every line here is also a line in a file", c["faint"], 12, UI, "400", "end"))

    # sections
    sw = 220
    p.append(f'<path d="M{x + sw} {y + 52} v{h - 52}" stroke="{c["line"]}"/>')
    sections = [("themes", True), ("monitor", False), ("terminal", False), ("window", False),
                ("buttons", False), ("agents", False), ("keys", False), ("signals", False),
                ("faults", False)]
    sy = y + 84
    for name, active in sections:
        if active:
            p.append(f'<rect x="{x + 10}" y="{sy - 19}" width="{sw - 20}" height="34" rx="7" fill="{c["hover"]}"/>')
        p.append(T(x + 28, sy + 4, name, c["fg"] if active else c["dim"], 14, UI,
                   "600" if active else "400"))
        sy += 44

    # theme list
    lx = x + sw + 28
    p.append(T(lx, y + 86, "THEME", c["dim"], 10, UI, "600"))
    themes = [("Dark", ["#17191d", "#42a5f5", "#66bb6a", "#ffca28", "#ab47bc"], True),
              ("Light", ["#ffffff", "#1565c0", "#2e7d32", "#a06a00", "#7b1fa2"], False),
              ("Catppuccin Mocha", ["#1e1e2e", "#89b4fa", "#a6e3a1", "#f9e2af", "#cba6f7"], False),
              ("Nord", ["#2e3440", "#81a1c1", "#a3be8c", "#ebcb8b", "#b48ead"], False),
              ("Gruvbox", ["#282828", "#83a598", "#b8bb26", "#fabd2f", "#d3869b"], False),
              ("Colour-vision safe", ["#101418", "#56b4e9", "#009e73", "#f0e442", "#cc79a7"], False)]
    ty = y + 104
    for name, swatch, active in themes:
        if active:
            p.append(f'<rect x="{lx - 10}" y="{ty}" width="330" height="40" rx="8" fill="{c["hover"]}"/>')
        for i, col in enumerate(swatch):
            p.append(f'<rect x="{lx + i * 18}" y="{ty + 12}" width="14" height="16" rx="3" fill="{col}" '
                     f'stroke="{c["line"]}"/>')
        p.append(T(lx + 108, ty + 26, name, c["fg"], 13.5, UI, "600" if active else "400"))
        ty += 46

    # the readout
    rx = lx + 372
    rw = x + w - rx - 28
    p.append(T(rx, y + 86, "WHAT THIS THEME IS LIKE TO READ", c["dim"], 10, UI, "600"))
    p.append(f'<rect x="{rx}" y="{y + 100}" width="{rw}" height="184" rx="9" fill="{c["panel"]}" '
             f'stroke="{c["line"]}"/>')
    rows = [("text contrast", "12.4 : 1", c["green"], "well past the 4.5 a small size needs"),
            ("colour-blind distinguishability", "good", c["green"], "checked against three forms of it"),
            ("Minimum contrast", "4.5 : 1", c["dim"], "the floor this palette is held to")]
    ry = y + 132
    for label, value, col, note in rows:
        p.append(T(rx + 18, ry, label, c["fg"], 13, UI, "500"))
        p.append(T(rx + rw - 18, ry, value, col, 13, MONO, "600", "end"))
        p.append(T(rx + 18, ry + 20, note, c["faint"], 11.5, UI))
        ry += 54

    # preview
    p.append(T(rx, y + 320, "AND WHAT IT LOOKS LIKE", c["dim"], 10, UI, "600"))
    p.append(f'<rect x="{rx}" y="{y + 334}" width="{rw}" height="150" rx="9" fill="{c["term"]}" '
             f'stroke="{c["line"]}"/>')
    py = y + 362
    for s, col in [("$ npm run build", c["fg"]), ("  built in 4.1s", c["green"]),
                   ("  2 warnings", c["yellow"]), ("$ ", c["fg"])]:
        p.append(T(rx + 18, py, s, col, 13, MONO))
        py += 26

    p.append(T(x + sw + 28, y + h - 34, "A theme is a file. Drop one in the folder and it is in the "
                                        "list; edit it and the window redraws.", c["dim"], 13, UI))
    p.append('</svg>')
    return "".join(p)


# ── 3. The monitor, and the file that arranges it ─────────────────────────
def monitor(c):
    W, H = 1400, 620
    p = head(W, H, c, "The system monitor and the five-line skin file that arranges it")
    x, y = 60, 60
    mw = 800
    p.append(card(x, y, mw, H - 100, c))
    p.append(f'<rect x="{x}" y="{y}" width="{mw}" height="40" rx="10" fill="{c["bar"]}"/>')
    p.append(f'<rect x="{x}" y="{y + 22}" width="{mw}" height="18" fill="{c["bar"]}"/>')
    p.append(f'<path d="M{x} {y + 40} h{mw}" stroke="{c["line"]}"/>')
    p.append(T(x + 18, y + 26, "monitor", c["dim"], 12, UI, "500"))
    p.append(T(x + mw - 18, y + 26, "eleven kinds of panel", c["faint"], 11.5, UI, "400", "end"))

    cards = [("PROCESSOR", "18%", "user 11 · sys ≈7", 0.18, c["blue"]),
             ("MEMORY", "21.4 GB", "of 32.0 GB · swap 0", 0.67, c["magenta"]),
             ("DISK", "402 GB", "free of 1.0 TB", 0.6, c["cyan"]),
             ("NETWORK", "1.4 MB/s", "down · 240 KB/s up", 0.35, c["green"]),
             ("BATTERY", "84%", "3 h 20 m · wear 4%", 0.84, c["yellow"]),
             ("SENSORS", "48 °C", "cpu · fans 1 900 rpm", 0.42, c["red"])]
    cw, ch = (mw - 24 - 2 * 12) / 3, 150
    for i, (title, big, sub, frac, col) in enumerate(cards):
        cx = x + 12 + (i % 3) * (cw + 12)
        cy = y + 52 + (i // 3) * (ch + 12)
        p.append(f'<rect x="{cx}" y="{cy}" width="{cw}" height="{ch}" rx="8" fill="{c["panel"]}" '
                 f'stroke="{c["line"]}"/>')
        p.append(T(cx + 12, cy + 20, title, c["dim"], 9.5, UI, "600"))
        p.append(T(cx + 12, cy + 50, big, c["fg"], 20, MONO, "500"))
        p.append(T(cx + 12, cy + 70, sub, c["faint"], 10.5, UI))
        p.append(f'<rect x="{cx + 12}" y="{cy + 84}" width="{cw - 24}" height="6" rx="3" fill="{c["tab"]}"/>')
        p.append(f'<rect x="{cx + 12}" y="{cy + 84}" width="{(cw - 24) * frac:.0f}" height="6" rx="3" fill="{col}"/>')
        pts = [30, 36, 28, 44, 58, 47, 35, 30, 38, 52, 66, 55, 42, 37, 31, 34]
        w0 = (cw - 24) / (len(pts) - 1)
        base = cy + ch - 14
        path = " ".join(f'{"M" if k == 0 else "L"}{cx + 12 + k * w0:.1f} {base - v * 0.55:.1f}'
                        for k, v in enumerate(pts))
        p.append(f'<path d="{path}" fill="none" stroke="{col}" stroke-width="1.5" stroke-linejoin="round" '
                 'opacity="0.85"/>')

    # the file
    fx = x + mw + 36
    fw = W - fx - 60
    p.append(T(fx, y + 22, "skins/essentials.json", c["dim"], 11, MONO, "600"))
    p.append(f'<rect x="{fx}" y="{y + 36}" width="{fw}" height="330" rx="10" fill="{c["term"]}" '
             f'stroke="{c["line"]}" filter="url(#m)"/>')
    code = [('{', c["fg"]),
            ('  "name": ', c["blue"]), ('"Essentials only",', c["green"]),
            ('  "panels": [', c["blue"]),
            ('    { "kind": ', c["fg"]), ('"cpu"', c["green"]), (', "title": ', c["fg"]), ('"PROCESSOR" },', c["green"]),
            ('    { "kind": ', c["fg"]), ('"mem"', c["green"]), (', "title": ', c["fg"]), ('"MEMORY" },', c["green"]),
            ('    { "kind": ', c["fg"]), ('"procs"', c["green"]), (', "rows": ', c["fg"]), ('10 }', c["yellow"]),
            ('  ],', c["blue"]),
            ('  "colors": { "a": ', c["blue"]), ('"#3b82f6"', c["green"]), (' }', c["blue"]),
            ('}', c["fg"])]
    # lay the code out as lines
    lines = [[code[0]], [code[1], code[2]], [code[3]],
             [code[4], code[5], code[6], code[7]],
             [code[8], code[9], code[10], code[11]],
             [code[12], code[13], code[14], code[15]],
             [code[16]], [code[17], code[18], code[19]], [code[20]]]
    cy2 = y + 66
    for line in lines:
        cx2 = fx + 18
        for s, col in line:
            p.append(T(cx2, cy2, s, col, 12.5, MONO))
            cx2 += len(s) * 7.5
        cy2 += 26
    p.append(T(fx, y + 400, "Drop it in the settings folder and run", c["dim"], 13, UI))
    p.append(f'<rect x="{fx}" y="{y + 414}" width="{fw}" height="34" rx="7" fill="{c["term"]}" '
             f'stroke="{c["line"]}"/>')
    p.append(T(fx + 16, y + 436, "vobuda skin essentials", c["fg"], 13, MONO))
    p.append(T(fx, y + 486, "No restart. The window redraws as the", c["faint"], 12.5, UI))
    p.append(T(fx, y + 506, "file is saved.", c["faint"], 12.5, UI))
    p.append('</svg>')
    return "".join(p)


# ── 4. A file open beside the shell ───────────────────────────────────────
def editor(c):
    W, H = 1400, 640
    p = head(W, H, c, "The files panel, a file open beside the shell, and search across the project")
    x, y = 60, 60
    w, h = W - 120, H - 120
    p.append(card(x, y, w, h, c))
    p.append(f'<rect x="{x}" y="{y}" width="{w}" height="40" rx="10" fill="{c["bar"]}"/>')
    p.append(f'<rect x="{x}" y="{y + 22}" width="{w}" height="18" fill="{c["bar"]}"/>')
    p.append(f'<path d="M{x} {y + 40} h{w}" stroke="{c["line"]}"/>')
    p.append(T(x + 18, y + 26, "app.tsx — colouring from the terminal's own theme", c["dim"], 12, UI, "500"))

    # files panel
    fw = 250
    p.append(f'<path d="M{x + fw} {y + 40} v{h - 40}" stroke="{c["line"]}"/>')
    files = [("src", True, 0), ("components", True, 1), ("Button.tsx", False, 2),
             ("Dialog.tsx", False, 2), ("app.tsx", False, 1), ("store.ts", False, 1),
             ("styles.css", False, 1), ("tests", True, 0), ("app.test.ts", False, 1),
             ("package.json", False, 0), ("README.md", False, 0)]
    fy = y + 72
    for name, folder, depth in files:
        gx = x + 20 + depth * 16
        if folder:
            p.append(f'<path d="M{gx} {fy - 9} h6 l2 3 h8 v10 h-16 z" fill="none" stroke="{c["faint"]}" '
                     'stroke-width="1.2" stroke-linejoin="round"/>')
        else:
            p.append(f'<path d="M{gx + 1} {fy - 10} h8 l4 4 v12 h-12 z" fill="none" stroke="{c["faint"]}" '
                     'stroke-width="1.2" stroke-linejoin="round"/>')
        active = name == "app.tsx"
        if active:
            p.append(f'<rect x="{x + 8}" y="{fy - 15}" width="{fw - 16}" height="26" rx="6" fill="{c["hover"]}"/>')
            p.append(f'<path d="M{gx + 1} {fy - 10} h8 l4 4 v12 h-12 z" fill="none" stroke="{c["accent"]}" '
                     'stroke-width="1.2" stroke-linejoin="round"/>')
        p.append(T(gx + 22, fy + 3, name, c["fg"] if not folder else c["dim"], 13, UI,
                   "600" if active else "400"))
        fy += 30

    # editor
    ex = x + fw
    code = [
        [("import", c["magenta"]), (" { useStore } ", c["fg"]), ("from", c["magenta"]), (" \"./store\"", c["green"])],
        [],
        [("export function", c["magenta"]), (" App", c["blue"]), ("() {", c["fg"])],
        [("  const", c["magenta"]), (" tabs = useStore((s) => s.tabs)", c["fg"])],
        [("  const", c["magenta"]), (" active = useStore((s) => s.activeTab)", c["fg"])],
        [],
        [("  return", c["magenta"]), (" (", c["fg"])],
        [("    <", c["fg"]), ("Window", c["yellow"]), (" tabs={tabs} active={active}>", c["fg"])],
        [("      <", c["fg"]), ("Dock", c["yellow"]), (" side=", c["fg"]), ("\"left\"", c["green"]), (" />", c["fg"])],
        [("      <", c["fg"]), ("Layout", c["yellow"]), (" />", c["fg"])],
        [("    </", c["fg"]), ("Window", c["yellow"]), (">", c["fg"])],
        [("  )", c["fg"])],
        [("}", c["fg"])],
    ]
    cy = y + 76
    for i, line in enumerate(code):
        p.append(T(ex + 22, cy, str(i + 1).rjust(2), c["faint"], 12, MONO))
        cx = ex + 52
        for s, col in line:
            p.append(T(cx, cy, s, col, 13.5, MONO))
            cx += len(s) * 8.1
        cy += 25

    # cursors
    for cyy in [y + 76 + 25 * 3, y + 76 + 25 * 4]:
        p.append(f'<rect x="{ex + 52 + 7 * 8.1:.0f}" y="{cyy - 13}" width="2" height="17" fill="{c["accent"]}"/>')
    p.append(T(ex + 22, y + h - 26, "two cursors, placed by keyboard or mouse", c["faint"], 11.5, UI))

    # search across the project
    sx = x + w - 430
    p.append(f'<rect x="{sx}" y="{y + 66}" width="410" height="266" rx="10" fill="{c["menu"]}" '
             f'stroke="{c["line"]}" filter="url(#m)"/>')
    p.append(f'<rect x="{sx + 12}" y="{y + 78}" width="386" height="32" rx="7" fill="{c["term"]}" '
             f'stroke="{c["line"]}"/>')
    p.append(T(sx + 26, y + 99, "useStore", c["fg"], 13, MONO))
    p.append(T(sx + 384, y + 99, "34 in 9 files", c["faint"], 11.5, UI, "400", "end"))
    hits = [("src/app.tsx", "3"), ("src/Dock.tsx", "5"), ("src/Layout.tsx", "7"),
            ("src/Monitor.tsx", "4"), ("src/settings/panel.tsx", "6"), ("tests/app.test.ts", "9")]
    hy = y + 140
    for name, n in hits:
        p.append(T(sx + 26, hy, name, c["fg"], 12.5, MONO))
        p.append(T(sx + 384, hy, n, c["faint"], 12, MONO, "400", "end"))
        hy += 30
    p.append(T(sx + 26, hy + 6, "the core walks the folder, the window draws it", c["faint"], 11.5, UI))
    p.append('</svg>')
    return "".join(p)


root = pathlib.Path("/Users/gary/Claude_memory/проекты/vobuda-public/assets")
for name, fn in [("commands", commands), ("settings", settings),
                 ("monitor", monitor), ("editor", editor)]:
    (root / f"{name}.svg").write_text(fn(DARK))
    (root / f"{name}-light.svg").write_text(fn(LIGHT))
    print(f"{name}.svg", (root / f"{name}.svg").stat().st_size, "bytes")
