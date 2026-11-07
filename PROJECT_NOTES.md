# CookieRun Classic Bot: project notebook

Working log kept by Claude for this project. Update it after every change, finding or decision.
Entries marked **(verified)** were observed directly. **(unverified)** means assumed or inferred.

Last updated: 2026-10-10 ~14:52

---

## 1. Current status

- Bot runs from a Command Prompt: `cd C:\Users\leoni\Desktop\cookierun-classic-bot-main` then `python main.py`.
- Last observed state (14:44): **hung** since 14:40:43 in the friend-lives routine (K10). Fixed in code by C7; the user must restart the bot (Ctrl+C, `python main.py`) to get it running and to pick up C7.
- Earlier, 12:44: running and healthy, mid-run. **(verified)**
- Options used at the 12:37 start: Fast Start, Cookie Relay, HP Extension, Power Jelly, Double XP, Desired Random Boost = Double Coins. Relic detection was not seen in the log. **(from console log)**
- Game progress seen by Claude: level 22 at 10:45 to level 25 at 12:43; coins 27k to about 178k.
- **The PC has C1 + C2 + C5 + C6 + C7** (port, top-row boosts, auto-jump, stop jumping after relay, lives-loop timeout). C7 deployed and verified byte-for-byte at ~14:52.
- **Experiment result (user, 13:50): auto-jump raised coins per run by about 30%.** Auto-jump is now a keeper, not just an experiment.
- C3 (stuck-screen screenshots) was drafted and tested offline but **not deployed**. C4 (restart the app when stuck) is kept as a viable alternative; not built.
- K1 fix (second main-menu template for other tabs) was coded but **set aside, not deployed**, when the user switched to the auto-jump experiment. Design kept under K1; needs re-coding from the PC copy.

## 2. Environment

| Item | Value |
|---|---|
| PC | Windows, host name "robert", user `leoni` |
| Project folder | `C:\Users\leoni\Desktop\cookierun-classic-bot-main` |
| Python | 3.11 (`...\AppData\Local\Programs\Python\Python311`) |
| Packages | numpy 2.4.6, opencv-python 5.0.0.93 (installed with `pip install numpy opencv-python`; `requirements.txt` pins numpy 2.5.0 / opencv 4.13.0.92, which were not used) |
| Emulator | MuMu Player 12, Android 15 |
| Bot's instance | index **2**, name "Cookie Run", ADB `127.0.0.1:16448` (instances 0 "emu1" and 1 "emu2" exist but are not running) |
| Find the port again | `"C:\Program Files\Netease\MuMuPlayer\nx_main\MuMuManager.exe" info -v all`, then read `adb_port` of the instance with `is_android_started: true` |
| Monitors | Emulator is on the side monitor (label `LQ173M1JW04`). Bot console and Claude are on the main monitor (`LG ULTRAWIDE`). |
| Resolution | Bot needs 1280x720. The instance reported `Physical size: 1080x1920`. Claude gave `wm size 720x1280` and `wm density 240`. The user's run afterwards detected screens fine (main menu scored 0.96), but the screencap shape `(720, 1280, 3)` was never explicitly confirmed. **(unverified)** It may reset if the emulator restarts. |

Claude's screenshot coordinate conversion (only for reading screenshots, not used by the bot): the game viewport on the side monitor spans about x 79-1377, y 46-777, i.e. about 1.0145x the 1280x720 game space. `screen = 79 + gx*1.0145`, `screen = 46 + gy*1.0145`.

## 3. How Claude works on this machine (gotchas)

1. **No shell on the PC.** `device_bash` fails with "Workspace unavailable". Command Prompt/terminals are click-only for computer use (no typing), so the user runs every command. Files are edited by staging them from the PC, editing, and committing back.
2. **Commit lag bug (important).** Twice, `device_commit_files` reported success but wrote the previous version, because it ran right after the file was copied to the outputs folder. Always: copy, wait about 8 seconds, commit, then verify with `device_list_dir` (byte sizes) or by re-staging and comparing md5. This also explains the earlier "port reverted to 16384" incident. It was not the user.
3. **Computer-use access expires** after 30 minutes of inactivity. Re-run resolve/request access. The emulator window is drawn by `mumunxdevice.exe`, which must be granted along with MuMuPlayer or the window is masked. Command Prompt is view-only.
4. A running bot has already imported its code. Edits to the `.py` files take effect only after the bot is restarted (Ctrl+C, then `python main.py`).
5. Claude's local copies of the project files are scratch space. Stage fresh from the PC before editing, and after every commit read back the sizes (`device_list_dir`) to confirm the PC has what was intended.

## 4. What the bot does (read from the code)

- It is a "smart macro". It never plays the run (no jump/slide logic). It recognises screens by OpenCV template matching on `adb screencap`, and taps buttons at fixed 1280x720 coordinates with ±15 px jitter.
- Handles the menu loop: purchase items, start, relay, finish, mystery box, congratulations, level up, relic, daily check-in, league screens, anti-bot card puzzle, connection lost / inactive (restarts the app).
- Waits 30-60 s between games, receives/sends friend lives about every 30 min, restarts the app every 1.5-3 h.
- The whole loop sits in one `try/except`: any unhandled error prints "An error occurred" and ends the program. There is no auto-restart.
- Detection runs in groups (PRE_GAME / IN_GAME / POST_GAME). A full scan of all stages runs as a fallback after 60 s / 300 s / 30 s with no match.

## 5. Changes we made (chronological)

### C1: ADB port (config.py), 2026-10-10 ~10:35
- `DEVICE_PORT` 7555 changed to **16384** (README default) and later to **16448** (the real port of the running MuMu instance 2). The 16384 attempt was refused. **(verified)**

### C2: Top-row boosts: HP Extension, Power Jelly, Double XP, 2026-10-10 ~12:30-12:45
- New startup prompts (after Cookie Relay): HP Extension, Power Jelly, Double XP, each "(auto-activate)? [y/n]".
- Files: `config.py` (coordinates + detection constants), `actions.py` (`_boost_is_checked`, `_ensure_boost_checked`, `activate_hp_extension`, `activate_power_jelly`, `activate_double_xp`), `bot.py` (prompts, options dict, calls in the PURCHASE_ITEM handler, before Fast Start).
- Tile centres (1280x720 space): HP Extension `(235, 440)`, Power Jelly `(385, 440)`, Double XP `(535, 440)`. Same columns as the bottom row (Fast Start 235, Cookie Relay 385, Random Boost 535 at y 600). Order is left to right as the user named them; the middle tile's icon looks like a pocket watch.
- **How it works:** tapping a top-row tile *toggles* its "check to activate automatically" box. The bot samples the tile colour (yellow, hue about 27 = checked; green, hue about 45 = unchecked; threshold 36) and taps only if unchecked, then re-checks. Answering `n` leaves the boost as it is (never unticks).
- **Design history:** the first version was tap-then-Buy, copied from the bottom row. Live testing showed that would untick active boosts and buy extra copies, so it was rewritten. Buying is not done; the game uses stock first.
- **Verified:** detection was tested offline on three real screenshots (all checked / HP unchecked / restored) and correctly read each state, with the bottom-row controls reading unchecked. Live log at 12:37 showed "Power Jelly activated" and "Double XP activated". At 12:44 it showed "already active" for all three. **(verified)**
- **Unverified:** that the game auto-buys at run start when stock is 0 (the checked pocket-watch tile showed an 800 price). Check the coin count after a run with zero stock.
- Calibration note: the user's first test tap on HP Extension toggled it off, and Claude toggled it back on. All three were checked again afterwards.

### C3: Stuck-screen screenshot (hang detector), 2026-10-10 ~12:55. DRAFTED, TESTED OFFLINE, NOT DEPLOYED
- Status: not on the PC. The user asked to go further (C4: restart the app when stuck). The code below is a good base for C4's detection part, because it already has the "unknown for too long" timer, per-group limits and tests.
- Goal: when the bot sees no known screen for too long, save a screenshot so the cause can be diagnosed (this is how we'd have caught K1 without watching the monitor).
- Files: `config.py` (`STUCK_SCREENSHOT_AFTER`, `STUCK_SCREENSHOT_REPEAT`, `STUCK_SCREENSHOT_MAX`), `debug.py` (`save_stuck_screen`), `bot.py` (tracking in the main loop, right after the recovery scan).
- **Rule:** "unknown" = no stage recognised on a frame. A timer starts at the first unknown frame and resets whenever any stage is recognised. When it passes the limit for the current detection group, the bot saves the current screen. Limits: PRE_GAME 120 s, POST_GAME 120 s, **IN_GAME 600 s** (a run itself shows no known screen for minutes; a normal run seen was about 2m40s). Repeats every 300 s while still stuck; stops after 40 captures per bot run (disk cap).
- **Output:** `debug_screens/stuck_<GROUP>_after-<LAST_STAGE>_<YYYYMMDD_HHMMSS>.png` (full 1280x720 capture) plus one line per capture appended to `debug_screens/stuck_log.txt` (time, group, last recognised stage, seconds stuck, filename). The console prints a `📸` line. `debug_screens/` is already in `.gitignore`.
- **Safe by design:** a failed save prints a warning and the bot carries on (it never raises).
- **Not covered:** a screen the bot *does* recognise but where its tap does nothing (it would loop on the same stage). That is not an "unknown screen", so no capture. Also it only captures; it does not recover (recovery for K1 is still planned).
- **Verified (offline):** drove the real `bot.main()` with a fake clock and scripted screens: first capture at 120 s then every 300 s; timer resets when a stage is seen; last-stage label correct; IN_GAME silent for 170 s gives no capture, IN_GAME silent for 700 s gives one at about 600 s; cap of 40 respected; file written, reads back identical, and log line correct; failing save returns None without raising. **Not yet seen live on the real emulator.** (unverified live)
- Claude's local scratch copies of `config.py`, `debug.py` and `bot.py` contain this draft. **Always stage fresh copies from the PC before the next edit**, otherwise the undeployed draft would be committed by accident.

### C4: Restart the app when stuck on an unknown screen. PLANNED (user's idea, 2026-10-10 12:52), not started
- Idea: when the bot has seen no known screen for too long, it force-stops and relaunches CookieRun (existing `device_reset_app`, already used for CONNECTION_LOST and the 1.5-3 h session reset), then goes back to the main menu and carries on. Would end the "perpetual hang" class of problems (K1, K4).
- Reuse: the C3 timer/limits, plus the CONNECTION_LOST branch of `bot.py` (it calls `device_reset_app`, waits, `close_announcement_dialog()`, resets timers and state).
- **Agreed/proposed safeguards** (see "Design notes" below): save a screenshot *before* restarting (so we still learn what the unknown screen was), cap consecutive restarts and then stop instead of looping, longer grace period after a restart, keep the IN_GAME limit long.
- **Open question: does login after restart work on this setup?** Unverified. The restart code path has never been seen running here (no CONNECTION_LOST or session reset has occurred yet). Proposed first step: a manual one-time test of `device_reset_app` while the bot is stopped, with Claude watching the emulator to see what screens appear (title screen, login, announcements, update prompts).

**Design notes (Claude's thoughts, for when we build it):**
1. The restart machinery already exists, so this is mostly "detect stuck, then call it".
2. Biggest risk is a **restart loop**: if the unknown screen survives a restart (login prompt, forced game update, server maintenance, terms dialog, account problem), the bot would restart forever and keep hitting the login. Needs a cap on consecutive restarts (about 3), growing waits between them, then stop and leave the last screenshot.
3. **False positives:** a run shows no known screen for minutes (about 2m40s seen), and app launch/loading is slow. Keep IN_GAME at 10 min; PRE/POST at 2-3 min; start the timer only after the post-restart wait (give about 3-4 min grace after a restart).
4. Restarting mid-run forfeits that run (acceptable).
5. K1 (wrong tab on the main menu) is the most likely trigger right now. A template fix for K1 is cheaper and avoids a needless restart; the restart is the general safety net for everything else. Doing both is best.
6. Does not help when ADB/emulator itself dies (K3 still needed).
7. After a reset the main loop sets `pending_send_friend_life = True` but the CONNECTION_LOST branch does not. Decide which behaviour the stuck-restart should use.

### C5: Auto-jump during runs (experiment), 2026-10-10 ~13:35. DEPLOYED
- User's hypothesis: tapping Jump continuously during a run will raise coins per run a lot. This is an experiment to test that.
- New startup prompt (after the desired-boost question): `Auto-jump during runs (experiment)? [y/n]`. Answering `n` keeps the old behaviour (no taps during a run).
- Files: `config.py` (`JUMP_BUTTON = (170, 630)`, `AUTO_JUMP_INTERVAL`), `actions.py` (`jump()`), `bot.py` (prompt, option, jump logic in the main loop, per-run summary).
- `AUTO_JUMP_INTERVAL`: first (0.9, 1.2); changed to **(0.6, 0.85)** at 13:40 at the user's request. Note: the jump check runs once per main-loop pass, and each pass includes an `adb screencap` (likely several hundred ms on this setup, unmeasured). So the real gap between jumps is at least one loop pass and may come out longer than 0.6-0.85 s. Compare the logged `jumps` count against the run time to see the real rate.
- **Rule:** jumps only while the detection group is IN_GAME (from Play to the results screen) **and** the current frame shows no known screen, so it never taps over the Fast Start / Cookie Relay prompts or the results screen. One tap each 0.9-1.2 s (random). Taps get the usual ±15 px jitter.
- **Jump button:** measured from a full-size in-run screenshot (12:29). The ring is centred near screen (250, 685) on the side monitor, i.e. (170, 630) in 1280x720 space, with a radius of about 100 px.
- **New per-run line (both modes):** at the results screen the console prints `⏱️ Run time: Ns (from Play to results)` and, with auto-jump on, `, jumps: N`. Use this to compare runs.
- **Verified (offline):** drove the real `bot.main()` with a fake clock through a scripted run (loading, GAME_START, about 60 s running, GAME_RELAY, about 30 s, GAME_COMPLETE, post-game). With auto-jump on: 86 jumps, all between Play and results, none on frames showing a known screen, gaps 0.95-1.2 s outside the prompts, summary printed with the matching count. With it off: 0 jumps, summary printed without a jump count. **Not yet seen live.**
- **Unknowns / risks:** (1) the interval may be shorter than the cookie's air time, which turns taps into double jumps; tune `AUTO_JUMP_INTERVAL`. (2) Constant jumping may *hit* high obstacles or skip low coin lines, so it could also lower coins. That is the point of the experiment. (3) In the moment between the run ending and the results screen being recognised, one stray tap can land at (170, 630) on whatever screen is showing. (4) If the results screen were ever not recognised, the bot would keep tapping until the 300 s IN_GAME fallback scan finds the next screen.
- **How to measure:** run several games with auto-jump off and several with it on, same cookie, boosts and options. Note the coins on each results screen (or the coin balance before and after a batch), plus the logged run time. Boost purchases cost the same per run in both modes, so they cancel out.

### C6: Stop auto-jumping once the Cookie Relay starts, 2026-10-10 ~13:55. DEPLOYED
- Why (user): the second (relay) cookie is only there for its passive +25% coin bonus, not to extend the run. Ending the run soon after the main cookie is done is the desired behaviour, so jumping must not keep the relay cookie alive.
- How: when the GAME_RELAY screen is recognised, the bot records the time (`relay_seen_at`) and auto-jump is off for the rest of that run. The relay itself is still used as before (if Cookie Relay is enabled). Resets at the next Play and at the results screen.
- Switch: `STOP_JUMPING_AFTER_RELAY = True` in `config.py` (set False to jump through the relay again). No new startup question.
- Console: prints `🦘 Relay started. Auto-jump stopped for the rest of this run.` once per run. The run summary now includes `relay at Ns` (seconds from Play to relay), e.g. `⏱️ Run time: 94s (from Play to results), relay at 64s, jumps: 80`.
- **Verified (offline):** two back-to-back scripted runs: run 1 (relay at 70 s) had 80 jumps before the relay and 0 after; run 2 (no relay) had 50 jumps, showing the stop resets per run. No jumps outside runs or on known screens. With the switch False, jumping continued after the relay (38 jumps), with no stop message. With auto-jump off: 0 jumps, summaries still show the relay time. **Not yet seen live.**
- Limitation: relies on the GAME_RELAY screen being recognised. If it is ever missed, jumping continues through the relay, which is the C5 behaviour.

### C8: Built-in coin ledger, 2026-10-12 ~15:20. CODED, needs a bot restart
- Coin tracking moved into the bot (`coin_ledger.py`); it always runs and can't be turned off. `coin_tracker.py` is retired (a stub), so don't run it.
- **`records.csv` (project root) is the one record to read:** one row per run with version + note, coins earned, run time, relay time, cycle time, coins/s, jumps, balance, extra lives, plus running avg coins/run and coins/s for that version and lifetime coins. Only `ok` / `backfill` / `legacy` rows count toward averages; `multi`, `incomplete`, `suspect` and `unread` are kept for the record.
- Versions: at boot the settings + `VERSION_NOTE` (config.py) are fingerprinted; any change opens a new version (V1, V2, ...). The internal registry with diffs is `ledger/versions.csv`. Update `VERSION_NOTE` for changes the bot can't see (treasures, cookie, pet).
- Each bot session takes a fresh starting balance at its first menu visit, so coins spent by hand while the bot is off never show as a loss.
- Report: printed at boot, or run `python coin_ledger.py`. Past data backfilled as V1-V4 (V4 = jump 0.3-0.55 s).
- Coin reads need two agreeing OCR reads on fresh main-menu frames and run in a background thread.

### C7: Time limit on the friend-lives wait (fixes K10), 2026-10-10 ~14:52. DEPLOYED
- Where: `handle_quick_receive_and_send_lives()` in `actions.py`; new `LIVES_WAIT_TIMEOUT = 60.0` in `config.py` (FRIEND LIVES section).
- What: after tapping "receive all", the wait for the "all lives received and sent" popup now gives up after 60 s instead of looping forever. It prints `⚠️ 'All lives received and sent' not seen within 60s. Giving up on lives for now.` and returns to the main loop, which retries lives on its normal ~30 min schedule.
- **Careful close:** on timeout it taps the mailbox close button **only if the main menu is not showing**. On the main menu that same spot `(1130, 87)` overlaps the Party Run button, and the 14:40 hang ended with the game already back on the main menu. Prints `Closing the mailbox...` or `Already back on the main menu.`
- Unchanged: the normal path (popup appears: confirm, close), the send-life confirm taps, and the "no lives to receive" early exit.
- **Verified (offline, fake clock, 0.4 s per screenshot):** (A) popup at 5 s: normal finish, no timeout; (B) popup never appears and the main menu is showing (the 14:40 situation): gives up about 61.5 s after receive-all, **no** close tap; (C) never appears, mailbox still open: gives up, taps close; (D) send-life confirms then popup: confirms tapped, normal finish; (E) no lives: early exit unchanged. **Not yet seen live.**

### C9: Auto-jump on its own thread, 2026-10-30 ~17:45. CODED, needs a bot restart
- Why (user): lowering `AUTO_JUMP_INTERVAL` barely changed the real jump rate. Tapping was tied to the main loop, so the gap could never beat one pass (screenshot, detection, tap, 0.1 s sleep). V13 was set to 0.10-0.25 s but really jumped every ~0.78 s (348 jumps before the relay at 272 s). `adb shell input` only costs ~75 ms, so the screenshot and detection were the limit.
- How: `AutoJumper` in `bot.py` taps on a daemon thread, timed from the start of each tap. The main loop only calls `resume()` or `pause()` after each detection. `pause()` waits for any tap in progress, so a jump can't overlap a stage handler's tap. The rules from C5/C6 are unchanged.
- **Verified (offline, fake tap of 75 ms):** gaps 0.101-0.250 s, average 0.169 s, jump count correct, no taps while paused. **Not yet seen live.**
- **Risk:** the bot still only sees a new screen once per pass. Taps keep landing at (170, 630) until the screen is recognised, so several stray taps can now land where C5 risk (3) expected one. C5 risk (4), an unrecognised results screen, also taps faster now. What sits at (170, 630) on those screens has not been checked.
- To tell if it worked: `jumps` in `records.csv` should be far higher for the same time before the relay, around 5-6 per second.

## 6. Known issues

| # | Issue | Details | Status |
|---|---|---|---|
| K1 | **Silent hang when the main menu has the League or Cookies tab selected** | `MAINMENU_1.png` is only the light "Friends" tab label (region 154,150,344,225). With another tab selected the match score is 0.00 (threshold 0.80), so no stage is recognised and the bot polls silently. Seen 12:40:45-12:44:22. The cause of the tab switch is unknown (last bot action was a Mystery Box tap). | Open. Agreed design (coded once, set aside 13:31, not deployed): new stage `MAINMENU_OTHER_TAB` using template `MAINMENU_2.png` (the "Friends" label on an *unselected* tab) in the same region, added to the PRE_GAME and POST_GAME groups; its handler taps the Friends tab at `FRIENDS_TAB_BUTTON = (247, 188)`, waits about 2 s, and lets the normal MAINMENU flow continue. Template to be cut from screenshots of the League and Cookies tabs (bot stopped, Claude clicks the tabs), checked to match both and *not* match the Friends-selected menu, then tested live. `detect_stage` skips a missing template, so the code is safe even before the image exists. |
| K2 | Unexplained stop around 12:04 | The bot's Command Prompt window was gone and no error was visible. Cause unknown. | Open. Run the bot from a window that stays open after exit, or use a restart wrapper with file logging. |
| K3 | One error ends the program | No per-iteration error handling, no ADB reconnect, no timeouts on `subprocess` calls. | Open (suggested fix: per-iteration try/except, timeouts, restart wrapper). |
| K4 | Unknown popups or screens | Bot polls forever on a screen with no template. | Diagnosis now possible via C3 (screenshots). Recovery not built. |
| K5 | Currency not checked | The bot buys items and boosts every run. It never checks coin/diamond balance. | Open. |
| K6 | Second Mystery Box tap | Log shows `MYSTERY_BOX` detected and accepted twice 5 s apart (12:40:40, 12:40:45). Not known whether harmful. | Observation only. |
| K7 | `wm size` / density may reset | If the emulator restarts, 1080x1920 may return. | Open. Better fix: MuMu Settings > Device > Resolution (Tablet 1280x720). |
| K8 | `requirements.txt` | Saved as UTF-16 and pins versions that were not installed. Works with the installed versions so far. | Low priority. |
| K9 | Console emoji | Windows console shows emoji as `?` boxes. Cosmetic. | Ignore. |
| K10 | **Infinite loop in friend-lives routine (original code)** | `handle_quick_receive_and_send_lives()` in `actions.py`: after tapping "receive all", a `while True:` loop waits for the "all lives received and sent" popup (or a send-life confirm). It has **no timeout and prints nothing while waiting**. If the mailbox closes or that popup never appears, the bot hangs forever. **Seen live 14:40:43:** last line `Receiving all lives...`, then silence; the emulator was back on the main menu (Friends tab, leaderboard scrolled to the bottom, mail badge 13) with no mailbox open. The bot process cannot recover; only Ctrl+C and a restart help. Also note the MuMu manager lists the instance as 1920x1080 / 280 DPI, its configured resolution (relevant to K7). | **Fixed by C7** (14:52, not yet seen live). |

## 7. Suggested improvements not yet done

1. Per-iteration error handling + ADB reconnect + restart wrapper with a log file.
2. Timeouts on all `adb` subprocess calls.
3. Fail fast if the screenshot is not 1280x720.
4. Save startup options to a file or CLI flags so unattended restarts need no prompts.
5. Auto-detect the ADB port from MuMuManager.
6. Stop or skip buying when out of coins/diamonds.
7. Log file plus a run counter; optional phone/Discord alert when the bot stops.
8. Lower CPU use of the 4x/second PNG screenshot.

## 8. Session log

- 10:30 Read the README and code. Found MuMu 12 on the side monitor. Device shell unavailable.
- 10:35 Set the port (16384). User ran pip and adb; port refused.
- 10:37 `MuMuManager info -v all` showed the running instance on port 16448. Config updated.
- 10:42 Bot started and connected.
- ~10:46 Emulator was 1080x1920; gave commands to set 720x1280 / density 240.
- 11:09 Discussed bot behaviour (macro, not a player) and what can stop it.
- 12:04 Bot console was gone (see K2).
- 12:10 Gave improvement suggestions.
- 12:29-12:45 Added top-row boosts (C2); found the toggle behaviour, rewrote, hit the commit lag bug, fixed, verified.
- 12:43 Bot "frozen": caused by K1. It resumed once the Friends tab was selected again.
- 12:47 User asked for this notebook and the stuck-screen screenshot (C3).
- 12:50 Notebook created. C3 (screenshot on unknown screen) built and tested offline.
- 12:52 User cancelled the C3 deploy and proposed C4 instead: restart the app when stuck and loop again. Notebook finished and saved to the PC. No code changes after C2 are on the PC.
- 12:54 User: keep C4 as an alternative; do the K1 template fix instead. K1 code written; waiting for the bot to be stopped to capture tab screenshots.
- 13:31 User: skip K1 for now, urgent experiment: auto-jump during runs. C5 built on a fresh copy of the PC files (K1 draft discarded), tested offline, deployed and verified at ~13:35.
- 13:40 Jump interval changed to 0.6-0.85 s (config only).
- 13:50 User reports auto-jump gives about +30% coins per run. Asked to stop jumping once the relay starts (relay cookie used only for its +25% coin passive). C6 built, tested offline, deployed and verified ~13:55.
- 14:39:45 **C6 seen working live:** console printed "Relay started. Auto-jump stopped for the rest of this run."; the summary showed `Run time: 161s ... relay at 151s`.
- 14:40:43 Bot hung in the friend-lives routine (K10). Found at 14:44 when the user asked "is the bot stuck". Needs a manual restart.
- 14:47 User: fix it. C7 built, tested offline (5 cases), deployed and verified ~14:52.
- 15:58 Found bot not running (no python process), game idle on main menu. Added `run_bot.ps1` (no bot code changed): starts `main.py` unattended with answers in `bot_answers.txt` (yes to all, boost 1 Double Coins, per user). Claude now has a local shell and runs it in a Claude terminal tab; checks health every 10 min. Bot back on MAINMENU at 16:02.
- 2026-10-30 ~17:45 User: real jump rate too slow despite 0.10-0.25 s. C9 built (jumping moved off the screenshot loop), tested offline, `VERSION_NOTE` updated. Needs a bot restart, opens the next version.
