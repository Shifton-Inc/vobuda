<p align="center">
  <img src="assets/icon.png" alt="" width="128" height="128">
</p>

<h1 align="center">vobuda</h1>

<p align="center">
  <b>A terminal that keeps every setting as a file you can read —<br/>
  and treats a running AI agent as part of the window, not as text scrolling past.</b>
</p>

<p align="center">
  <a href="https://vobuda.com"><img alt="Download" src="https://img.shields.io/badge/download-vobuda.com-2563eb?style=flat-square"></a>
  <img alt="Version" src="https://img.shields.io/badge/version-0.2.2-1f2937?style=flat-square">
  <img alt="macOS" src="https://img.shields.io/badge/macOS-signed%20%26%20notarised-1f2937?style=flat-square">
  <img alt="Languages" src="https://img.shields.io/badge/languages-40-1f2937?style=flat-square">
  <a href="LICENSE"><img alt="Licence" src="https://img.shields.io/badge/licence-free%2C%20closed%20source-1f2937?style=flat-square"></a>
</p>

<p align="center">
  <sub>
    Rust · Tauri 2 · React 19 · xterm.js · macOS today, Linux and Windows next
  </sub>
</p>

---

A terminal is where the work happens, so it should get out of the way — and
where it cannot, it should be honest about what it is doing.

Three things follow from that, and they are what this program is.

**Every setting is a file.** Themes, monitor skins, buttons, shortcuts, agent
descriptions — readable JSON in `~/.config/vobuda`. Save the file and the
window redraws. No restart, no hidden state, nothing that exists only inside
the program.

**Everything can be reached five ways.** A button, a key, the menu bar, the
command line, and one list of all of it. They are not five implementations:
each names the same action in one dictionary, so what a button does is exactly
what a script can do.

**An agent is part of the window.** Start Claude Code or Codex in a block and a
control bar appears above it: past sessions, skills, model, effort, what it may
do without asking. Its lists are ordinary drop-downs, drawn by us — an agent
draws its own with arrow keys, and a mouse cannot use those at all.

## Get it

One line, on a Mac:

```bash
curl -fsSL https://vobuda.com/install.sh | sh
```

It reads which version is current, downloads the image, checks its SHA-256
against the sums file on the same site, copies the app into `/Applications`
(or `~/Applications` where that would need a password it will not ask for),
and opens it. No administrator rights, every step printed, and it stops at the
first thing that goes wrong. The same line updates an installed copy — and the
program's own update strip types it for you.

The disk image is on **[vobuda.com](https://vobuda.com)** as well, for anyone
who would rather download it in a browser.

**macOS opens it without a word.** The build is signed with an Apple Developer
ID and notarised — no "cannot be verified" window, no trip through System
Settings.

**An image passed on through a messenger will not open.** macOS marks every
file a sandboxed program wrote — a messenger from the App Store is one — and
refuses to run anything off it, however well the build is signed. Nothing on
the building side can remove that mark. The install line above avoids it
entirely, because `curl` sets no such mark; an image already downloaded is
freed with:

```bash
xattr -d com.apple.quarantine ~/Downloads/vobuda-*.dmg
```

## What it does

### Blocks, not just tabs

A window holds tabs, a tab holds blocks, and a block is a terminal, a file
being edited, the files panel, a web page, the system monitor or the settings
screen. They split, drag, resize and close the same way — one set of rules for
everything, rather than a second set for each new feature.

A block can be **dragged onto another tab** and it lands there with its shell
still running: same session, different place. The alternative — close it and
start again — kills the build you were moving it for.

### Everything it can do, in one list

`Cmd+K`. Type to narrow it — the letters match in order, so `spld` finds
**Split down** — arrows to move, Enter to run. Each line shows its own
shortcut, so this is also where the keys are learnt.

### Agents, described by themselves

Sessions come from the agent's own files, models from its own installation,
effort levels from the model in use, and the access mode is read off its screen.
**Nothing here is our list of somebody else's models** — that list goes stale
the day a new model ships.

**While you were away.** Each time an agent stops, one line is kept: which
block, what it was asked, when it finished, how long it took. Grouped by block,
newest first, with a mark on what you have not seen. The request is read off
the agent's own screen and left empty when it cannot be read — a guess in a
record is worse than a gap.

**And the night nobody is there for.** The machine is held awake while there is
work, an agent stopped by a usage limit goes back to work by itself when the
limit lifts, and a badge in the morning says what happened while you slept.

### A monitor of its own

Processor, cores, memory, disks, disk traffic, network, sensors, battery,
processes, GPU — as panels described by a skin file, not as a fixed screen.
Twenty-three looks ship; a skin of five lines makes another.

### A file opens beside the shell

Colouring for 227 kinds of file, taken from the terminal's theme so an open
file looks like it belongs next to the shell. Search across the work, a file
opened by typing part of its name, several cursors. Nothing is written until
`Cmd+S`, a file changed on disk underneath you is not overwritten, and a binary
is refused rather than shown as noise.

### Dictation, and reading the answer back

`Cmd+Shift+V` types what you say into the block; `Cmd+Shift+R` reads the
agent's answer out loud. Both use the system's own speech, **on your machine**
— nothing is sent anywhere. The strip says which language it is listening in,
and the reader knows where an answer begins and ends, because reading a person
their own question back is worse than silence.

### Settings, as a screen and as files

Eight sections, about ninety settings, and every one of them a line in a file
you can also edit by hand. The theme picker says what the contrast of the
chosen theme is and how distinguishable its colours are to a colour-blind
reader, because a theme that cannot be read is not a theme.

### And the small things

- **The right button is ours**, everywhere in the window: the block's own menu
  inside a block, the window's outside one, and settings that open *over* the
  work rather than instead of it.
- **Signals.** An agent that finished pulses a badge on its tab, plays a sound
  and posts a notice — and stops the moment you touch the window.
- **Workspaces.** A project is a window with its own settings, its own layout
  and its own name in the strip.
- **A quake window**: one global key, the terminal drops from the top of the
  screen, the same key hides it.
- **Sessions come back**: tabs, blocks and their folders, restored where they
  were — and a session that arrived from another machine opens what it can and
  says what it could not.
- **40 languages**, including the menu bar, which macOS builds in the core.
- **A guide in all 40**, opened from Help, written for somebody who does not
  program for a living.

## The command line is the whole program

```bash
vobuda state                    # what is in the window: tabs, blocks, panel, theme
vobuda do block.split-down      # any action by name — the same names the keys use
vobuda do "settings.here:themes"
vobuda button files             # press a dock button
vobuda send 'ls -la\n'          # type into the active block
vobuda theme dark               # theme, look, dock side
vobuda signal done              # badge and sound
vobuda log 20                   # the program's log
```

This is not a side door: the interface checks drive the program entirely
through it, which is why they can be trusted.

## Configuration

| File | What it holds |
|---|---|
| `settings.json` | theme, look, terminal, shell, window, signals |
| `themes/*.json` | colours and fonts — one file per theme |
| `looks/*.json` | the window's shape: corners, shadows, panel colours |
| `skins/*.json` | which panels the monitor shows and how they are drawn |
| `buttons.json` | the dock: buttons, their order, its side and shape |
| `agents.json` | how an agent is recognised and what it is offered |
| `keys.json` | shortcuts; the native menu is built from this same file |

A monitor skin in five lines:

```json
{
  "name": "Essentials only",
  "panels": [
    { "kind": "cpu", "title": "PROCESSOR" },
    { "kind": "mem", "title": "MEMORY" },
    { "kind": "procs", "title": "PROCESSES", "rows": 10 }
  ],
  "colors": { "a": "#3b82f6", "b": "#ec4899" }
}
```

Drop it in `~/.config/vobuda/skins/` and run `vobuda skin essentials`.

## What leaves your machine

Almost nothing, and each of these is worth naming.

- **Speech is recognised on the machine.** On-device recognition is demanded,
  not preferred; a language that can only be recognised over the network is
  refused, with instructions for installing it locally instead.
- **Faults are yours until you say otherwise.** The program keeps a record of
  its own faults where they happen, scrubbed before it is written, and sends
  nothing until you turn it on.
- **Once a day it asks whether there is a newer version**, and the address
  panel of the monitor — only while it is on screen — asks what address the
  internet sees. Neither request carries anything about you or the machine.

## Versions

Every version and what it added is in **[CHANGELOG.md](CHANGELOG.md)**. The
program looks for a new one once a day and says so in a single strip; there is
also **Check for updates** in the program's own menu.

## Licence

**Free of charge, and closed.** The program costs nothing — for your work and
your business alike — and its source is not published. What is handed out is
the build.

What the licence does not allow is handing the program on: distributing a copy,
selling it, offering it as a service, taking it apart or changing it, using its
name, or removing the parts of the interface that mention the author's other
products. If someone else wants it, point them at
[vobuda.com](https://vobuda.com) — it is free for them too.

See [LICENSE](LICENSE); it is a hundred and fifty lines and written to be read.
If you need something it does not give you, ask — the answer is often yes.

The libraries this is built on are other people's, given away under their own
terms. The full list with every licence text ships inside the program (menu:
**What vobuda is built on**); [THIRD-PARTY.md](THIRD-PARTY.md) is the readable
summary.

---

<p align="center">
  <sub>
    Made by <a href="https://github.com/Haruvg">Gary</a> ·
    <a href="https://vobuda.com">vobuda.com</a> ·
    a program from <a href="https://shifton.com">Shifton</a>
  </sub>
</p>
