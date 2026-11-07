# Cookie Run Classic captcha / anti-macro check: Korean-language sources

Scope note: nearly all Korean evidence is about the **Korean Kakao build** (쿠키런 for Kakao, 쿠키런 클래식 in Korea, com.devsisters.CookieRunForKakao), which DC Inside users call "카쿠" (카카오 쿠키런). I found **no Korean source about the global 2026 build (com.devsisters.crg)** and its check. Sister games are flagged separately. All sources are Korean (KO) unless marked otherwise. Pages fetched 2026-10-12. namu.wiki, thewiki.kr, theqoo, and ppomppu returned HTTP 403, so I could not read namu.wiki directly. DC Inside comment threads did not load in any fetch (header counts showed comments, but the bodies were empty), so only the opening posts are cited.

## 1. What Korean players call it, and is it documented officially?

### Takeaway
Players have no single fixed name for it. They call it "미니게임" (mini-game), "매크로방지" (anti-macro), "점프하는 쿠키 찾기/고르기" (find/pick the jumping cookie), "카드 짝맞추기" (card matching), and "카드뽑기 미니게임" (card-draw mini-game). The mechanism dates back to at least 2014 in the Kakao build. I found no official Devsisters notice, FAQ, or namu.wiki text that describes it.

### Cited Findings
- 2014-10-11, Hungryapp (KO): "일정시간 사용시 미니게임 (카드 짝맞추기, 점프하는 쿠키 고르기 등)이 등장하여 더이상 진행이 막힐 수 있지요." In English: after macros are used for a certain period, mini-games such as card matching or "pick the jumping cookie" appear and can stop further progress. This is the earliest description I found, from the Kakao build. — [Hungryapp 초보를 위한 손크로 설명](https://m.hungryapp.co.kr/bbs/bbs_view.php?bcode=coockirun&pid=577928)
- 2024-04-08, DC Inside (KO). Title: "손크로돌려도 매크로방지뜨는거 정상임?" ("Is it normal for the anti-macro check to appear even when doing 손크로?"). Body: "…한 생명 20개녹인거같은데 점프하는쿠키찾기나옴" ("I think I burned about 20 lives, then 'find the jumping cookie' appeared"). So players use the label 매크로방지. — [DC 1005240](https://gall.dcinside.com/mgallery/board/view/?id=cookierun&no=1005240)
- 2024-04-04, DC Inside (KO), a gallery-staff-style post: "기존에도 매크로 방지용으로 카드뽑기 미니게임이 있었고 매크로 이용자들은 영정을 먹였던 사례도 있었음." In English: a card-draw mini-game already existed for macro prevention, and some macro users received permanent bans (영정 = 영구정지). — [DC 1000564](https://gall.dcinside.com/mgallery/board/view/?id=cookierun&no=1000564)
- 2024-05-11, DC Inside (KO). Title: "카쿠 손크로 미니게임뜨는거 뭐노" ("What's this mini-game that pops up during 카쿠 손크로?"). — [DC 1032066](https://gall.dcinside.com/mgallery/board/view/?id=cookierun&no=1032066)
- Searches for an official Devsisters notice, FAQ, or 고객센터 (customer support) page about this mini-game or about anti-macro sanctions in Cookie Run, Kakao, OvenBreak, or Classic returned nothing. Search results pointed only to the generic support site cookierun.zendesk.com. — search only, no page found

### Inferences
- The global build's "Find the sliding card" check (6 cards, slide vs jump) looks like the same family as the Kakao build's long-running "점프하는 쿠키 찾기/고르기" check. Both show a cookie action, and the player picks the matching cards. The global build may only add a "sliding" variant. This is an inference from the descriptions; I saw no screenshots.
- "카드 짝맞추기" (card matching, 2014) and "카드뽑기" (card draw, 2024) may be older or alternative variants.

### Gaps
- I could not access the namu.wiki pages (쿠키런, 쿠키런/게임 요소, 쿠키런/팁) because they returned 403. Search snippets did not show any 매크로 방지 section.
- I found no official name for the check and no official documentation.

## 2. Reported triggers

### Takeaway
Korean evidence on triggers is thin and anecdotal. Two themes repeat: (a) **extended, repeated or idle play over many runs** ("일정시간 사용시" (after a period of use); about 20 lives in a row), and (b) **input patterns or devices that look automated**: identical tap coordinates, emulator or keyboard input (BlueStacks), and click-assistant apps. Nobody gives a specific run count, a time window, or a night-time effect. No source mentions score or coin thresholds, account reports, IP, or level.

### Cited Findings
- **Period or volume of play:** "일정시간 사용시" ("after a certain period of use") — [Hungryapp 2014](https://m.hungryapp.co.kr/bbs/bbs_view.php?bcode=coockirun&pid=577928). One user saw "점프하는쿠키찾기" after about 20 lives' worth of runs with 손크로. — [DC 1005240, 2024-04-08](https://gall.dcinside.com/mgallery/board/view/?id=cookierun&no=1005240)
- **Definition of 손크로**, which matters because it is mostly not an external macro. It means "손 + 매크로": the player presses start by hand with no outside program, and the combo/pet runs itself while the player does nothing. — [DC 1000564](https://gall.dcinside.com/mgallery/board/view/?id=cookierun&no=1000564). Hungryapp 2014 describes it the same way: the player taps start, lets the cookie run on its own, then taps the result and mystery-box screens by hand. — [Hungryapp](https://m.hungryapp.co.kr/bbs/bbs_view.php?bcode=coockirun&pid=577928)
- **Same-coordinate repeated taps / tap count (speculation):** On 2022-04-13 (tagged [오븐] but about 카쿠 macros on BlueStacks), the author guessed the detection uses "같은 좌표에 반복클릭" (repeated taps on the same coordinate) and a very high tap count. The author called this "뇌피셜" (pure guesswork). With image-search tapping at fixed points, the mini-game still appeared. After the author randomized tap positions inside each button's area, it reportedly stopped appearing: "미니게임이 안뜸. 역시 같은 위치에 반복된 클릭이 문제였던거임" ("the mini-game doesn't appear; the problem was repeated taps at the same spot"). This is one person's self-test. — [DC 682065](https://gall.dcinside.com/mgallery/board/view/?id=cookierun&no=682065)
- **Emulator / keyboard input:** On 2024-05-05, a user who had earlier said the mini-game appears very often ("쥰내게") when running 손크로 on BlueStacks 5 posted that "판테블릿 하나 연결해두고 따로따로 누르니깐 미니게임안나오넹. 키보드가 문제임?" ("with a tablet connected and pressing separately, the mini-game doesn't appear; is the keyboard the problem?"). — [DC 1027983](https://gall.dcinside.com/mgallery/board/view/?id=cookierun&no=1027983)
- **Emulator, first run:** On 2024-05-11, a user installed the game on BlueStacks and saw the mini-game on the very first run: "실행하자마자 첫판만에 미니게임뜨네" ("it popped up on the first run right after launching"). — [DC 1032066](https://gall.dcinside.com/mgallery/board/view/?id=cookierun&no=1032066)
- **Click-assistant apps (a separate block, not the mini-game):** On 2024-04-02, the 11th-anniversary update day, a user wrote "클릭어시스턴트 앱 켜놓고있었는데 실행하니깐 저런거 뜨면서 강제종료됨" ("I had a click-assistant app on; when I launched, that screen appeared and the game force-closed"). The title was "카쿠 이제 매크로 사용못함" ("you can't use macros in 카쿠 anymore"). — [DC 996028](https://gall.dcinside.com/mgallery/board/view/?id=cookierun&no=996028). The 2024-04-04 post reads this update as "데브는 매크로를 완전히 막는 기조로 가는 듯 함" ("Devsisters seems to be moving toward blocking macros completely"). — [DC 1000564](https://gall.dcinside.com/mgallery/board/view/?id=cookierun&no=1000564)

### Inferences
- The check appears for people using plain 손크로 with no external tool (DC 1005240, 2014 Hungryapp). That supports the user's suspicion that the check is not only about automation tools. It probably triggers on volume or repetitiveness of play, such as many consecutive runs with little variation in input. "Little input" is itself typical of 손크로, where the player taps only menu buttons.
- Emulator (BlueStacks) and keyboard-mapped input seem to raise how often it appears (DC 1027983, 1032066). Possible causes are identical tap coordinates from key mapping or emulator fingerprinting. This cannot be confirmed.

### Gaps
- No source gives a numeric threshold (runs, minutes, lives), and none mentions time of day, score or coin per run, combo reuse, rooting, IP, reports, or player level as triggers. Do not assume any of these.
- No Korean source mentions the global build's check.

## 3. Frequency: manual vs macro players, and does everyone get it?

### Takeaway
Reports come almost entirely from people running 손크로 or macros. Players on emulators describe it as very frequent; 2024 handheld-device reports describe it after long sessions. I found no Korean report of a purely hands-on (actively playing) player seeing it, and none saying it never appears for manual play.

### Cited Findings
- Very frequent on BlueStacks 5 during 손크로 ("미니게임쥰내게 나온다"), and none on a tablet with separate taps. — [DC 1027983](https://gall.dcinside.com/mgallery/board/view/?id=cookierun&no=1027983)
- First run on a fresh emulator install. — [DC 1032066](https://gall.dcinside.com/mgallery/board/view/?id=cookierun&no=1032066)
- About 20 lives of 손크로 before it appeared. — [DC 1005240](https://gall.dcinside.com/mgallery/board/view/?id=cookierun&no=1005240)

### Inferences
- Frequency seems to vary with device and input method rather than being uniform. That fits a risk-score or heuristic trigger more than a fixed "every N runs" timer, though the evidence is weak.

### Gaps
- I found no statistics and no reports from actively playing manual players. Comment threads, where such reports might be, would not load.

## 4. Consequences of failing or ignoring it, and does passing reset anything?

### Takeaway
Korean sources say the check **blocks further progress** ("더이상 진행이 막힐 수 있지요"). A gallery post claims some macro users got **permanent bans (영정)**, but it does not say whether failing the mini-game caused them. I found nothing on per-failure penalties, lost run rewards, timeouts, or whether passing resets a counter.

### Cited Findings
- Progress is blocked: "더이상 진행이 막힐 수 있지요" ("further progress can be blocked"). — [Hungryapp 2014](https://m.hungryapp.co.kr/bbs/bbs_view.php?bcode=coockirun&pid=577928)
- Permanent bans for macro users: "매크로 이용자들은 영정을 먹였던 사례도 있었음" ("there were cases of macro users being permanently banned"). The post also says users who macro on their own risk account suspension. — [DC 1000564](https://gall.dcinside.com/mgallery/board/view/?id=cookierun&no=1000564)
- Macros could bring sanctions (제재) and usually required rooting (2014 claim): "매크로는 루팅 및 기타 불법적인 요소로 인해 제재를 받을 수 있으며" ("macros can lead to sanctions because of rooting and other illegal elements"). — [Hungryapp](https://m.hungryapp.co.kr/bbs/bbs_view.php?bcode=coockirun&pid=577928)
- Players were afraid of 정지 (suspension) and asked whether macros get you banned, with no confirmed answer in the opening posts. 2025-01-27: "돌리면 정지 먹을까봐 무섭다" ("I'm scared I'll get suspended if I run it") — [DC 1148152](https://gall.dcinside.com/mgallery/board/view/?id=cookierun&no=1148152). 2020-02-27: [tdgall 80396677](https://tdgall.com/80396677). On 2025-12-15 a user guessed that tools which only auto-start 손크로 would not get you suspended. — [DC 1264046](https://gall.dcinside.com/mgallery/board/view/?id=cookierun&no=1264046)

### Inferences
- No source links the 영정 cases directly to failing the mini-game; they may come from separate detection.

### Gaps
- Nothing found on: what happens after 3 failed tries, cooldowns, whether the run's rewards are lost, whether ignoring or closing the app is penalized, or whether passing resets anything.

## 5. Official Devsisters statements on anti-macro policy (Cookie Run Kakao/Classic and sister games)

### Takeaway
I found no official Devsisters notice, FAQ, or patch note on anti-macro checks or macro sanctions for Cookie Run for Kakao/Classic, OvenBreak, or Kingdom. The only "policy" evidence is indirect: the 2024-04-02 11th-anniversary update apparently started force-closing the game when click-assistant apps run (user report).

### Cited Findings
- Click-assistant app detection and force-close in the Kakao build after the 2024-04-02 update (user report with a screenshot I could not view). — [DC 996028](https://gall.dcinside.com/mgallery/board/view/?id=cookierun&no=996028)
- OvenBreak: searches turned up namu.wiki controversy pages (abuse of Play Points, leaks, and scores zeroed for 대리 플레이 (paid account piloting), per search-result summaries), but no macro-specific official notice. I could not verify these because namu.wiki returned 403. — [namu.wiki 쿠키런: 오븐브레이크/논란](https://namu.wiki/w/%EC%BF%A0%ED%82%A4%EB%9F%B0:%20%EC%98%A4%EB%B8%90%EB%B8%8C%EB%A0%88%EC%9D%B4%ED%81%AC/%EB%85%BC%EB%9E%80) (not directly read)
- A 2026-10-13 OvenBreak-tagged post complains that the "미니게임 최고난도" (highest-difficulty mini-game) is too hard to clear before the event ends. This is almost certainly an **event** mini-game, not an anti-macro check, and is unrelated. — [DC 1352745](https://gall.dcinside.com/mgallery/board/view/?id=cookierun&no=1352745)
- Global Classic launched 2026-06-25 and was #1 in Thai App Store grossing within 3 days. No anti-macro info. — [Nate News 2026-06-29](https://news.nate.com/view/20260629n26397)

### Gaps
- Devsisters' Korean terms of service, the operating policy (운영정책), and in-game notices were not found or read. They would be the place to look for an official macro clause.
- I found no Korean coverage of the global build's "Find the sliding card" check.
