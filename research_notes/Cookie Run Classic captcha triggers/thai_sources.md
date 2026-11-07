# Cookie Run Classic captcha triggers: Thai-language sources

Scope: Cookie Run Classic (com.devsisters.crg, global launch 2026-06-25). Researched 2026-10-12. Overall verdict: **Thai sources show the check exists and that bots solve it, but none say what triggers it.** I found no Thai player reports (Pantip, Facebook, TikTok, YouTube) of the check that search engines index. No vendor gives a frequency or a trigger, and I found no official Thai Devsisters statement about it.

## 1. What Thai players and vendors call the check

### Takeaway
Thai vendors use English loanwords: "CAPTCHA", "Anti-Bot", and "Card Game (Anti Bot)". Searches for "แคปช่า" (captcha), "ทดสอบบอท" (bot test), "หาการ์ด" (find the card), "กันบอท" (anti-bot) and "เด้งให้เลือกการ์ด" (pops up asking you to pick a card), each paired with the game name, found nothing about this check.

### Cited Findings
- cookierunbot.com (Thai) calls it a "Card Game". Its settings toggle reads "เล่น Card Game(Anti Bot)" ("play Card Game (Anti Bot)"), and the page says the bot will "เจอหน้า Card Game แก้ให้เองแล้ววิ่งต่อ" ("hits the Card Game screen, solves it itself, then keeps running"). Auto-solving is a Pro-plan feature. — [cookierunbot.com, TH](https://www.cookierunbot.com/)
- jlbotcookierun.me (Thai) lists "ระบบแก้ CAPTCHA อัตโนมัติ" ("automatic CAPTCHA solving system") and "มีตัวช่วย CAPTCHA" ("has a CAPTCHA helper") as Premium features. — [jlbotcookierun.me, TH](https://jlbotcookierun.me/); [jlbotcookierun.me/bot-cookie-run, TH](https://jlbotcookierun.me/bot-cookie-run)
- cookieafk.com ("CookieRunBot", English page with Thai baht pricing) says the bot "Detects and solves the 'find the card' bot-check on its own, so runs never stall". It also has a "Solve captcha automatically" toggle and a captcha counter. — [cookieafk.com/en, EN](https://cookieafk.com/en)
- The balagux GitHub bot (Thai/English release notes) calls it "Anti-Bot". Its notes quote the in-game English prompt "Find the jumping card!" and say the header text says either "jumping" or "sliding". — [balagux releases, TH/EN](https://github.com/balagux/cookierun-classic-bot/releases)
- The max180643 GitHub bot (English) calls it the "Anti-bot card challenge" and describes it as picking "the odd card out from a set of six". — [max180643 README, EN](https://github.com/max180643/cookierun-classic-bot)
- cookiegamebot.com was unreachable (connection refused), so it was not checked.

### Inferences
- The in-game text seems to be English even in Thai builds ("Find the jumping/sliding card!"). That may be why Thai players have no settled Thai name for it.
- Two descriptions of the puzzle exist: "odd card out" (max180643) and "jumping vs sliding" (balagux v1.4.16). The challenge may have changed, or come in several variants.

### Gaps
- I found no Thai forum, Facebook or TikTok post that names the check. Facebook groups and TikTok are mostly not indexed, and the search engine is US-based.

## 2. Reported triggers

### Takeaway
**No Thai source names a trigger.** The only clues are indirect. Bot authors add random waits, tap jitter and periodic app restarts "to reduce detection risk", which shows what they think matters. A Korean source (not Thai) says the check kept appearing when the bot tapped the same pixel every time.

### Cited Findings
- max180643 README (EN): "Auto-waits 30–60 seconds between games to reduce detection risk"; it restarts the app "every 1.5–3 hours to avoid long-session detection"; it uses "Human-like tap behavior with randomized coordinate jitter and delays". It does not say what triggers the card check. — [max180643, EN](https://github.com/max180643/cookierun-classic-bot)
- cookierunbot.com (TH) says the bot "สุ่มพฤติกรรมการแตะหน้าจอ" ("randomizes tap behaviour") and pauses between stages. It does not say this prevents the Card Game. — [cookierunbot.com, TH](https://www.cookierunbot.com/); [is-cookierunbot-safe, TH](https://cookierunbot.com/articles/is-cookierunbot-safe)
- jlbotcookierun.me (TH): "จำลองจังหวะการกระทำของผู้เล่น" ("simulates the timing of player actions"). It is not linked to CAPTCHA. — [jlbotcookierun.me, TH](https://jlbotcookierun.me/)
- cookieafk.com (EN): "human-like random timing", described as jump timing, not captcha avoidance. — [cookieafk.com/en, EN](https://cookieafk.com/en)
- balagux release notes name no in-game trigger. They only mention bot-side false positives (Daily Check-in and News/Announcement screens misread as Anti-Bot), plus one live appearance of "Find the jumping card!". — [balagux releases, TH/EN](https://github.com/balagux/cookierun-classic-bot/releases)
- Korean source, not Thai (found by an earlier researcher in this project): a bot author said the anti-bot mini-game kept appearing and blamed 「같은 위치에 반복된 클릭이 문제였던거임」 ("repeated clicks at the same position were the problem"). Their fix was to randomize click positions. — see `research_notes/Cookie Run Classic XP farming/korean_sources.md`. That file holds the original URL; I did not check it again.

### Inferences
- The user saw the check while playing by hand. Bot vendors treat it as something that will happen anyway ("so runs never stall"), not something they can prevent. Together these suggest the check fires at least partly at random or on a schedule, not only on detected automation. **This is an inference; no source states it.**
- Vendors focus on tap jitter, timing randomness and session resets. That suggests they believe the check, or detection generally, responds to repeated input positions, exact timing and long continuous sessions. This is vendor belief, not confirmed behaviour.

### Gaps
- Nothing found on consecutive-run counts, coins per run, emulator detection, time of day, or account age/level as triggers.

## 3. Frequency (manual players vs bot users)

### Takeaway
**No source gives a frequency.** The only number is one vendor screenshot showing the Card Game 3 times in 80 runs, all 3 solved. That is marketing material, not a measurement.

### Cited Findings
- cookierunbot.com sample panel: "เจอหน้า Card Game" ("Card Game screen seen") = 3 and "แก้สำเร็จ" ("solved successfully") = 3, over 80 runs. This is one promotional screenshot. — [cookierunbot.com, TH](https://www.cookierunbot.com/)
- cookieafk.com sample panel shows a captcha counter of 5. The page gives no run count or time window to go with it. — [cookieafk.com/en, EN](https://cookieafk.com/en)
- balagux v1.4.15: a stress test hit a "Daily Check-in → Anti-Bot false-positive ก่อนรอบที่ 10" ("before round 10"). This was the bot misreading a screen, not a real challenge. v1.4.16 says the solver was not tested live because "ไม่มีการบังคับให้เกิด Anti-Bot challenge ใหม่แบบ live" ("no new live Anti-Bot challenge could be forced"), meaning the developer could not make the check appear on demand. — [balagux releases, TH/EN](https://github.com/balagux/cookierun-classic-bot/releases)

### Inferences
- If the panel is representative, bot users see the check roughly once every 25–30 runs. Treat this as very weak evidence.
- The balagux developer could not force the check to appear. That fits an infrequent or probabilistic trigger, not a fixed every-N-runs rule.

### Gaps
- No manual-player frequency reports in Thai. Vendor FAQs and changelogs (cookierunbot, jlbot, cookieafk) give no frequency. cookiegamebot.com could not be reached.

## 4. Consequences of failing or ignoring it, and ban links

### Takeaway
The in-game consequence of failing all 3 tries is **not documented** in any Thai source. Bots simply stop after 3 failures to stay safe. The mid-July 2026 ban wave was blamed on a **450,000 raw coins per run** anti-cheat threshold triggered by buffed Banana Cookie. Neither source ties it to the card check.

### Cited Findings
- balagux v1.4.15: "เพิ่ม Anti-Bot fail-safe: หากลองครบ 3 ครั้งแล้วยังไม่ผ่าน บอทหยุดพร้อม error แทนการคลิกไม่จำกัด" ("adds Anti-Bot fail-safe: after 3 failed attempts the bot stops with an error instead of clicking without limit"). v1.4.16: "หากยังไม่ผ่านหลัง 3 candidate จะหยุดอย่างปลอดภัย" ("if still not passed after 3 candidates it stops safely"). Neither says what the game does after 3 failures. — [balagux releases, TH/EN](https://github.com/balagux/cookierun-classic-bot/releases)
- 24buym.com blog (TH, dated 2026-07-17), from a top-up seller and therefore secondhand. The old Anti-Cheat system flags accounts whose raw coins in one run exceed 450,000: "ถ้าไอดีไหนเก็บเหรียญดิบในหนึ่งรอบการวิ่งได้เกินเพดานนี้" ("if any ID collects raw coins in one run above this ceiling"). The blog says wrongly banned accounts were "ปลดแบน" ("unbanned"). It cites only "ข้อมูลที่ทีมงานชี้แจงในช่วงเกิดเหตุ" ("information the team clarified during the incident") and gives no official link. It never mentions captcha or card checks. — [24buym.com, TH](https://www.24buym.com/blog/cookie-run-classic)
- indexgame.in.th (TH), as summarized in search results; the page itself returned 403. It says the auto-ban treated more than 450,000 raw coins in one run as program assistance and suspended the account "ทันที" ("immediately") with no human review, and blames the Banana Cookie buff. — [indexgame.in.th, TH](https://www.indexgame.in.th/en/article/cookie-run-classic-banana-cookie-auto-ban-fix)
- Vendor disclaimers (TH): jlbot says "เราจะไม่รับผิดชอบต่อความเสี่ยงใด ๆ ที่เกิดขึ้นกับบัญชีของท่าน รวมถึงการถูกระงับหรือแบน" ("we are not responsible for any risk to your account, including suspension or ban"). cookierunbot says "ไม่สามารถการันตีว่าจะไม่มีความเสี่ยงเลยร้อยเปอร์เซ็นต์" ("cannot guarantee 100% zero risk"). — [jlbotcookierun.me, TH](https://jlbotcookierun.me/); [cookierunbot safety article, TH](https://cookierunbot.com/articles/is-cookierunbot-safe)

### Inferences
- The 450k ban wave looks like a **separate** server-side score/coin check, unrelated to the card puzzle. No source connects the two.
- Bot authors stopping after 3 failures suggests they think repeated failures could be risky. That is caution, not evidence of a penalty.

### Gaps
- No Thai reports of what happens after failing: a lockout, lost run rewards, or a ban.
- No ban reports tied specifically to the card check.

## 5. Official Devsisters statements (TH/global)

### Takeaway
I found no official Thai or global Devsisters statement about the card check. A search for the "Fair Play Campaign" returned nothing indexed. (An earlier researcher in this project noted a July 2026 Fair Play campaign warning of "permanent account suspension", but could not get its full text.)

### Cited Findings
- English search for "CookieRun Classic Fair Play Campaign Devsisters" returned only store pages and Wikipedia, with no campaign page. — [Google Play listing](https://play.google.com/store/apps/details?id=com.devsisters.crg&hl=en)
- Earlier project note: `research_notes/Cookie Run Classic XP farming/automation_and_exploits.md` line 120 mentions the Fair Play campaign. That file holds the source.
- Older-game material, flagged as **not Classic 2026**: the cookierun.wiki "Clean-up Campaign" page draws on LINE Cookie Run, and a Fandom post describes an occasional "match similar cards" anti-bot puzzle in the Korean (Kakao) version. These show the mechanic has a history in earlier Cookie Run versions. — [cookierun.wiki Clean-up Campaign](https://cookierun.wiki/w/Clean-up_Campaign); [Fandom post, EN; page returned 402, content seen in search summary only](https://cookierun.fandom.com/f/p/2502410501095892997)

### Inferences
- The card check probably descends from the old Kakao/LINE Cookie Run anti-macro puzzle, which also appeared "occasionally" to ordinary players. If so, that would fit the user seeing it while playing by hand. This rests on a single unverified Fandom summary.

### Gaps
- No Thai Devsisters social post, FAQ or in-game notice about the check could be retrieved. The in-game news, the official Facebook TH page and Discord are not indexed.
