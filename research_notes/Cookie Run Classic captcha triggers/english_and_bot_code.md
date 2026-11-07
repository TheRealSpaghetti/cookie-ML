# Cookie Run Classic captcha triggers: English sources and open-source bot code

Scope: the 2026 global CookieRun Classic (com.devsisters.crg, launched 2026-06-25). Research date: 2026-10-12. Bot code was read on GitHub only, never run. Overall, the evidence is **thin**. No English player report, official FAQ, patch note or "Fair Play Campaign" text describing the check turned up in search. Most concrete facts come from bot repos.

## 1. What do English-speaking players report? Do manual players see it, and how often?

### Takeaway
No English-language player reports (Reddit, X, YouTube, app-store reviews) about the card check turned up in four searches. Nothing citable confirms or measures manual-player encounters. The user's own manual sighting is currently the only manual-play data point.

### Cited Findings
- A web search for "Cookie Run Classic sliding captcha bot check" returned only generic slider-CAPTCHA vendor pages. Nothing was game-specific. — [search result example: GeeTest](https://www.geetest.com/en/article/slider-CAPTCHA-top-tool-for-security-and-usability)
- A search for Reddit "cookie run classic are you a bot cards" found no relevant thread. The r/CookieRun mirror listing surfaced, but without any match. — [r/CookieRun mirror](https://red.applefritter.com/r/CookieRun)
- Exact-phrase searches for "find the sliding" / "find the jumping" card in Cookie Run material returned nothing relevant. The only card-picking hit was a Cookie Run: Kingdom event, which is unrelated. — [CRK Game of Cards event](https://cookierunkingdom.fandom.com/wiki/Game_of_Cards_with_Royal_Margarine_Cookie)
- The official store pages and site describe a two-button (jump/slide) runner and say nothing about a verification puzzle. — [Google Play](https://play.google.com/store/apps/details?id=com.devsisters.crg&hl=en), [App Store](https://apps.apple.com/us/app/cookierun-classic/id6759596824), [Devsisters site](https://game.devsisters.com/en/cookierun-classic/)
- The challenge's prompt text exists in at least two variants. "Find the jumping card!" is quoted by a Thai bot dev (balagux v1.4.16, 30 Sep). The upstream issue #4 (31 Aug 2026) reports that "now have 2 (jumping and sliding)". — [balagux releases](https://github.com/balagux/cookierun-classic-bot/releases), [max180643 issue #4](https://github.com/max180643/cookierun-classic-bot/issues/4)

### Inferences
- The lack of English chatter could mean the check is rare for normal players. It could also mean the search tools simply index little Reddit/Discord content. No conclusion on frequency for manual players is possible from English sources.

### Gaps
- Reddit, Discord and X content was not reachable or indexed through the tools used. App-store review text was not retrievable.
- No manual-player frequency data exists in English sources.

## 2. Official information (support FAQ, ToS, July 2026 Fair Play Campaign, patch notes)

### Takeaway
No official Devsisters English text about the check, its triggers, or the July 2026 "Fair Play Campaign" was found. The only related material is a fan wiki page about Kakao/LINE-era "Clean-up Campaigns" from 2014, which is old-game info.

### Cited Findings
- The Clean-up Campaign page on cookierun.wiki describes a recurring event encouraging play without cheating tools. Past versions warned of penalties up to a permanent ban, and a later format rewarded players who reached a stage "without unauthorized methods". Its event history covers only 2014 campaigns, and the page itself says its content comes from LINE/Kakao and may not match Classic. **This is older-game info.** — [cookierun.wiki Clean-up Campaign](https://cookierun.wiki/w/Clean-up_Campaign)
- The official channels listed for Classic are X @CRClassicEN and Instagram crclassic_en. Their content was not retrieved. — [X](https://x.com/CRClassicEN), [Instagram](https://www.instagram.com/crclassic_en)

### Inferences
- The Clean-up/Fair Play naming is probably carried over from the Kakao original. That suggests Devsisters frames anti-cheat as a recurring campaign. This is speculative.

### Gaps
- Fair Play Campaign announcement text, the ToS clause on automation, support FAQ entries, and any patch note mentioning the check were all not found.
- The reported 450k coins/run server cap in July 2026 could not be confirmed from any English source. The khm0612 bot only has a local OCR sanity limit of 400,000, not a server cap (see section 3).

## 3. Open-source bot code and issues: observations on when the check appears and anti-detection measures

### Takeaway
None of the bot repos document what triggers the check or how often it appears. They treat it as a screen that can appear between runs: after a run ends, before the result screen. Each repo adopted human-like jitter and pauses on its own. The one dev who commented on effectiveness said jitter is **unverified** at reducing CAPTCHA prompts. Bots seeing the check is consistent with automation being a factor, but it proves nothing about the trigger.

### Cited Findings

**max180643/cookierun-classic-bot (upstream, Python/ADB/OpenCV, 59 commits, 37 stars, 14 forks)**
- The README lists an "Anti-Bot" stage in the game loop that "identifies and taps the odd card out". Its anti-detection measures are randomized tap coordinate jitter and delays, a 30–60 s wait between games, and an app restart every 1.5–3 h. The README presents these as ways to reduce detection risk and gives no evidence that they work. There is no ban warning. — [README](https://github.com/max180643/cookierun-classic-bot)
- config.py has the comment `# ANTI-BOT CAPTCHA`, a single template `ANTI_BOT_1.png`, a detection region at the top of the screen (309,10,968,111), and six card positions (two rows of three; card 183×241 px). ANTI_BOT sits in the stage map under "higher priority stages first". Also `SESSION_RESET_INTERVAL = (5400, 10800)  # 1.5-3 hours`. — [config.py](https://raw.githubusercontent.com/max180643/cookierun-classic-bot/main/config.py)
- detection.py's docstring for `detect_anti_bot_odd_cards` reads "Return 0-based indices of the 2 cards that differ from the majority 4". The function uses pairwise grayscale normalized cross-correlation, and the two cards with the lowest average similarity are the answer. So the expected format is 2 odd cards out of 6. — [detection.py](https://raw.githubusercontent.com/max180643/cookierun-classic-bot/main/detection.py)
- actions.py `handle_anti_bot` taps a random point inside each odd card with a 20 px margin, then sleeps `random.uniform(10, 15)` s after each card tap. Normal taps are followed by 0.8–1.4 s random sleeps. — [actions.py](https://raw.githubusercontent.com/max180643/cookierun-classic-bot/main/actions.py)
- bot.py also randomizes the lives send/receive interval (25–35 min) and the between-game delay (30–60 s). No code comment gives a reason based on detection. — [bot.py](https://raw.githubusercontent.com/max180643/cookierun-classic-bot/main/bot.py)
- Commits run Jul 7 – Aug 4, 2026. None mention anti-bot, jitter or captcha in their messages. The visible commits cover connection-lost resets, session-reset fixes and detection priorities. — [commits](https://github.com/max180643/cookierun-classic-bot/commits/main)
- **Issue #4 (31 Aug 2026), the key observation:** "anti bot png has only one but now have 2 (jumping and sliding)" and "anti bot should detect before result screen (code detect after result screen)". This places the check **between the end of a run and the result screen**, and shows that a second variant (sliding vs jumping) appeared by late August. It has no comments. — [issue #4](https://github.com/max180643/cookierun-classic-bot/issues/4)
- Issues #1 and #2 have the title "." and were closed Aug 10–11, 2026. Their content is not informative. — [issues](https://github.com/max180643/cookierun-classic-bot/issues?q=is%3Aissue)

**balagux/cookierun-classic-bot (Thai, Windows ADB/OpenCV, v1.4.21, 32 commits)**
- v1.4.15 (29 Sep) added a fail-safe: after 3 failed Anti-Bot attempts, the bot stops instead of clicking endlessly. A stress test found Daily Check-in misdetected as Anti-Bot "before round 10". That is a false positive, not a real trigger. — [releases](https://github.com/balagux/cookierun-classic-bot/releases)
- v1.4.16 (30 Sep) says the challenge shows up in real use with the prompt "Find the jumping card!". The old solver clicked the same candidate repeatedly until the fail-safe tripped. The new one reads the jumping/sliding command from the header, ranks cards by pose/slide score, and tries up to 3 different candidates. If those fail, it stops and saves a screenshot. — [releases](https://github.com/balagux/cookierun-classic-bot/releases)
- The README says timing is **not** randomized (fixed coordinates and scroll distances) and that use on a real account may conflict with the game's terms. It documents no trigger or frequency. — [README](https://github.com/balagux/cookierun-classic-bot)

**khm0612/cookierun-classic (English, LDPlayer 2560×1440, learned agent, 65 commits)**
- docs/PROJECT.md gives its reason for tap jitter: "tapping the SAME exact pixel hundreds of times per run is a trivial server-side bot tell". Defaults are a 50 px Gaussian tap scatter and ±0.15 hold-duration jitter, described as "anti-detection humanization". — [PROJECT.md](https://github.com/khm0612/cookierun-classic/blob/main/docs/PROJECT.md)
- For the card challenge, the solver uses a deliberate stand-down: a human or Claude solves it visually. Its rule for the "Find the jumping card" round is that the minority animation group is the answer pair. It warns that "wrong card taps cost more than pausing". There is also a local OCR guard, `_RESULT_COINS_MAX = 400_000`, which is a parsing sanity limit and not evidence of a server cap. — [PROJECT.md](https://github.com/khm0612/cookierun-classic/blob/main/docs/PROJECT.md)

**PacbookMro/cookierun-classic-bot-mobile (AnkuLua port)**
- v1.1.0-mobile.5 (16 Sep) added optional tap-position variation, a 40–100 ms press duration by default, and extra random pauses. — [releases](https://github.com/PacbookMro/cookierun-classic-bot-mobile/releases)
- v1.1.0-mobile.6 (16 Sep): "Tap/timing variation remains available, but its effectiveness at reducing CAPTCHA prompts is unverified." — [release mobile.6](https://github.com/PacbookMro/cookierun-classic-bot-mobile/releases/tag/v1.1.0-mobile.6)

**Commercial: CookieRunBot (cookieafk.com)**
- It claims it "detects and solves the 'find the card' bot-check on its own, so runs never stall". It has a "Solve captcha automatically" toggle, and a sample panel shows "Captchas: 5" with no time period. There is no trigger or frequency info, and the page is promotional. — [cookieafk.com](https://cookieafk.com/en)

### Inferences
- **Placement:** the check appears after a run ends, before results, which fits "between runs" (issue #4). Since bot loops treat it as a sporadic stage rather than a per-run event, it seems not to appear after every run. No repo states a run count or time interval, though.
- **Evolution:** the check had one template (odd-card) in July, gained "jumping"/"sliding" command variants by late August, and solvers were still being reworked in late September. Devsisters seems to be changing the challenge over time.
- **Failure:** the game gives limited attempts (balagux and the user both say 3). What happens after 3 failures is not documented in any repo. Bots simply stop.
- **Anti-detection rationale:** jitter is adopted on the theory that pixel-identical taps are a server-side tell (khm0612). No dev offers evidence that jitter, between-game pauses or session restarts reduce how often the check appears, and PacbookMro says explicitly that it is unverified.

### Gaps
- No repo logs or documents check frequency (per N runs, per hour, per session, after restart).
- The consequence of failing all 3 tries (lockout, lost rewards, flag or ban) is undocumented.
- Fork issues beyond the upstream repo and balagux were not reviewed. Upstream issue comments may be hidden to logged-out viewers.

## 4. Analogous mechanisms in the Korean Kakao build or sister games (OvenBreak)

### Takeaway
No English documentation of a similar in-run verification puzzle in Cookie Run for Kakao or OvenBreak was found.

### Cited Findings
- A search on Kakao "macro prevention quiz" returned only general background. Kakao is the original Korea-only version (2013). — [Wikipedia: Cookie Run (video game)](https://en.wikipedia.org/wiki/Cookie_Run_(video_game))
- The Kakao/LINE-era anti-cheat that is documented takes the form of Clean-up Campaigns with ban warnings (2014). That is older-game info. — [cookierun.wiki](https://cookierun.wiki/w/Clean-up_Campaign)

### Gaps
- Korean-language sources (for example 쿠키런 매크로 방지) are out of this English-only scope and may hold the answer.

## 5. Plausible trigger hypotheses and the evidence for each

### Takeaway
No hypothesis has direct evidence. Bots, both jittered (max180643, khm0612, PacbookMro) and non-jittered (balagux), all encounter the check, and the user reports it during manual play. That pattern fits a trigger at least partly independent of input timing, such as random sampling or play-volume and session-based checks. It cannot be established from the sources.

### Cited Findings and assessment
- **Tap timing regularity:** this is only a developer theory ("trivial server-side bot tell"). — [khm0612 PROJECT.md](https://github.com/khm0612/cookierun-classic/blob/main/docs/PROJECT.md). It is weakened by the fact that jittered bots still see the check, and by "effectiveness ... unverified". — [PacbookMro mobile.6](https://github.com/PacbookMro/cookierun-classic-bot-mobile/releases/tag/v1.1.0-mobile.6)
- **Session length / long sessions:** the upstream bot restarts the app every 1.5–3 h to reduce detection risk, but gives no evidence. — [max180643 README](https://github.com/max180643/cookierun-classic-bot)
- **Run count / play volume:** balagux's stress test mentions "before round 10", but that was a false-positive misdetection, not a real trigger. — [balagux releases](https://github.com/balagux/cookierun-classic-bot/releases). There is no other evidence.
- **Abnormal coins/score per run (450k cap):** no English source found for the cap. The only related number is khm0612's 400k OCR guard, which is unrelated. — [PROJECT.md](https://github.com/khm0612/cookierun-classic/blob/main/docs/PROJECT.md)
- **Emulator detection:** no evidence. Bots run on LDPlayer and MuMu (max180643 commit "mumu player default port"), and the AnkuLua port runs on real phones (S20 FE). — [max180643 commits](https://github.com/max180643/cookierun-classic-bot/commits/main), [PacbookMro releases](https://github.com/PacbookMro/cookierun-classic-bot-mobile/releases)
- **Random sampling:** no direct evidence. It is consistent with manual sightings and with every bot type encountering the check.

### Inferences
- The most defensible statement is this: the check appears between the end of a run and the result screen, not every run. It comes in jump/slide variants with 2 correct cards out of 6 and limited tries. Its trigger is not publicly documented in English. Randomized tap timing has not been shown to reduce it.

### Gaps
- Each trigger hypothesis lacks controlled observations. A useful next step would be for the user to log run count, session time, coins per run and device each time the check appears.
