# What changed, version by version

Every build that leaves this machine carries a number of its own, and every
number is here. Newest first.

The program looks for a new version once a day and says so in one strip; there
is also **Check for updates** in its own menu. Updating is the same line that
installs it: `curl -fsSL https://vobuda.com/install.sh | sh`.

---

## 4.1.2 — 24 September 2026

**The window keeps its shape.** In 4.1.1, pressing Monitor beside a folded block, or opening one block too many, pushed the dock past the edge of the window, and a new block could be squeezed down to a thread. Now only what stands on the screen shares the room, nothing is drawn past the window, every block gets at least its smallest useful size, and what does not fit goes down to the strip, where one press brings it back. A dock taller than its window scrolls instead of squashing its buttons, and the monitor scrolls up and down only.

**The program is a third smaller.** Its binary ships without what only a debugger reads, and the Mac package comes straight from the site again rather than from a redirect.

**Settings are arranged by what you came to do.** Ten sections — General, Appearance, Agents, Protection, Notifications, Voice, Window and panels, Terminal, Buttons and keys, Data and privacy — listed down the left instead of tiles that took half the panel, and a row of icons in a narrow block. The language is the first row of General; dictation has a section of its own; the rare settings of each section are folded under "More settings", and a search that finds one opens it. A shortcut or a command that still names an old section opens where its rows are now.

**Your data in one place.** Data and privacy holds saving the settings to a file, restoring them, the copy in iCloud Drive as a switch you can see, and checking for updates. Searching "backup" finds them.

**The tabs come back after a restart.** The shells went on running when the window closed, and the window did not bring their tabs back. It does now by default; a settings file that held the old default is turned on once, and switching it off again stays off.

**The dock in captioned groups.** Start, See, Voice and Add-ons, with Agent as the one main button in blue, Settings and Help at the far end. Its side, the shape of its buttons and which ones to show are on a right-click on the dock.

**Tabs say what works in them.** A tab you have not named reads "Claude · site" or "terminal · shop", and a dot on it breathes while its agent works. While the Mac is kept awake a ☕ sits at the end of the tabs, and ⏳ with the hour while a limit is waited for; press either to turn it off or open its settings. The project's name stands at the left once you have more than one project.

**An agent's questions in your language.** When Claude asks whether to trust a folder, or whether it may run a command or change a file, a card lies over its block and asks in the window's language — "Yes, it is my folder", "Allow once", "Always allow in this folder". It presses the same keys you would; "Show it as in the terminal" leaves you the agent's own screen.

**One word for one thing.** A window's space is a project everywhere, plugins are add-ons, sessions are past conversations — in the window, the menus, the command line and the guide.

**A greyed button says why.** Rest the mouse on it and the reason is there; the same reason is in `vobuda ui`. In the Design plugin, Save names how many changes it writes, and after saving says "Saved into …" with a button that shows the file in Finder.

**For agents that drive the window.** Every control in `vobuda ui` has a name that stays the same in every language. `vobuda press` refuses when two things answer to one name, and answers with what appeared, went or turned on after the press.

**Smaller things.** Counts under the agents and elsewhere are in the forms your language has ("3 buttons", «5 кнопок»). "Back to how it shipped" in Window and panels puts back the monitor's readings too, and it no longer stands under the results of a search. A section's name wraps rather than being cut. With the tab strip turned off, the first block's header no longer sits under the window's own buttons.

## 4.1.1 — 23 September 2026

**A page can no longer give the program orders.** A site open in the Design plugin, or in any page block, could reach the program's own address and from there call any of its commands — open a folder, run something, write a file. Now a page is let through to exactly what it was given and nothing else; a plugin's panel cannot grant itself a folder; the window puts its helpers only into pages of installed plugins that work on one; and `vobuda set` writes only inside the settings folder. A page sent to the program's address shows that address in its bar instead of the site it came from.

**The model menu waits for the agent.** In the first seconds after an agent starts, a press on a model used to type into a terminal that was not listening yet, or do nothing at all. Now the menu says the agent is starting and keeps your choice until it is ready, then sends it; if the agent never gets ready, it says nothing was sent. The row lit as current is the one the agent is really on, and a row keeps its name when pressed.

**"Keep the Mac awake" shows what is really held.** The row in settings used to show an hour and no screen whatever was chosen, and a touch sent that over the real hold — the time went, the tick went, the screen was let sleep. It now shows the hold as it is and changes only what you changed. The hold can also be found by searching settings.

**Typing a number in settings no longer takes effect letter by letter.** Typing 5000 into Scrollback went through 5, and every open block cut its history down to five lines on the way. A number is written when you finish typing it, and the fields take the same ranges the settings catalogue promises.

**Text reads on every theme and every look.** A look laid over a theme could put its text on its own accent at about two to one; plugin panels drew their quiet text by transparency and kept the colours they were opened under. Every text is now held to 4.5 to 1 after the look is applied, panels follow the window's colours when you change theme, and the grey a shell prints for suggestions and hints is readable: Minimum contrast ships at 4.5. A settings file that held the old 1 moves to 4.5 once; set 1 again and it stays.

**Screenshots dropped into a block stay on this Mac.** Their copies are swept after a week and never go into the settings copy in iCloud Drive. Plugins do not travel in that copy either: each Mac installs its own, and a restore leaves them as they are.

**Saving a file you reach through a link writes the file, and the link stays a link.** Before, the save replaced the link with a plain copy. A working copy whose state git cannot read, or which holds ignored files, is kept rather than removed.

**The Director decides by itself, as the panel says.** It was started asking for a yes on every command. Its workers' reports reach it within seconds whatever the width of their blocks, a worker on Codex asking permission is heard too, a second director gets a name of its own, the panel shows a worker standing on a question as asking, and the Director's role goes when the plugin goes.

**The director's window stays yours.** What you type goes to the director, not to a worker that has just opened beside it. Workers share their column in equal parts, quick jobs open folded into the strip, and the director always keeps at least a quarter of the tab. Workers' reports wait until the line you are typing to the director is empty, so a half-written message is never sent or spoiled; and a worker's question is said only in the bar of the agent that asked, and not once it has been answered.

**The Design plugin, after a restart and on a copy.** After Quit and a new start it binds to the page on the screen, not to the folded site. The agent asked about a copy is given the copy's file, not an address it cannot open. Closing the panel with unsaved changes asks first. A question waits for a busy agent rather than being typed into its turn, and the panel lets the agent's question go when the agent leaves.

**Plugins are taken away cleanly.** Removing a plugin closes its own panels in every tab and no one else's; a failed update puts everything back instead of losing your work, and "your work was kept" says where. The catalog does not offer a plugin the window is too old for, and the daily check no longer makes a plugins folder on machines that never opened one.

**An agent keeps room to work.** Claude started beside a shell used to come up barely wider than its prompt, and every panel opened afterwards took more from it. A block running an agent now keeps a readable width, never under sixty columns, and takes it the moment the agent starts; a shell keeps room to work in as well. A new block is cut out of the widest shell rather than out of a panel, and the plugin catalog opens down an edge. When a row has no room left, its oldest panel, file or page folds into the strip instead of everything being squeezed, and the button of a folded view unfolds it rather than closing it.

**An agent that is not installed says so.** Starting an agent this Mac does not have names it over its block, with the line that installs it and a button that puts that line in the terminal.

**Settings are found by your words.** Settings are found by the words you use, in any language, from the window, the command line and MCP; "Back to how it shipped" puts back exactly what the section shows, to your profile's starting values.

**Smaller things.** "Read the answer out" reads exactly what you selected, in any block or page, even when the terminal redraws under it; a press while something is playing reads the new choice. Ligatures turn on and off in open blocks. Quit is named in the menu's language, and its question is no longer drawn under the designer. A red question mark leaves the tab when the agent that asked has gone. Reading a folder outside the project is called reading, not writing. The drop-down key registers only a whole shortcut. The answer to "how do you work" is kept. Two quick changes to settings no longer lose the first one. `vobuda send` into a block with no terminal says so instead of losing the words. The editor takes the keyboard as soon as its block becomes the active one. The floating settings card and the menu are opaque under every look. The agent panel's buttons are in your language. An address typed over a page that never opened opens there, rather than the refused one again.

## 4.1.0 — 23 September 2026

**A director runs the work for you (a plugin).** Install **Director**, press it, and press "Call a director": your own agent starts beside the panel as a manager, not a worker. Tell it what you need in your own words. Before anything is built it holds a meeting — the people it thinks the task needs, each forming a view before seeing its own — and comes back with what it understood, what it proposes and a few questions in plain words; work starts on your yes. It hires the workers the job needs, writing a role for any specialist you do not have, picks the model for each, and hands you the result. When a worker finishes, its whole answer reaches the director by itself; when a worker stops to ask permission, the director is shown the question and answers what is safe, asking you about the rest. The panel lists every director and its people as they work. One agent is enough, and nothing assumes a method.

**The Design plugin, run in by a second pair of eyes.** Its agent's whole answer reaches the panel even after the question about trusting a folder, and Codex's no longer arrives as half a line. Two designers in two tabs keep a page, a folder and an agent each. Saving a copy again writes in place instead of asking "Save As" every time, a saved copy stands on its own and opens again, and an address typed into a copy's block no longer wipes the copy off the screen. Words a site makes in code are said before you edit them and are never written over; the outline follows every change; the dev server of the folder you work in is found and offered by itself.

**The model menu names the model the agent names.** Opus 5.5 shipped and the menu went on saying Opus 5: the words under Opus, Sonnet and Haiku are now the newest model Claude Code itself was seen running, and the button reads the agent's own status line when its screen has scrolled the banner away.

**A window opened on a sleeping screen, or hidden, starts at its size.** Its first terminal used to come up two columns wide and stay so.

**Saving asks where, and the press is the asking.** The one step that cannot be undone is no longer taken in silence: Save opens the system's own chooser, with nothing in between — no question under the button, no second button, and no line naming the file it would write into. You pick the place and the program writes there; the plugin never reaches the disk by itself. A page of your own project is not asked — its draft belongs to the files it came from, and saving writes them.

**The Design plugin changes what was pointed at, not what is near it.** The words of an element are taken apart into their own runs: a heading of two halves offers two fields, and a colour lands on the one in hand rather than always on the first. Text filled with a gradient finally takes a colour. The field being worked in is outlined and scrolled into view — half the fields "did not work" only because they were below the fold. The palette no longer mixes the colour of letters with the colour behind them: one band per question, with a seam between this site's colours and the rest.

**Two buttons under the panel instead of one.** "Put it back" drops the whole draft, rather than one step of undo repeated on the right element in the right order. "Save" names where it is about to write before it is pressed: the copy's own file, or the very sources the draft is addressed to. And what was saved stops counting as unsaved.

**A copy lives its own life.** It can be copied again, it opens ready to be changed, and after a write it is really read again — the checking used to read the document from before the write and report every change as drawn differently.

**A plugin is entirely outside the program.** Nothing of it ships inside: a catalog, a download checked against its hash on install, and removal to the last byte. A refusal is shown on the catalog row, not only in the log. The dock button goes with the plugin and comes back with it.

**An agent driving the program is told what happened, not that it asked.** `vobuda press`, `vobuda type` and `vobuda point` reach a plugin's panel and the page being designed, and both of those draw in a webview of their own — so the command used to report the message leaving as the deed: `press "Open"` said `pressed "Open"` and exited zero against a panel in Russian that holds no "Open" at all. Now the webview says what came of it and the command waits for that: a press that reached nothing exits non-zero and names what is there to press instead, a control that is off says so, and a press that landed says that. An agent told "pressed" builds its next three steps on it.

**The Design plugin's agent answers in the panel.** You type what you want in the panel and the answer comes back there, under your question, the way a chat reads. Before, the question went into an agent's block and the panel told you to go and look — and when the window held no agent, one opened under the panel to hold an answer you then had to read somewhere else. The agent still runs in a block, because that is where agents run; a block started for a question folds itself away.

**"Read the answer out" reads what you chose.** Select a paragraph anywhere in a block and press it: those words are read, taken from the same place Cmd+C takes them from. With nothing selected it reads the last answer, as it did before.

**The Design plugin takes the window.** Pressing Design folds everything else in the tab down to the strip, so the panel and the page beside it get half each instead of whatever a shell left them; taking a copy folds the page it was copied from. Nothing is closed and nothing is ended — one press on an icon in the strip brings it back, which is also how you put the copy and the original side by side again.

**Any block folds.** Beside the cross there is a second button: the block goes down to a strip, and pressing its icon brings it back.

**A place for plugins, so the program stops growing for people who do not want what is growing.** A Plugins button on the dock opens a catalog; one press installs, one press takes away. A plugin is a folder with an opis and a page, and it runs in a webview of its own — the window's content policy could never have loaded one, and that turned out to be the better shape anyway: a plugin cannot touch the window, cannot bring it down, and cannot reach past what it was given. What it may reach is a numbered surface the window promises for that number alone; a plugin built for another number refuses to load loudly and completely, naming both numbers, because a plugin that half works is worse than one that does not open. Removal is measured rather than inspected — the settings folder is listed before and after — and a person's own work is moved aside and kept, never deleted by a cross. A plugin nobody installed costs nothing: no code in the package, no button in the dock, and the programmer looks' set exactly as small as it was.

**The first plugin: Design.** The site you are building opens beside the agent, you point at something with the mouse and say what you want, and it changes while you watch. Colour, size, spacing, font, alignment and radius are arithmetic — instant, and they never reach a model. Meaning goes to the agent, and its answer arrives as a change you can undo like any other. Nothing reaches a file until you say "keep it"; then the page comes back from the real code, and anything that was drawn differently from the draft is named rather than quietly absorbed. Astro first, Next.js with Tailwind beside it, and everything that knows what a framework is lives behind one boundary two functions wide.

## 4.0.6 — 19 September 2026

**Every effort pill, on every model, for both agents.** 4.0.5 said the effort button changes the effort. It did not: pressing every one of the twenty-nine pills on a live window found three rows that had been dead since the day they were drawn, and one more failure on every row. `default` is not a model — it is the word for whichever model Claude Code recommends, and the agent answers it by naming the model it resolved to, so the row was never confirmed, the level was never sent, and each level pressed on it was recorded as one that model refuses: the row went dead one press at a time. Fable and Opus-with-a-million-tokens went the same way for a different reason — their row sends an identifier out of Claude Code's own list, `claude-fable-5-1[1m]`, and the agent answers `Set model to Fable 5.1`, which shares no word with it. And the first press onto any row whose model has to change lost the level, because Claude Code is redrawing its own switching question when the line arrives. A row is now met by the words written on it, the alias for the recommended model by the agent's own answer to it, and a level that does not arrive is written once more.

**Codex has a model menu that works.** It never had one. The menu sent Codex `/model gpt-5.6-luna high`, which Codex does not take as a command at all — the whole line goes to the model as a prompt, and the model answers it. Once, after searching the web, it answered «Model set to gpt-5.6-luna with high reasoning. This level is supported by the model», and nothing had changed: a confirmation invented, paid for in tokens and a web search. The menu now does what a person does — opens Codex's own picker, reads the rows and presses the number Codex gave the row it wants. Nothing is pressed that was not read off the screen first.

**Each Codex model offers the levels it has.** Codex keeps a different set per model — six for `gpt-5.6-terra`, five for `gpt-5.6-luna`, four for `gpt-5.5` — and the menu drew one model's set under every row, so `max` sat on a row that has never had it.

**The model button says what is running.** It showed whatever had just been pressed until the reading caught up, so it read `sonnet` — the word a command takes — beside `Haiku 4.5`, the model still in force. And the tooltip the system drew over a model row covered the very pills underneath it.

## 4.0.5 — 18 September 2026

**The effort button changes the effort.** Pressing `ultracode` or `xhigh` on a model's row changed the model and left the thinking where it was — and lit up all the same, so the window said one thing and the agent did another. Three faults made it. The two commands went into the terminal back to back, and the second arrived while the agent was still being handed the first, which swallowed it. The button was lit by the press rather than by the agent. And the reader could not see the lines Claude Code actually prints today — it knew the opening banner and `Using <Model>`, not `Set model to <Model>` and not the `◉ xhigh · /effort` hint — so nothing could have confirmed a choice even if it had wanted to. Now the model goes first and the effort only once the agent's own line reports the new model; a row that names the model already running sends the effort alone; and the button looks pending until the agent says the level is set, rather than claiming it in advance.

**Two windows are two windows.** In this toolkit a listener that names no window is reached before any filter, so addressing an event to one window was politeness and not delivery: everything went everywhere. Dictation was typed into the active block of both windows at once. The question before quitting stood in both, and answering one left the other standing. An agent that finished rang, badged and read aloud in both. A page an agent asked for opened over somebody else's work while the window that asked got nothing. The tabs menu listed the last window that spoke while Cmd+1 switched in the window in front, and a window with no waiting work of its own released another's hold on sleep. Every message now names the window it is for and every listener checks; one rule answers whose a thing raised in a block is, and a command nobody comes for within half a minute goes to the window in front rather than sitting in the queue for ever.

**The commands menu opens over one block.** Two agent blocks side by side and the menu of the agent bar — and the "ask in passing" field — were drawn twice, each over the other's content. Which menu is open was kept as one bare name for the whole window, and the bar is drawn over every agent block, so all of them opened at once; a tab that is not in front is hidden rather than closed, and a menu leaves through a portal where "hidden" does not reach it, so the hidden tab's copy came down over the tab in front. The same flatness restarted every agent in the window on one press and opened the find bar in every file. Everything that belongs to a block now names its block.

**No time where nobody wrote.** The column beside a block showed the minute the block opened on rows nobody had written: a window replaying the history it kept, a block coming back to the front, a reflow after a resize, a program taking the whole screen, a `clear` and a repaint, a theme or a font changed under it. A row dated by when its text first appeared took the current minute from every one of those. A repaint is now something the column is told about, and a screen taken in by a repaint is dated not at all — while what the agent really writes keeps its own minute.

**A flood past the scrollback leaves a column that still says something.** 4.0.2 said this was fixed. It was not, and the line of proof under it had not been read since the rule it stood on changed. A flood sweeps the lines the markers stood on off the top, so the marker left over names a row above the screen and every visible row reads as more of the same moment; and a flood begins sixty lines inside one millisecond, so two beginnings a thousand lines apart carried the identical time and the second read as a continuation of the first. The newest row that holds something now takes a marker when a write leaves the screen without one, and a beginning is told from a continuation by the line its marker stands on rather than by the clock.

**Smaller:** the events file is no longer read whole every time a line is added to it; reading the account's limits no longer holds up the thread the window draws through; two long lines written in one breath cannot land their returns in the other order; `vobuda guard` sees `../../etc/passwd` and `~/x` as the addresses they resolve to, which is how their absolute twins were always judged; an installer printing "press enter to continue" is no longer read as the agent being busy; the week's share is counted when the numbers arrive rather than a moment before; and the prompt log is bounded at six hundred instead of growing for the life of the session.

## 4.0.4 — 17 September 2026

**The input line no longer says when the window opened.** Under an answer written at 15:40, the line you type into read 05:33 — the minute the block had started, ten hours earlier. A full-screen program places its cursor and begins no lines, so the column dates a row by when its text first appeared; the input line's text has not changed since the block opened, and that is the moment it answered with. True, and useless. The cursor's row now shows its time only while it is the newest thing on the screen: the line a program is writing this moment keeps its time, and an input line waiting under an older answer shows nothing.

## 4.0.3 — 17 September 2026

**The Integration button no longer sends the agent the tail of its own brief.** Pressing it put a fragment into the block — "re, then carry on." — and nothing else. The brief is many lines, and the press wrote it straight to the terminal, so every newline inside it was an Enter: the agent was sent the brief a piece at a time, and what was left in its input when the return arrived was the end of the last line. The message now goes in as a paste, which is what tells an agent where pasted text starts and ends, and the return follows on its own.

## 4.0.2 — 17 September 2026

**The update strip no longer offers the version you are running.** After updating from the strip, the new copy read the record the old one had written — "4.0.0, latest 4.0.1" — and took that for its own version, so 4.0.1 offered you 4.0.1. The running version is now read from the program itself on every road. Two smaller things from the same minute: the reason of a failed install is what the installer complained of, not its last line of chatter; and the hide button on that failure works.

**No more red boxes on ordinary letters.** Claude Code draws its screen by placing the cursor and never types the space between two words; the marks read that cell as nothing, ran every word of a row into the next, and took "Проект vobuda" for one word with three letters swapped from another alphabet. An unwritten cell reads as the space it is now. The rule for a swap is stricter — a Russian ending on a Latin name, "GitHubе", is an ending — a no-break space counts between two words and not beside a bullet, and the pill counts what is on the screen, not how many times a status line was redrawn.

**The time stands beside what was written, and beside an agent too.** Two faults in the column of 4.0.1. It put a time on every row it could reach — every row of a paragraph, and every blank row below the last line, so a shell holding one prompt carried the same minute down forty empty rows. A row now carries a time when it holds something and begins what was written in that moment; the rest of a paragraph and the blank rows carry nothing. And beside an agent the column was blank altogether, because it took its markers from line feeds and Claude Code sends none — it runs on the alternate screen and places its cursor. Beside a full-screen program a row now shows the minute its text first appeared, so a whole answer carries one time and a line added later carries its own; the history a window replays when it opens stays blank, since when it was written is not known. A flood past the scrollback no longer leaves the column blank behind it either.

## 4.0.1 — 16 September 2026

**A restart after an update saves your files first.** The restart the strip offers goes through without the quit question — that was the fix of 4.0.0 — and the question was the only thing that counted a file typed into and not saved. Now every window is told to save before it is told to leave; nothing typed ends with the old copy.

**A copy with commits of its own is never removed.** A copy of the project is removed when its last block closes and it holds nothing the project lacks. "Lacks" was counted against the project's current branch, and a project checked out at a commit has none — so the count read zero, and a copy with unmerged commits went with them. The count is now against the commit the project is on, which is always there; when even that cannot be read, nothing is removed.

**Two windows saving one file no longer trip over each other.** Every file of the settings folder is written aside and renamed into place; the aside name was one per file, and two windows writing at the same instant shared it. Each write now has a name of its own.

**The awake holds survive a crash mid-write.** The one file of the folder written in place is now written aside and renamed like the rest.

**A run block closes under fish too.** The block types the command and then a line that reports its exit code — spelled `$?`, which fish does not have: fish refused the whole line, the command never ran and the block never closed. The program now asks which shell it starts and spells the code the way that shell does.

**`vobuda run` keeps your quotes.** `vobuda run grep 'a b' f` ran `grep a b f`: the arguments were joined with spaces. An argument with a space or a quote in it now reaches the block in single quotes, which every shell reads alike.

**A long line is long in letters, not in bytes.** A command of 61 Russian letters was treated as a long line and had its Enter typed apart; the count was in bytes, and a Cyrillic letter is two.

**An open file takes a new theme at once.** A theme or a font changed in the settings left every open file in the old colours until it was closed and opened again; now the change reaches the open view, and the cursor stays where it was.

**A tab remembers where you were.** Switching to a tab and back landed in its first block, every time; now it lands in the block you left, and a block moved to a tab lands beside that one.

**"5 min ago" in your language.** The list of past conversations carried that one English line beside every entry, in forty languages. The four spans are in the dictionary now.

**The settings say where a site opens, in the right words.** A site remembered as "in a new tab" or "in its own window" was listed as "In the browser".

**A new agent never overwrites another.** With `agent1` and `agent3` left after a deletion, "New agent" made `agent3` again and wrote over the survivor; it takes the first free name now.

**999 999 tokens read "1M", not "1000k".**

**An older settings file keeps every default.** A file naming one field of a section — the voice, the pages, the limits — used to lose the rest of that section's defaults silently; every section is topped up now.

**A signal from a block marks that block's tab.** `vobuda signal done` — and through it the agents' hooks — marked whatever tab was in front; the signal now names the block it came from. And one rule for the sound: silent while you are looking at that tab, quiet in quiet hours, off with signals off — the same on every road a signal takes.

**Read-aloud reads the agent that finished.** With two agents it read the block in front, which was the wrong one half the time.

**The MCP server names the version that installed it.** It carried a copy of its own, bumped by hand — and on the day 4.0.1 began it still said 4.0.0.

**The effort button names its own model's effort.** With settings for both `claude-opus-5` and `claude-opus-5[1m]`, "opus" could show the other one's; the exact name wins now, and a Codex profile's model is no longer read as the default.

**A page reopened on the same block says so when it never loads.** Only a page made fresh was watched; a second address that never arrived left a blank and no word.

**Smaller:** the menu's memory is written once the menu is on the window, not before; a file git reports as a copy no longer leaves a mark on its source; the first disk reading is no longer the total since boot; a refused dictation phrase no longer leaves the microphone running.

**The time beside every line.** An agent writes screens of text and nothing says when; scrolling back, a line from the morning looks like one from a minute ago. A column beside the block now shows the minute each line was written — bright where the minute changes, the seconds under the mouse — and stays out of every copy. Under the terminal's settings, on by default.

**The invisible in the text.** What a machine can put into a text and an eye cannot see — zero-width characters, special spaces, soft hyphens, direction marks, hidden tag characters, a letter of another alphabet swapped into a word — is marked over its cell and counted on the block's header; the pill lists the kinds, copies the text with the hidden taken out, and hands the selection to the agent to be rewritten as a person would write it. A model's typographic habits are counted apart as tells, never as a verdict; a watermark nobody can see without its key is not looked for. Under the terminal's settings, on by default.

**Show in its folder.** A picture, a document or a file open in a block has a button that opens Finder at the file's folder with the file selected — to copy it, move it, or see what lies beside it. Before, there was only "open in the system".

**A folder's link opens the folder.** Pressing the path of a folder in an agent's answer opened an editor that could only say it was a folder; now the folder opens in Finder, and a file opens in the block as before.

## 4.0.0 — 16 September 2026

**The restart after an update starts the new copy.** Updating to 0.3.13 installed it, the strip offered a restart, and the copy that kept running was the old one — with the strip asking again: the restart asked the program to quit, the quit waited for its question about the work still running, and a second later the system was told to open a program that had not gone, which only brought the old one forward. The restart now goes through without the question, waits for the old copy to end, and only then opens the new one.

**The numbering starts again at 4.0.** After a day with 0.3.12 and 0.3.13 one after the other, and a Linux package rebuilt under the second, the count begins clean here.

## 0.3.13 — 15 September 2026

**A setting is found by what it does.** The settings screen has a search field: type "pasted key", "font", "notice" or the key as the file spells it, and the rows that match are listed with their section, their title and a line about what they do; one press opens the section and lights the row. Every setting has such a title and line now, in the window's language.

**Four things the window did have a switch.** Right-to-left drawing of a row, file paths made into links, the question of where a page opens, and the system notice when an agent finishes each have a row of their own; before, the only way to turn one off was a text editor.

**The command line knows the settings.** `vobuda settings list` names every setting with its meaning, kind, choices and current value; `settings set <key> <value>` changes one, and the window applies it at once. A value of the wrong shape is refused with the reason, so a setting is never set to a word the program does not know.

**The program is a set of tools for the agents.** `vobuda mcp` is an MCP server, registered with Claude Code and Codex at start: the settings by meaning, the actions by name, the screen by what is on it, a screenshot, a wait, the log. "Make the letters bigger" or "stop blocking my keys" said to the agent now ends in the setting changed, not in a path to click.

**An Integration button on the tab bar.** One press puts the links for both agents in again — hooks, status line, skill, MCP server — and tells the agent in this tab, in its own input, what the window can do and how to ask. For an agent that was already running when the program was installed, or a person who wants to be sure.

**Quit asks once.** With a project window per project, quitting put up "something is still running" in every window, one after another, and only then closed the program. Now the one question comes up in the window you are looking at, with every window's running work and unsaved files in its list; Stay keeps everything, Save and quit saves in every window.

**On Linux, the menu at the top stays open.** The bar was rebuilt ten times a second by the settings watcher, and on GTK a rebuilt bar closes the menu you had open; people saw menus that vanished under the pointer. A menu is now rebuilt only when the language, the shortcuts or the tabs changed. (Linux packages rebuilt under this number.)

**On Linux, Quit quits.** The Quit item had no action at all on GTK, so Ctrl+Q and the menu did nothing. It now asks the core for the exit, which asks its one question first. (Linux packages rebuilt under this number.)

**The command line hears a project window.** With a project window in front, `vobuda ui`, `press`, `type` and `shot` waited five seconds and heard nothing: the window in front took the command and answered into its own state file, and the command line read the main window's alone. An agent working in a project window can drive it again.

**A page opens on the server's port by itself, in a second and a half.** Starting a server and pressing Enter opened the page six seconds later, or not at all: the three quick looks after Enter all read the same one-second-old list of processes. The looks are spaced so that at least one sees a fresh list.

## 0.3.12 — 15 September 2026

**Hebrew and Arabic read right to left in the block.** A Hebrew word typed after a prompt came out backwards, and switching the keyboard did not help: the terminal drew each letter at the column it was typed in and knew no right-to-left. Every right-to-left run of a row is now drawn as one piece, in reading order, and Arabic letters take their joined forms. What the shell, the cursor and the copy see is unchanged.

**A font that has those letters.** No monospace font on a Mac carries a Hebrew or an Arabic letter, so they came from whatever the system found, one squeezed glyph per cell. The program now ships Cascadia Mono for exactly those letters; your own font still draws everything it has.

**The model button no longer reads a file name.** On a Claude Code block it once said `its-420.png · xhigh`: a line that happened to have the shape of Codex's status line was read as one. Each agent's screen is now read by that agent's shape only.

**A review of the whole program, and fourteen faults from it.** On 15 September the whole program was read end to end — the window, the core, the command line and the hooks — for faults of the kind above and for plain logical ones. The ones confirmed are fixed here; the rest are written down with the contracts.

**A fresh shell no longer carries the agent's session.** Claude Code began exporting one more variable about the session that started the program, and every shell in a block inherited it. The live sweep caught it; the list knows the name.

**Past conversations and the limit's return are found under a folder with any name.** The agent names a project's folder with a dash for every character that is not a Latin letter or a digit; the program replaced only three, so a project under a Cyrillic folder — or one with a space — had no past conversations to show and no transcript to read the limit's return from.

**A core crash is recorded again.** A second hook installed at start replaced the one that writes a panic down as a fault; the panic reached the log and never the report.

**A setting turned back on survives an update.** The one-time step that turns off "restore the session" ran for every file below the current version, not only for files from before it.

**One busy flag per block, not per window.** With two agents open the window's one flag flipped between them every second, wiping every badge; now the flag is the block in front's, and an agent that resumes clears its own tab only.

**The files panel walks on from a folder it was sent to**, and a deleted folder no longer sends it in circles. The folder you walked to is the one that comes back with the session.

**Quit asks about an unsaved file.** It asked about running work alone; with idle shells and an edited file it ended the program without a word.

**A shortcut can be recorded again.** The keys screen took the modifier itself as the whole combination and wrote `cmd+metaleft`.

**A merge that conflicts puts the project back as it was**, instead of leaving conflict markers and a merge in progress behind one press.

**A file in another encoding is refused, not rewritten.** Opened leniently and saved, a Windows-1251 file lost every letter outside ASCII.

**Putting a snapshot back leaves the index alone**: nothing that was untracked comes back staged.

**"Bring the page back" brings back a page that left**, never one still in the layout beside it.

**Stopping the agent finds the agent**, by what the process is now and on every branch of the tree, not by the name it was born with.

**The panel resumes a conversation the agent's own way**, from the file that declares it, and in a block of its own when the block in front is busy.

**Prompt marks in bash sit where they belong** when your profile has a precmd of its own: selecting a command's output no longer starts at the prompt above it.

## 0.3.11 — 14 September 2026

**The update notice is back for Claude Code and Codex.** The daily check looked for both where the app itself was started — Finder's four system folders — and found neither, so it said nothing while both fell releases behind. It looks where your shell looks now, and the line it offers matches the way the program was installed: npm, Homebrew, or Claude Code's own `claude update`.

**An agent installed after vobuda is wired too.** The hooks and the status line were set up once, on the first start, and an agent that was not there yet — or had never been run — was skipped for good: no numbers under the bar, no signal when it finished. They are set up the moment the agent is there, and again just before the window starts one.

**The files panel does not go blank when its folder disappears.** A folder renamed or deleted under the panel left it showing nothing at all. It moves up to the nearest folder that still exists and says which one is gone.

**The model menu offers what your account has.** A model out of Claude Code's cache — Fable on a Pro plan — was on the list, and choosing it was an error. The list is checked against your account's own limits now.

**The restarted program comes back in front.** After an update the program came back behind every other window, and looked as if it had not come back at all. It comes to the front.

## 0.3.10 — 8 September 2026

**A page asked for from another window opens.** Every command carries the block it came from, so that an agent showing a file puts it beside its own work. When the sender was in a *different* vobuda window — which is exactly what happens when an agent working in one window drives another — the page was split off a block this window does not have, and nothing opened at all: no error, no block, nothing to look at. It opens beside the block that is here now.

## 0.3.9 — 8 September 2026

**vobuda runs on Linux, and on far more of it than before.** A `.deb` and an `.AppImage` for both Intel and ARM machines. The AppImage needs nothing installed at all: make it executable and open it — the webkit it draws with travels inside the file. Built on Ubuntu 22.04 rather than Debian 12, which is not a detail: a package runs on the system it was built on and everything newer, never on anything older, and the old base quietly left out Ubuntu 22.04 LTS — the commonest desktop Linux there is, supported until April 2027. It now opens on Ubuntu 22.04+, Debian 12+, Fedora 36+ and openSUSE Leap 15.6+.

**Nothing is offered that your system cannot do.** Dictation and reading aloud are macOS speech services. On Linux and Windows their buttons are gone from the dock, their items from the menu bar and their section from the settings, instead of sitting there doing nothing when pressed.

**The first question no longer leaves an error in the terminal.** Answering "keep it here" sent the shell `cd '~'`, and quoted like that it means a folder literally named "~" — so the shell answered "No such file or directory" under the very first prompt. It goes to the home folder now, and a folder with a space in its name still works.

## 0.3.8 — 8 September 2026

**Commands come back twice as fast.** A command run from the command line took 600 ms to answer; it takes 281 ms. Most of that was the program waiting on itself — reading a file twice a second, and sleeping four hundred milliseconds before typing anything into a fresh block on the assumption that a shell needs the time. A shell that has written its prompt is ready, and it says so by writing.

**Output arrives three times faster.** Everything a command prints, from the shell to the screen, at 3.8 MB/s where it was 1.1.

**Snapshots have one switch instead of three.** How many to keep and how large a folder may be were questions nobody could answer from a screen; they keep sensible values and live in the settings file.

**Quiet hours read straight.** The clocks, "all day" and the seven days line up where you would look for them, and each interval can be taken away.

## 0.3.7 — 8 September 2026

**Updating happens inside.** The installer no longer opens a terminal of its own for you to watch: the program updates itself and says one thing — installing, then restart. What the installer said is in the log, where it belongs.

**Restarting is one question, and it is the same program that comes back.** With several windows open it used to ask about each of them in turn, and then start a second copy beside the one that quit. It asks once, the windows come back as they were, and the program that starts is this one.

**No offer of the version you are already running.** The daily check kept what was true when it ran, and went on offering an update that was already installed.

**A dragged screenshot survives the drag.** The thumbnail in the corner hands over a file the system deletes a moment later; it is kept now, and the agent gets a file that is still there.

**A picture reaches the agent as a picture.** Paste or drop a screenshot into a block where Claude Code is working and it arrives the way it used to — one line in the input, and the picture read with the turn — instead of a long path typed into the prompt.

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
