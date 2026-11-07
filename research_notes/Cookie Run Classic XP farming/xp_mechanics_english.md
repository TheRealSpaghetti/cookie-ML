# Cookie Run Classic (2026, com.devsisters.crg): XP and Leveling Mechanics, and English-Community Leveling Strategies

Research date: 2026-10-12. About 19 search/fetch calls. **Overall verdict on sources:** English-language material about the 2026 game's XP system is very thin. No Reddit threads, YouTube guides, gaming-news articles or official patch notes describing Classic's XP system turned up in search. Most "CookieRun Classic wiki" sites in the results (cookierun-classic-wiki.wiki, cookierunclassic.online, cookie-run-classic.wiki, cookierunclassicwiki.site) are unofficial, cite nothing and contradict each other. Several show signs of being AI-generated SEO content; for example, one recommends "Fire Spirit Cookie / Flame Mirror" combos and gives a level cap of 70. Treat everything from them as low-confidence. The best numeric source found is a level-curve table on cookierundb.com, which has no datamine attribution.

Background context, which is well sourced:
- Cookie Run Classic released worldwide on June 25, 2026. It is a "globalized English version of Cookie Run for Kakao" (the 2013 Korean game, revived with updates in April 2024). It uses DevPlay login instead of KakaoTalk, and it is not available in South Korea or India. — [cookierun.wiki: CookieRun: Classic](https://cookierun.wiki/w/CookieRun:_Classic); release date also in [Wikipedia: Cookie Run (video game)](https://en.wikipedia.org/wiki/Cookie_Run_(video_game))
- Devsisters announced Classic at DevNow 2026 (March 28, 2026), with pre-registration starting in June. — [Wikipedia: Cookie Run](https://en.wikipedia.org/wiki/Cookie_Run), citing the Devsisters DevNow 2026 YouTube stream
- Current versions per the wiki: 26.08.01 (iOS) and 26.08.02 (Android); page last edited September 3, 2026. — [cookierun.wiki](https://cookierun.wiki/w/CookieRun:_Classic)
- Note: "max level 8" in Classic sources refers to **Cookie/Pet upgrade level**, not account level. Fully upgrading a Cookie or Pet unlocks a Treasure. — [cookierun.wiki](https://cookierun.wiki/w/CookieRun:_Classic)

## Q1. How is XP earned per run, and what is the XP curve to level 110?

### Takeaway
The only level-curve data found (cookierundb.com, unsourced) puts the total XP from level 1 to level 110 at about **125 million XP**. The last 10 levels alone need about 36M, with levels 105 to 110 costing 4.2M to 5.3M XP each. I found no verified Classic-specific per-run XP formula. The only formula found (10 base XP per second survived) comes from documentation of the older LINE/Kakao game.

### Cited Findings
- cookierundb.com has a "Level curve" page charting XP-to-next-level and rewards for all 110 player levels. This implies the account level cap is 110. — [cookierundb.com/economy/levels](https://cookierundb.com/economy/levels)
- Selected XP-to-next-level values from that table: Lv1 1,500; Lv5 9,000; Lv10 23,000; Lv50 350,000; Lv70 700,000; Lv80 900,000; Lv90 1,200,000; Lv100 1,285,900; Lv105 4,234,500; Lv106 4,876,500; Lv107 5,123,400; Lv108 5,223,450; Lv109 5,345,600 (109 to 110). Level 110 is max. — [cookierundb.com/economy/levels](https://cookierundb.com/economy/levels)
- Cumulative XP from the same table (summed by the fetch tool): to Lv11 98,000; through Lv20 420,000; Lv30 930,000; Lv40 1,735,600; Lv50 4,723,600; Lv60 10,570,000; Lv70 20,220,000; Lv80 39,620,000; Lv90 61,920,000; Lv100 89,105,900; **Lv1 to Lv110 total 125,040,750 XP**. — [cookierundb.com/economy/levels](https://cookierundb.com/economy/levels)
- Per-level rewards in that table: coins (10k to 50k), crystals (1 to 30 per level at high levels) and a "bonus score" that rises from 0 to 550 at Lv110. — [cookierundb.com/economy/levels](https://cookierundb.com/economy/levels)
- One fan guide says account level raises a "Level Bonus" score multiplier applied at the end of each run, so account level directly feeds League scores. — [cookierun-classic-wiki.wiki progression guide](https://cookierun-classic-wiki.wiki/guide/cookierun-classic-account-progression-guide) (unverified fan site)
- One unofficial fan guide (updated June 26, 2026) claims XP "scales with distance and combo score" but gives no numbers. The same page claims the level cap "was raised to 70", which contradicts the 110-level table. — [cookierunclassic.online farming guide](https://cookierunclassic.online/farming/cookie-run-classic-farming-guide)
- **Older game (LINE/Kakao-era documentation, may not apply to Classic):** the Fandom "XP Farming" page says each second of a run gives 10 base XP, so run XP divided by 10 is roughly seconds survived, and treasure/combi XP bonuses have changed over time. This is from a search-result summary only; the page returned HTTP 402 on fetch. — [cookierun.fandom.com/wiki/XP_Farming](https://cookierun.fandom.com/wiki/XP_Farming)
- **Older game:** the LINE Cookie Run user level cap was raised to 80 in v3.0.6 (May 15, 2015) and to 100 in v6.0.0 (October 14, 2016). — [cookierun.wiki: LINE Cookie Run](https://cookierun.wiki/w/LINE_Cookie_Run)
- A fan site says the third Treasure slot unlocks at account level 25. — [cookierunclassicwiki.site upgrade guide](https://cookierunclassicwiki.site/guide/upgrade/)

### Inferences
- If the cookierundb curve is accurate, about 125M XP is a very large total. With the old-game formula of 10 XP per second, a 3-minute run gives about 1,800 base XP, or about 3,600 with Double XP. Reaching 110 would then take tens of thousands of runs, which is implausible for thousands of players in about 4 months without automation **unless** Classic's per-run XP is far higher than the old 10 XP/s base. This is a sensitivity estimate, not a sourced figure.
- Break-even framing for the report writer, using 125M XP over 109 days (June 25 to about Oct 12):
  - The average needed is about 1.15M XP per day.
  - At 5k XP per run, that is about 230 runs/day; at 20k XP per run, about 57/day; at 50k XP per run, about 23/day.
  - The decisive missing number is the **actual XP per run at endgame** in Classic.
- The table has oddities: Lv7 needs less XP than Lv6, and XP jumps 3.3x between Lv100 and Lv105. This could be real data or transcription error, so it should be checked against in-game values.

### Gaps
- I found no verified figure for XP earned per run in Classic, whether official, datamined, or from a screenshot/video.
- I could not confirm whether Classic XP depends on time survived, score, distance, or Cookie/Pet level.
- The cookierundb.com table has no stated data source.
- NamuWiki (the Korean wiki that would document the Kakao level curve and XP formula) returned HTTP 403.

## Q2. What multiplies XP (items, Cookies, Pets, Treasures, Combi, events, passes, packages)?

### Takeaway
A pre-run **Double XP** boost exists in the lineage. In LINE Cookie Run it cost 800 coins and doubled run XP, and one Classic fan wiki lists "Double EXP". Fan sites mention "Burning Time" XP events and XP-boosting Cookies and Treasures without naming any. Old-game combi XP bonuses of about 20 to 30% are documented, but some were removed and none are confirmed for Classic.

### Cited Findings
- **Older game (LINE):** "Double XP" costs 800 coins and "Doubles the XP during the run". An unofficial v3.0.6 note says new and returning players got free Double XP for one week. — [cookierun.wiki: LINE Cookie Run](https://cookierun.wiki/w/LINE_Cookie_Run)
- **Older game (LINE):** C-grade Cookies "give the player extra XP" (no amount given). — [cookierun.wiki: LINE Cookie Run](https://cookierun.wiki/w/LINE_Cookie_Run)
- A Classic fan wiki (labelled July 2026) lists a "Double EXP" power-up that "Doubles Cookie and Pet experience gained". That wording suggests Cookie/Pet XP rather than account XP. No cost is given, and the claim is unsourced. — [cookie-run-classic.wiki power-ups](https://cookie-run-classic.wiki/items/power-ups/)
- A fan guide claims "Burning Time" events double XP or Coin gain for a few hours, and that Special Episodes/Event Maps "often yield 2x or 3x normal XP". It also says unnamed XP-boost Cookies and Treasures exist. None of this is sourced. — [cookierun-classic-wiki.wiki progression guide](https://cookierun-classic-wiki.wiki/guide/cookierun-classic-account-progression-guide)
- Another fan guide claims XP Boost items come from events and the shop, that an "XP Potion" adds XP per jelly, and that "Magic Candy" unlocks XP multipliers. These names look borrowed from Cookie Run: Kingdom, so this is likely unreliable. — [cookierunclassic.online farming guide](https://cookierunclassic.online/farming/cookie-run-classic-farming-guide). A different fan site says XP Potions apply to individual Cookies (cap Lv8), not account level — [cookierunclassicwiki.site](https://cookierunclassicwiki.site/guide/upgrade/)
- **Older game (Fandom, archived/"no longer relevant" list):**
  - The Bright Cookie + Wishing Star combi gave 30% extra XP, which "has been removed".
  - Peach Cookie + Panda Dumpling gave a 20% XP combi.
  - Alchemist Cookie + Coin Scale gave an alternate 20% XP.
  - Source: search-result summaries of [Fandom List of Combination Bonuses](https://cookierun.fandom.com/wiki/List_of_Combination_Bonuses), [Fandom XP Farming](https://cookierun.fandom.com/wiki/XP_Farming) and [Fandom Cookie Run Records](https://cookierun.fandom.com/wiki/Cookie_Run_Records). The pages themselves were not fetched because of HTTP 402.
- The official store description says: "Get a head start with special events and buffs just for new players!" No specifics are given. — [BlueStacks listing for com.devsisters.crg](https://www.bluestacks.com/campaign/com.devsisters.crg/ms/)

### Inferences
- Stacking Double XP (2x) with combi/treasure bonuses (old game about 20 to 42%) and timed events (2x) could plausibly give about 4 to 6x base XP during events. That narrows the gap in Q1 but does not close it unless base XP per run is substantial.
- Paid packages, a season pass, and friend/invite XP bonuses: nothing found (see Gaps).

### Gaps
- There is no official list of Classic XP multipliers or their values.
- I found nothing on season-pass XP, paid XP packages, or friend/invite XP bonuses for Classic.
- I could not confirm whether Classic's Double XP affects account XP or only Cookie/Pet XP.

## Q3. Which combos, maps, or modes are recommended for XP farming, with XP-per-run and runs-per-level figures?

### Takeaway
I found no credible, Classic-specific XP-farming recommendation with numbers. The combos and modes that do appear come from unverified fan sites or describe the old game.

### Cited Findings
- An unofficial fan site attributes these combos to "community reports":
  - Fire Spirit Cookie + Fire Spirit Pet + Flame Mirror
  - Millennial Tree Cookie + Leafy Sapling + Elder Tree Branch
  - Dark Enchantress Cookie + Dark Butler + Magic Candy

  It also recommends "Breakout" and "Trophy Race" on special maps for jelly density, gives no XP numbers, and claims level 70 takes "2–3 weeks of daily play (1–2 hours per day)". It says auto-farming yields less XP per run. — [cookierunclassic.online](https://cookierunclassic.online/farming/cookie-run-classic-farming-guide). *Several of these names (Millennial Tree, Flame Mirror, Magic Candy) are from other Cookie Run titles, so this list is likely fabricated.*
- **Older game:** Fandom's XP Farming page describes Fire Spirit Cookie-based XP methods tied to old-game mechanics. — [cookierun.fandom.com/wiki/XP_Farming](https://cookierun.fandom.com/wiki/XP_Farming) (via search summary)
- The current top Cookie in Classic tier lists is Lotus Root Phantom Cookie, added in the June 25, 2026 update together with the Lotus Sitter pet. The rankings are for score, not XP. — [cookierunclassicwiki.site tier list](https://cookierunclassicwiki.site/tier-list/); [@CRC_news on X, June 25 update](https://x.com/CRC_news/status/2070075773545844955)
- A Kakao-version newbie guide (dated April 29, 2026) recommends episode-by-episode setups for **League/Medal** farming, not XP. — [cookierunhub.com newbie guide step 3](https://www.cookierunhub.com/en/encyclopedia/newbie-guide/5)

### Inferences
- Without XP-per-run figures, runs-per-level cannot be calculated from any source. Even the Lv109-to-110 step (5.35M XP) can only be expressed as a function of an unknown per-run yield.

### Gaps
- I found no YouTube or Reddit English guide titled "fastest XP" or "best combi for XP" for Classic.
- I found no in-game screenshots of XP-per-run results.

## Q4. How long do players say it took to reach 110? Are there leaderboards or stat sites showing the level distribution?

### Takeaway
Nothing found. Searches for "level 110" or "max level" across Reddit, YouTube and news turned up no English player reports of reaching Lv110 and no public leaderboard or stat site showing account-level distribution.

### Cited Findings
- Searches for "CookieRun Classic level 110" plus reddit/YouTube found no r/CookieRunClassic posts or videos about Lv110. Results were dominated by Kingdom/OvenBreak pages. — e.g. [cookierunclassicwiki.site tier list](https://cookierunclassicwiki.site/tier-list/), which also warns that "pre-launch CRK posts pollute search results"
- The only "time to level" claim found is about 2 to 3 weeks to level 70 at 1 to 2 hours per day. It comes from an unreliable fan site that also says the cap is 70. — [cookierunclassic.online](https://cookierunclassic.online/farming/cookie-run-classic-farming-guide)
- A third-party "earning guide" describes running multiple LDPlayer emulator instances with OSLink remote control to farm CookieRun Classic AFK. This is direct evidence that multi-instance automation is being promoted publicly for this game. — [oslink.io: CookieRun Classic best earning guide](https://www.oslink.io/blog/guide/cookierun-classic-best-earning-guide.html)

### Inferences
- The lack of English community discussion about grinding to 110 is weak evidence, since search-index coverage of Reddit/Discord is poor. However, it means no public organic explanation, such as a known fast-XP method, was found.

### Gaps
- I found no player-reported time-to-110.
- I found no level-distribution leaderboard. Classic's in-game League and friend rankings may show levels, but no external aggregator was found.

## Q5. Was there XP carry-over from older accounts, pre-registration rewards, or catch-up mechanics at launch?

### Takeaway
I found no evidence of account or XP carry-over: Classic uses a new DevPlay login and is region-locked away from Korea, where the Kakao game lives. Launch rewards mentioned are crystals and treasure tickets. New-player "buffs" are advertised but not specified.

### Cited Findings
- Classic uses DevPlay login instead of KakaoTalk and is unavailable in South Korea and India. Nothing on the page mentions account transfer. — [cookierun.wiki: CookieRun: Classic](https://cookierun.wiki/w/CookieRun:_Classic)
- LINE Cookie Run was shut down on June 5, 2018, so there was no live LINE account base to carry over. — [Wikipedia: Cookie Run (video game)](https://en.wikipedia.org/wiki/Cookie_Run_(video_game))
- A fan site mentions launch rewards of 300 Crystals and Supreme Treasure Tickets, not XP or levels. — [cookierunclassicwiki.site upgrade guide](https://cookierunclassicwiki.site/guide/upgrade/)
- The store description says: "Get a head start with special events and buffs just for new players!" — [BlueStacks listing](https://www.bluestacks.com/campaign/com.devsisters.crg/ms/)
- **Older game precedent:** LINE gave free Double XP for one week to new and returning players (unofficial note). — [cookierun.wiki: LINE Cookie Run](https://cookierun.wiki/w/LINE_Cookie_Run)

### Inferences
- Every Classic account started at level 1 on or after June 25, 2026, so all of the roughly 125M XP (if the table is right) had to be earned within about 109 days, possibly with new-player XP buffs.

### Gaps
- I did not find the exact contents of the new-player buffs, or whether they include XP multipliers or how long they last.
- I did not find the pre-registration milestone reward list.

## Q6. Were there patches that nerfed or buffed XP, or known XP exploits/bugs?

### Takeaway
I found no Classic patch note mentioning XP changes, and no reported XP exploit.

### Cited Findings
- The June 25, 2026 update thread from @CRC_news (a fan news account covering Classic/Kakao) lists Lotus Root Phantom Cookie, Lotus Sitter, a Devsquirrels friend-ranking challenge, and a Melon Bingsoo crafting event. No XP changes are visible. — [x.com/CRC_news/status/2070075773545844955](https://x.com/CRC_news/status/2070075773545844955)
- A January 15 (Kakao/Classic) update made Cookie abilities behave the same across phone models and added Episode 6. No XP change is described. — [x.com/CRC_news/status/2011829275058462951](https://x.com/CRC_news/status/2011829275058462951)
- **Older game:** the 30% XP combi for Bright Cookie + Wishing Star "has been removed", which is a historical XP nerf. — [Fandom List of Combination Bonuses](https://cookierun.fandom.com/wiki/List_of_Combination_Bonuses) (via search summary)

### Inferences
- No public patch or exploit explains rapid mass leveling, at least among English-indexed sources.

### Gaps
- I could not read the full official patch notes. The X threads were only seen as search snippets, and the official Devsisters notice board was not found in search.
- NamuWiki's Kakao patch history was blocked (HTTP 403).
- Discord announcements were not reachable.
