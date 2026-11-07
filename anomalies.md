# Anomaly log (2026-10-10)

Things that happened which the bot or monitoring didn't already account for.

| Time | What | Impact | Status |
|---|---|---|---|
| ~15:58 | Bot not running at all when monitoring started (no python process); game idle on main menu | Lost play time, unknown how long | Restarted via run_bot.ps1 |
| 16:50-16:54 | Coins fell 926,662 -> 23,648 and diamonds changed while the bot was stopped | ~903k coins gone | Unexplained; asked user |
| 16:50 | After a manual game restart, 3 popups (New Treasures, Fire Feather Hunt, News) | Bot might not recognise start screen | Closed by hand; bot's own reset at 18:29 closed popups itself |
| 17:35 | In-run "5 crystals for 1 Pit Lift" prompt at end of run | Crystal spend risk | Bot's jump taps land far from the button; never pressed |
| 17:52 | Tracker could not read 7-digit coin balance (OCR) | One run not logged | Fixed (multi-scale OCR) 17:56 |
| 18:27 | First automatic session reset (app restart after 1.56 h) | ~2 min downtime | Worked: app restarted, popups closed, main menu found 18:29 |
| various | Net per run varies 54,815 to 110,700 (avg ~76k) | None | Normal variance (mystery box / boosts) |
| 18:29 | Tracker logged the bot's app restart as a fake run with net 0 (dragged avg to 72k) | Wrong average | Row removed; tracker now ignores zero-change visits (18:36) |
| 18:32-18:42 | Extra lives fell 13 -> 10 over ~2 runs (faster than ~0.6/run before) | Lives alert sooner | Watching |
| 18:46 | Tracker OCR can't read single-digit lives (+9 showed as blank) | Lives file blank below 10 | Claude reads the saved lives crop image directly each check |
| 18:46 | Run net only +41,685 (below usual 55k-110k) | Lower avg | Watching |
| 18:35-18:55 | Since the 18:27 app restart, runs are shorter (133-155 s vs 162-171 s; relay at ~115-145 s vs ~152-158 s) and net per run fell to 31k-45k (was ~75k) | ~40% fewer coins/run | Cause unknown. Boosts still show active; Double XP stock ran out (now auto-buys at 800). Watching |
| 19:01 | Likely cause of shorter runs: only 1 of 3 Treasure slots is equipped in-run (at 15:59 all 3 were filled) | Lost treasure bonuses | Reported to user |
| 19:40 | Re-equipped Red Hot Chili Drink (slot 1) and Jingle-jangle Coin Wallet (slot 2) at user's request; restarted bot. Old run log moved to coin_runs_until_1909.csv so the new average reflects full treasures | - | Done |
| 19:46 | User says treasures should not unequip by themselves. Bot code has no treasure-unequip path (only a TOO_MANY_TREASURES popup, never seen today). Test: check Treasure screen right after the next bot session reset (~21:15-22:45) | - | Observing |
| 19:47-22:40 | Bot, tracker and watcher sessions all stopped; emulator restarted ~22:38 (density override had reset to 280; set back to 240). coin_runs.csv missing, so tracker average restarts from zero | ~3 h lost | Restarted 22:41; all 3 treasures confirmed equipped |
| 2026-10-11 ~17:50-18:32+ | Bot sits on the 'Find the sliding card' check; tries stay 3/3, bot process alive and polling | No runs | Waiting on user to clear it by hand |
| 2026-10-11 20:56 | Tracker misread balance (5,390,613; real ~5.17M), logging run 16 as +262k and run 17 as -183k | Wrong avg | Both rows removed; tracker restarted (real 2-run total was +79k) |
| 2026-10-12 15:23-15:33 | coin_runs.csv was emptied by something outside the tracker (only run 13 left, no header) | Run log lost | Rebuilt runs 1-13 from the tracker's console output |
| 2026-10-12 15:53 | Tracker read balance as 941,131 (dropped a digit; real 9,520,906 at ~16:00) | None | Misread |
| 2026-10-12 ~16:00 | Crystals at 5; were 15 on 10-11 19:35. Cause unknown (not seen being spent) | Possible crystal spend | Flagged to user |
| 2026-10-12 ~17:03-17:08 | Bot process exited after its 17:02:58 record (cause unknown, no error seen); game idle on main menu | ~5 min | Restarted with run_bot.ps1 in a terminal tab at 17:08 |
| 2026-10-12 17:09-17:13 | During one normal bot run, coins fell 11,208,012 -> 10,121,896 (~1.23M spent) and extra lives fell 344 -> 243 (-101). Bot log shows only a normal run; only one bot process | ~1.23M coins, 101 lives | Unexplained; asked user (other device/manual purchase?) |
| 2026-10-12 17:23-17:28 | Second losing run: -109,790 (normal is ~+145k). Crystals 17 (17:08) -> 8 (17:29); keys 45 (17:00) -> 38 (17:29) -> 35 (17:33). Recorded run at 17:29-17:34 was normal; the bot never taps near the end-of-run '5 crystals for 1 Pit Lift' button. Another Claude Code process is running on this PC | Coins, crystals | Asked user |
| 2026-10-12 17:39 | Caught a losing run on video: on the pre-run boost screen the balance fell 10,627,687 -> 10,090,087 (-537,600) on the Fast Start buy (listed 1,600; stock +1 only), -> 9,941,087 (-149,000) on the Cookie Relay buy (listed 3,000), -> 9,736,887 (-204,200) on Random Boost Multi-Buy. Run net -724,593. Frames in debug_screens/coin_drop_1739 | ~890k | Reported to user; cause unclear (bad charge, multi-buy, or server-side correction) |
| 2026-10-12 19:25 | Card check cleared (~18:21-19:25). A second bot (python main.py, from a separate PowerShell window) started 19:25:13 while Claude's bot was still running; both drove the game for ~3 min. Ledger logged -1,068,985 for the 18:15-19:25 span | Double taps risk; ~1.07M lost over the stuck period | Stopped Claude's copy at 19:28; the user's copy keeps running |
| 2026-10-12 ~20:48-20:54 | On the pre-run boost screen: crystals 0 (were 8-9 at 17:39), keys 3 (were 33-35), coins 10,733,786 (11,556,073 at 20:43, about -822k before the run). Random Boost Multi-Buy screen showing many rerolls before Double Coins | Crystals gone; ~820k coins | Alerted user |
