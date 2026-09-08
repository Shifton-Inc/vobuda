# What changed, version by version

Every build that leaves this machine carries a number of its own, and every
number is here. Newest first.

The program looks for a new version once a day and says so in one strip; there
is also **Check for updates** in its own menu. Updating is the same line that
installs it: `curl -fsSL https://vobuda.com/install.sh | sh`.

---

## 0.3.6 — 8 September 2026

**The window stays where you left it, if you say so.** A finish elsewhere used to bring the window to the tab that finished; the signals settings now decide whether it does. Turned off, the badge lights up and nothing moves — which is what you want when you are working on another screen.

**What an agent shows opens beside its own work.** Ask an agent to show a file, a picture or a page and it appears in *its* tab, not in whichever tab you happen to be reading. Every block's shell carries its own name, and the command line puts it on the command.

**Quiet hours, said as many times as you need.** The hours are a list now: each entry with its own times and its own days, and a day can be named whole — the weekend quiet from end to end, the weekdays quiet only at night.

**The window can be worked by name.** `vobuda ui` lists everything on the screen — what it is called, what kind of thing it is, how it stands; `vobuda press <name>` presses one; `vobuda type` and `vobuda key` fill a field; `vobuda shot` photographs the window; `vobuda wait` waits for the window instead of guessing. An agent can now check its own work without asking you to click.

**The night's waiting says what it did.** Whether the window wrote "carry on" to an agent after a limit, or the agent carried on by itself, is in the log and readable the next morning.

**A question about reading a file has words.** When an agent stops to ask before reading a file outside the project, the bar says so and names the file instead of only "waits".

**The archive for a developer leaves your machine behind.** `.claude/settings.json` — the paths and permissions of *this* machine — stays out of it, and the README says so.

## 0.3.5 — 7 September 2026

**A block is a copy of the project.** Open a block in a copy and the agent works in a git worktree on its own branch; the copy goes when its last block closes, unless it holds work nobody has taken.

**Any program signals through the terminal.** A build, a test run, a script of your own: OSC 9, 99 and 777 mark the tab and ring the same bell an agent does, with no hook to install.

**The shell's own prompt marks.** Jump from one command to the previous, select what a command printed, and see a failed command's code on its own line at the right margin — press it and the agent explains the error in plain words and names one thing to try.

**The ports a block listens on, on its header.** Start a server and `:3000` appears; press it and the page opens where you say.

**Asked where a page opens, everywhere.** The port button, the page that opens by itself, "Open a page", a link in the terminal, a pull request and the agent's own browser all ask once per site: here beside the work, in a new tab, in a window of its own, or in the browser — with "remember for this site".

**The shell outlives the window.** Quit, update or crash, and what runs in a block carries on: a keeper holds the shell and the agent, and the blocks come back to them.

**A block over SSH.** Open one by the host's name and the block is a shell on that machine.

**`vobuda events`.** What changes in the window, one JSON line each, followed as it happens; and the whole command line is documented, with a page on what the program does with your machine.

**Pictures in a block.** Sixel and the iTerm2 protocol are drawn where the command printed them.

**Measured before it ships.** Every release carries its own numbers — memory, the delay from key to letter, redraw, search, ligatures, pictures.

**A snapshot before every turn, and "put it back".** The project folder as it was before the agent's turn, and one press to have it back; the snapshots wait in the files panel under "before".

**The fence.** The agent's writes and deletes outside the project folder are refused, "never delete" refuses every delete, and a red line says what was stopped and by which rule.

**The agent's question, in words.** While an agent waits on you, the bar says what it is asking for in a sentence rather than a tool name, in the danger colour when it wants to install, delete, reach the network or use `sudo`.

**What changed, in words.** The files panel says what the agent touched in a sentence, and names in the warning colour anything that looks like your data.

**"My app".** The first time a block starts listening on a port, a page opens beside it on that address; "Show the agent this page" hands the agent a picture of what you see.

**The guard for keys.** A key pasted into a request is stopped before the agent sees it, and a key the agent writes into a file that ships is refused with where to put it instead.

**"What does this mean?"** The failed command's output goes to the agent as a question beside the work: what the error means, and one thing to try.

**The way out of the fix loop.** When the same file has been edited three times in ten minutes, the bar says so and offers the snapshots.

**The limit in words.** After a turn the bar says what share of the week — or of the five hours — it took, and when the tightest limit of your account is nearly spent and returns within the hour, that waiting is cheaper than starting.

**Every limit of your Claude account, in a menu.** Press the limit on the numbers line: the session, the week for all models, and the week of each model by name, with the one counting against you now marked. Settings → agents → The limits turns it off.

**"Put it online", "Put it on GitHub", "Pack for a developer".** Three items in the File menu for the person who built something and wants it out of the folder: the steps handed to the agent under your own account, a private repository through your own `gh`, and an archive with a README on top — with every file that carries a key left out of it and named.

## 0.3.4 — 6 September 2026

**The update goes to the end.** After the installer finishes, the window sees the new version on disk and offers the restart on a strip that cannot be closed away; with nothing running it restarts by itself after ten seconds, "not now" holds it. The restart now actually starts the program again.

**One copy of vobuda.** The install line puts the package where vobuda already is, the running copy first, and removes a second copy left by an earlier install; a fresh Mac gets your own Applications folder, with no password.

## 0.3.3 — 6 September 2026

**The file panel follows the agent's hand.** A file the agent writes shows up, with its git mark, the moment it is written, not at the next poll.

**A failed turn says so.** When Claude Code's turn ends on an error, the light says "failed" and which error, with the message under the pointer, instead of "waiting".

**The block's folder follows the agent.** After the agent's own `/cd`, the file panel and everything that reads the block's folder mean the new place.

**The prompt cache on the numbers line.** "cache · cools in 4m", in the warning colour within five minutes of cooling, "cold" when it is; the hit ratio and the last miss's cause under the pointer.

**The agent's own wait, offered.** When Claude Code stopped on a limit without starting its own wait, one button opens its menu for waiting it out; the window's wait stays the backstop.

## 0.3.2 — 6 September 2026

**Claude Code's own continue comes first.** When Claude Code continues a task by itself after a usage limit, the window's wait stands down and the night's record says so; the window's line goes in only if the agent is still waiting three minutes after the reset, or at once when Claude Code says its own wait ended. Its three notifications about that no longer ring the waiting bell.

**A tab's task name is given once.** A tab named by its task keeps that name until the agent is gone or you rename it; it no longer follows a session name that appears a minute later.

## 0.3.1 — 6 September 2026

**A status line of your own named like ours is kept and called.** The link into Claude Code took any script called `statusline.sh` for its own, so a person who had one saw no numbers line under the bar and no chain to their line; ours is now told apart by its whole path, and theirs is remembered and called after it.

**The same rule for every link.** A Codex `notify` script of yours named like ours is chained rather than replaced, a `notify_…` key of yours is not mistaken for the `notify` line, and a hook you typed by hand as `vobuda signal …` or `vobuda ask` stays where it is; only the lines the window wrote are the window's to clear.

## 0.3.0 — 6 September 2026

**A long command in the shell signals its finish** like an agent: the tab wears a badge, a sound plays, and when the hands are off the keyboard and the mouse the window goes to it by itself; the badge stays until the first key or click there.

**vobuda run.** An agent runs a command in a block of the window, where the person can watch, and gets the exit code back. A block whose command worked closes by itself, a failed one stays with its code; a setting decides.

**Quiet hours, by weekday.** Between the hours and on the days ticked, a signal marks its tab and makes no sound and no notice.

**Hold to talk.** The dictation key held while speaking, let go to send.

**The local models, from the machine.** Ollama's bar lists what is installed; choosing one restarts it with that model.

**The update in place.** The install line runs in a kept block, and the strip offers the restart.

## 0.2.10 — 6 September 2026

**The board of agents.** One press on the light of the bar opens the board: every agent in every window, the waiting first, with what each waits for; a small number beside the light says how many other agents the window holds.

**Tabs named by the task.** A tab nobody named says what its agent is doing, from the session's name or its first request; a request that is only a picture gives no name.

**btw: a question beside the work.** A button on the bar takes a question and hands it to Claude as its own side command, while it works, without disturbing the task.

**What the agent changed.** The file list wears git's marks, "changed N" beside the search shows the marked files alone, and a file's changes open as a block, hunk by hunk, refreshed while the agent edits.

**Recent folders**, offered where a folder is asked for.

## 0.2.9 — 6 September 2026

**A picture opens as a picture.** A screenshot, a chart or a PDF the agent makes opens as a block beside it, fitted to the block; at its own size it is dragged with the mouse and scrolled with the wheel.

**A document opens as a page.** Any Markdown file reads as a page beside the block, with a table of contents for a long one, A− and A+ for the size, and links that lead somewhere.

**A screenshot pasted into a block becomes a file** whose path is typed for the agent.

**Paths in the output are links** to the files they name, at the line, in any alphabet.

**The agent knows what to show.** At the start of every session Claude Code is told, through its own hooks, that it runs inside vobuda and how to open a picture, a page, a file or a web page beside itself; Codex reads the same words from its instructions file. Nothing to mention in a request, no path pasted into the chat.

**Documents do not squeeze the agent.** Pictures and pages take at most two thirds of the row; the block that works keeps the rest.

## 0.2.8 — 6 September 2026

**The agent's numbers on a line of their own.** Under the bar: the model, the context with a bar and a percentage, the five-hour and the weekly limit with how much is used and when each resets. A fresh session shows the account's limits from the newest status line of any session, and its context as 0 %.

**The light tells the truth.** It says "compacting" while Claude compacts its context and counts the helpers it has running; when no end arrives it lets go of "compacting" after ninety seconds instead of five minutes.

**The branch, the copy and the pull request on the block's header**, read from the folder the agent works in, and what Claude's own auto-continue means, said plainly.

**The effort inside the model menu.** Rest on a model and the efforts appear beside it, low to ultracode, the current one lit; one press chooses both. The models and the efforts are named as Claude Code names them in its own picker, and the separate effort button is gone.

**The bar's lists are drawn over the window**, not inside the block: a menu is whole at any width, and a long one scrolls.

**Every button on the agent bar says what it does** under the mouse.

**A settings folder that holds our earlier Claude menus gets the new ones.** A list edited by hand stays as it is.

## 0.2.7 — 5 September 2026

**What is copied is what was selected.** In a block with an agent running,
Cmd+C sometimes gave a strip of the agent's frame instead of the selected
line: the agent repaints its screen in place, and the copy read whatever was
under the selection by then. The text is now taken the moment it is selected
and kept until the selection is dropped.

## 0.2.6 — 5 September 2026

**Copied text arrives as itself.** Text taken out of a block by the program's
own copy — a selection with copy-on-select, Copy in the menu, the block's copy
button, a panel's copy button — reached Telegram and ChatGPT as «–Т–Є–і–Є»
when it was Cyrillic: the clipboard was told the wrong alphabet. Every
alphabet now pastes as it was copied.

## 0.2.5 — 4 September 2026

**A second place to ask for the newest version.** When the download page
cannot be reached, the program asks for the same file in this repository;
a network that swallows one name rarely swallows both. Until now such a
network made the check say it could not check, from the first version on.

**A date in the language of the window.** In the list of past sessions an
older day is written the way the window's language writes it, "Aug 27" in
English, rather than one habit's numbers over another language's titles.

## 0.2.4 — 3 September 2026

**The first question.** On the first run the program asks how you work —
code yourself, with agents, just starting — and shapes the window to the
answer: a quiet look with four icons for a programmer, the full set under
Glass for working with agents, every button and the guide across the window
for a start. Asked once, before the folder; the application menu asks again
on request. A preset over the same files, never a mode.

**Six looks for programmers.** Ink, Graphite, Midnight and Ember dark,
Daylight and Linen light: flat, thin icons, four buttons, each with its own
colours and its own edge for the dock, the file list on the right.

**What changed, once.** After an update a window lists every version and what
each one brought; a cross closes it, the version number in the application
menu opens it again. Never on a fresh install.

**The install line checks whose signature the file carries**, keeps the old
app in place until the new one is copied whole, and refuses a version name
that is not one. A folder cannot run a program by being looked at. A page
block draws only web pages. A pressed update button goes away; a menu of the
agent bar closes when you press elsewhere; the update line opens its own
block beside a busy one.

## 0.2.3 — 3 September 2026

**An installer package.** Beside the disk image there is a `.pkg`: a copy
sent through a messenger opens from it, where the image alone was refused by
macOS. The release asks the messenger's question itself, so a build that
would be refused never ships.

## 0.2.2 — 3 September 2026

**A setting survives an update.** Nothing had ever proved it: the code that
moves an old settings file onto new defaults was trusted by being read, and
reading it says nothing about the version after next. It is now held by a
check — a complete settings file goes through it and every key is compared, and
only what a version's own note names may differ. A file already at the current
version is not rewritten at all.

**Dictation says which language it is hearing.** Two letters on the strip while
the microphone is open — `RU`, `EN` — taken from what the recogniser was
actually asked for. Dictating in a language other than the one you read stays
possible; it is no longer invisible.

**The monitor's address panel names the address the internet sees**, with the
one this machine has on its own network below it, and a copy button on each. It
is asked for at most once in ten minutes, only while the panel is on screen,
and the request carries nothing about the machine.

**And a release nobody was ever offered.** 0.2.1 was built, signed and
downloadable while the file every running copy reads to learn about new
versions still named 0.2.0. The download page and that file are now written by
the same script from the image that is actually there, and a disagreement
between them fails a check.

## 0.2.1 — 3 September 2026

**Read once more as an attacker would**, the morning after the fault receiver
went up. Four things closed before it went anywhere: a version string that
could break the counts inside a report and quietly reopen a closed issue; a
daily budget counted against an identifier the sender chooses for itself; a
receiver address that reached `curl` as an argument, where a leading dash is a
flag and the address can arrive from a settings archive somebody was sent; and
the install line — which works precisely because `curl` leaves no sandbox mark
— being the one road on which no signature was ever checked.

## 0.2.0 — 2 September 2026

**The night nobody is there for.** The machine is held awake while there is
work to do. An agent stopped by a usage limit goes back to work by itself when
the limit lifts — with a switch, and a badge in the morning that says what
happened. Sleep is released the moment the work ends.

**One line that installs and updates**, and a first run that survives whatever
road the file took to the machine.

**Everything a full reading of the program found.** The whole thing was read
end to end and the findings became work: a window that keeps drawing when a
panel throws, a session that arrived from another machine, a menu item that
reaches the window in front rather than whichever answered first, a file
dropped on the window landing where it was dropped, and eight smaller defects
that had been looked for rather than hit.

**A copy of the settings in iCloud Drive** as the default — a copy of the
archive, refreshed when the settings change, not the folder moved with a link
left behind.

## 0.1.2 — 2 September 2026

**The settings folder as one file, and back.** Save everything you have made —
themes, looks, skins, buttons, keys, agents — as a single archive, and restore
it on another Mac. The restore sets the old folder aside rather than deleting
it, and says so before it starts.

## 0.1.1 — 2 September 2026

**Signed by Apple and notarised.** The same program under a number of its own:
a Mac that has never seen it opens it without a word — no "cannot be verified",
no trip through System Settings.

The bump also found a defect in the download page itself, which had promised to
relink a release that was replaced and never did.

## 0.1.0 — 2 September 2026

**The first build handed out.** Six days from the first window to a program
somebody else could install, and by then it had: blocks that split, drag
between tabs and keep their shells; the agent control bar with sessions, skills
models and access read from the agent itself; the system monitor with skins;
a file open beside the shell with colouring for 227 kinds; dictation and reading
aloud through the system's own speech; the command line that drives every part
of the program; settings as a screen and as files; workspaces; the quake window;
and 40 languages with a guide in each.

---

<sub>Dates are the day the build was made. Everything before 0.1.0 was the six
days of building it, and is not a version anybody could install.</sub>
