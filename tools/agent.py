#!/usr/bin/env python3
"""The agent control bar and the three menus that are the point of it.

Everything an agent knows about itself, in the window rather than in a stream
of text: what it may do, which model, how hard it is thinking, what skills it
has here, and every command it takes — as a menu a mouse can use.
"""

import pathlib

MONO = "ui-monospace, 'SF Mono', SFMono-Regular, Menlo, Consolas, monospace"
UI = "system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif"

DARK = dict(
    page="#0b0c0e", win="#17191d", bar="#232529", tab="#333539", term="#0f1115",
    fg="#d6d9de", dim="#8b9099", faint="#5d636c", line="#2f3135", accent="#90caf9",
    green="#66bb6a", blue="#42a5f5", magenta="#ab47bc", yellow="#ffca28",
    menu="#1f2226", hover="#2a2d33", shadow="0.45",
)
LIGHT = dict(
    page="#eef0f3", win="#ffffff", bar="#f1f1f2", tab="#e2e2e3", term="#ffffff",
    fg="#1c1e21", dim="#6b7076", faint="#9aa0a6", line="#dbdbdb", accent="#1565c0",
    green="#2e7d32", blue="#1565c0", magenta="#7b1fa2", yellow="#a06a00",
    menu="#ffffff", hover="#f0f1f3", shadow="0.16",
)


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def text(x, y, s, fill, size=13, family=UI, weight="400", anchor="start"):
    return (f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" '
            f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" '
            f'xml:space="preserve">{esc(s)}</text>')


def draw(c):
    W, H = 1600, 800
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
         'role="img" aria-label="The agent control bar, and the sessions, skills and commands menus '
         'it opens">']
    p.append('<defs>'
             '<filter id="m" x="-30%" y="-30%" width="160%" height="180%">'
             f'<feDropShadow dx="0" dy="10" stdDeviation="16" flood-color="#000" flood-opacity="{c["shadow"]}"/>'
             '</filter></defs>')
    p.append(f'<rect width="{W}" height="{H}" fill="{c["page"]}"/>')

    # ── the bar ───────────────────────────────────────────────────────────
    bx, by, bw = 60, 60, W - 120
    p.append(f'<rect x="{bx}" y="{by}" width="{bw}" height="62" rx="12" fill="{c["win"]}" '
             f'stroke="{c["line"]}"/>')
    p.append(f'<rect x="{bx}" y="{by}" width="{bw}" height="30" rx="12" fill="{c["bar"]}"/>')
    p.append(f'<rect x="{bx}" y="{by + 18}" width="{bw}" height="12" fill="{c["bar"]}"/>')
    p.append(f'<path d="M{bx} {by + 30} h{bw}" stroke="{c["line"]}"/>')
    p.append(text(bx + 16, by + 20, "Claude Code — a block like any other", c["dim"], 11.5, UI, "500"))

    x = bx + 14
    y = by + 40
    # state
    p.append(f'<circle cx="{x + 9}" cy="{y + 11}" r="4.5" fill="{c["yellow"]}"/>')
    p.append(text(x + 22, y + 15, "waiting", c["fg"], 12, UI, "500"))
    x += 86

    def pill(x, label, value=None, glyph=None, caret=True, wide=None):
        w = wide or (len(label) * 7.0 + (len(value) * 7.2 + 14 if value else 0) + (26 if caret else 12) + 24)
        out = [f'<rect x="{x}" y="{y}" width="{w:.0f}" height="24" rx="6" fill="{c["tab"]}"/>']
        gx = x + 11
        if glyph == "plus":
            out.append(f'<path d="M{gx} {y+12} h9 M{gx+4.5} {y+7.5} v9" stroke="{c["dim"]}" '
                       'stroke-width="1.5" stroke-linecap="round"/>')
            gx += 15
        elif glyph == "play":
            out.append(f'<path d="M{gx} {y+7} l8 5 -8 5 z" fill="none" stroke="{c["dim"]}" '
                       'stroke-width="1.4" stroke-linejoin="round"/>')
            gx += 15
        elif glyph == "clock":
            out.append(f'<circle cx="{gx+4.5}" cy="{y+12}" r="5" fill="none" stroke="{c["dim"]}" stroke-width="1.3"/>')
            out.append(f'<path d="M{gx+4.5} {y+9} v3.2 l2.4 1.4" stroke="{c["dim"]}" stroke-width="1.3" '
                       'stroke-linecap="round" fill="none"/>')
            gx += 15
        elif glyph == "spark":
            out.append(f'<path d="M{gx+4.5} {y+6} l1.7 3.9 3.9 1.7 -3.9 1.7 -1.7 3.9 -1.7 -3.9 '
                       f'-3.9 -1.7 3.9 -1.7 z" fill="none" stroke="{c["dim"]}" stroke-width="1.3" '
                       'stroke-linejoin="round"/>')
            gx += 15
        elif glyph == "cube":
            out.append(f'<path d="M{gx+4.5} {y+6.5} l4.5 2.4 v5 l-4.5 2.4 -4.5 -2.4 v-5 z" fill="none" '
                       f'stroke="{c["dim"]}" stroke-width="1.3" stroke-linejoin="round"/>')
            gx += 15
        elif glyph == "bars":
            for i, h in enumerate([4, 7, 10]):
                out.append(f'<rect x="{gx + i*3.4}" y="{y + 15 - h}" width="2.2" height="{h}" rx="1" fill="{c["dim"]}"/>')
            gx += 15
        elif glyph == "shield":
            out.append(f'<path d="M{gx+4.5} {y+6} l4.5 1.8 v4.2 c0 2.6 -2 4.4 -4.5 5.2 '
                       f'-2.5 -0.8 -4.5 -2.6 -4.5 -5.2 v-4.2 z" fill="none" stroke="{c["dim"]}" '
                       'stroke-width="1.3" stroke-linejoin="round"/>')
            gx += 15
        elif glyph == "list":
            for i in range(3):
                out.append(f'<path d="M{gx} {y + 8 + i*3.5} h9" stroke="{c["dim"]}" stroke-width="1.3" '
                           'stroke-linecap="round"/>')
            gx += 15
        out.append(text(gx, y + 16, label, c["fg"], 11.5, UI, "500"))
        vx = gx + len(label) * 7.0 + 8
        if value:
            vw = len(value) * 7.2 + 12
            out.append(f'<rect x="{vx}" y="{y + 5}" width="{vw:.0f}" height="14" rx="4" '
                       f'fill="{c["accent"]}" fill-opacity="0.18"/>')
            out.append(text(vx + vw / 2, y + 15.5, value, c["accent"], 10.5, UI, "600", "middle"))
        if caret:
            cxx = x + w - 13
            out.append(f'<path d="M{cxx - 3.2} {y + 10.5} l3.2 3.6 3.2 -3.6" fill="none" '
                       f'stroke="{c["faint"]}" stroke-width="1.3" stroke-linecap="round" '
                       'stroke-linejoin="round"/>')
        return "".join(out), w

    for label, value, glyph, caret in [
        ("new", None, "plus", False),
        ("continue", None, "play", False),
        ("sessions", None, "clock", True),
        ("skills", None, "spark", True),
        ("model", "Opus 5", "cube", True),
        ("effort", "high", "bars", True),
        ("decides itself", None, "shield", True),
        ("commands", None, "list", True),
    ]:
        s, w = pill(x, label, value, glyph, caret)
        p.append(s)
        x += w + 8

    # ── three menus ───────────────────────────────────────────────────────
    top = 176
    col_w = 470
    gap = 35
    cols = [60, 60 + col_w + gap, 60 + 2 * (col_w + gap)]

    def menu(x, y, w, h, title, rows, right_col=True):
        out = [text(x + 2, y - 12, title, c["dim"], 10.5, UI, "600"),
               f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{c["menu"]}" '
               f'stroke="{c["line"]}" filter="url(#m)"/>']
        ry = y + 14
        for row in rows:
            kind = row[0]
            if kind == "group":
                _, name, count = row
                out.append(f'<path d="M{x + 16} {ry + 11} l4 4 -4 4" fill="none" stroke="{c["faint"]}" '
                           'stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/>')
                out.append(text(x + 32, ry + 19, name, c["fg"], 13, UI, "500"))
                out.append(text(x + w - 18, ry + 19, str(count), c["faint"], 12, UI, "400", "end"))
                ry += 34
            elif kind == "row":
                _, left, right, active = row
                if active:
                    out.append(f'<rect x="{x + 6}" y="{ry}" width="{w - 12}" height="28" rx="6" fill="{c["hover"]}"/>')
                out.append(text(x + 18, ry + 19, left, c["fg"], 13, UI, "400"))
                if right:
                    out.append(text(x + w - 18, ry + 19, right, c["faint"], 12, MONO, "400", "end"))
                ry += 28
            elif kind == "time":
                _, when, what = row
                out.append(text(x + 18, ry + 18, when, c["faint"], 11.5, MONO))
                out.append(text(x + 108, ry + 18, what, c["fg"], 12.5, UI))
                ry += 27
            elif kind == "rule":
                out.append(f'<path d="M{x + 10} {ry + 6} h{w - 20}" stroke="{c["line"]}"/>')
                ry += 13
        return "".join(out)

    p.append(menu(cols[0], top, col_w, 268, "SESSIONS — read from the agent's own files", [
        ("time", "14:06", "add the copy button to the address panel"),
        ("time", "11:42", "why does the update never reach anybody"),
        ("time", "09:15", "read the whole release script as an attacker"),
        ("time", "Tue", "the headset microphone stops the engine"),
        ("time", "Tue", "translate the guide's new paragraphs"),
        ("rule",),
        ("time", "Mon", "split the settings screen into sections"),
        ("time", "Mon", "the window keeps drawing when a panel throws"),
        ("time", "Sun", "one action for every button and key"),
    ]))

    p.append(menu(cols[1], top, col_w, 268, "SKILLS — what this folder actually has", [
        ("group", "Mine", 14),
        ("group", "team", 46),
        ("group", "writing", 8),
        ("group", "review", 12),
        ("group", "superpowers", 14),
        ("group", "research", 6),
        ("group", "release", 4),
    ]))

    p.append(menu(cols[2], top, col_w, 268, "MODEL — what this installation has, not our list", [
        ("row", "default", "", False),
        ("row", "Opus", "opus", True),
        ("row", "Sonnet", "sonnet", False),
        ("row", "Haiku", "haiku", False),
        ("row", "Opus, 1M context", "opus[1m]", False),
        ("row", "Fable", "fable", False),
        ("rule",),
        ("row", "effort  ·  low   medium   high   xhigh", "", False),
    ]))

    # commands, wide, underneath
    cy = top + 318
    cw = col_w * 2 + gap
    p.append(text(62, cy - 12, "COMMANDS — every slash command this agent takes, as a menu a mouse can use",
                  c["dim"], 10.5, UI, "600"))
    p.append(f'<rect x="60" y="{cy}" width="{cw}" height="216" rx="10" fill="{c["menu"]}" '
             f'stroke="{c["line"]}" filter="url(#m)"/>')
    rows = [("compact the conversation", "/compact"), ("clear the conversation", "/clear"),
            ("choose the model", "/model"), ("choose the effort", "/effort"),
            ("what it has cost", "/cost"), ("what is in context", "/context"),
            ("past sessions", "/resume"), ("undo the last steps", "/rewind"),
            ("edit the memory files", "/memory"), ("agents", "/agents"),
            ("MCP servers", "/mcp"), ("state", "/status")]
    for i, (label, cmd) in enumerate(rows):
        col = i % 2
        row = i // 2
        rx = 60 + 14 + col * (cw - 28) / 2
        ry = cy + 20 + row * 34
        if i == 4:
            p.append(f'<rect x="{rx - 6}" y="{ry - 2}" width="{(cw - 28) / 2 - 8}" height="28" rx="6" '
                     f'fill="{c["hover"]}"/>')
        p.append(text(rx + 6, ry + 17, label, c["fg"], 13, UI))
        p.append(text(rx + (cw - 28) / 2 - 20, ry + 17, cmd, c["faint"], 12, MONO, "400", "end"))

    # the note beside it
    nx = cols[2]
    p.append(text(nx + 2, cy - 12, "AND WHAT IT MAY DO", c["dim"], 10.5, UI, "600"))
    p.append(f'<rect x="{nx}" y="{cy}" width="{col_w}" height="216" rx="10" fill="{c["menu"]}" '
             f'stroke="{c["line"]}" filter="url(#m)"/>')
    modes = [("decides itself", True), ("accepts edits", False),
             ("asks before every step", False), ("plan only", False)]
    my = cy + 20
    for label, active in modes:
        if active:
            p.append(f'<rect x="{nx + 8}" y="{my - 2}" width="{col_w - 16}" height="28" rx="6" fill="{c["hover"]}"/>')
        p.append(f'<circle cx="{nx + 26}" cy="{my + 12}" r="5" fill="none" stroke="{c["faint"]}" stroke-width="1.3"/>')
        if active:
            p.append(f'<circle cx="{nx + 26}" cy="{my + 12}" r="2.4" fill="{c["accent"]}"/>')
        p.append(text(nx + 42, my + 17, label, c["fg"], 13, UI))
        my += 34
    p.append(f'<path d="M{nx + 10} {my + 4} h{col_w - 20}" stroke="{c["line"]}"/>')
    p.append(text(nx + 18, my + 28, "Read off the agent's own screen, not", c["dim"], 12, UI))
    p.append(text(nx + 18, my + 48, "a setting of ours it could disagree with.", c["dim"], 12, UI))

    p.append('</svg>')
    return "".join(p)


root = pathlib.Path("/Users/gary/Claude_memory/проекты/vobuda-public/assets")
(root / "agent.svg").write_text(draw(DARK))
(root / "agent-light.svg").write_text(draw(LIGHT))
print("agent.svg", (root / "agent.svg").stat().st_size, "bytes")
