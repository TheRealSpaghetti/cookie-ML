#!/bin/bash
# Watchdog: checks every 6 min; exits (waking Claude) on stall, bot exit, or lives < 5.
cd /c/Users/leoni/Desktop/cookierun-classic-bot-main
BOTLOG="$1"
while true; do
  sleep 360
  now=$(date +%s)
  age=$(( now - $(stat -c %Y "$BOTLOG") ))
  running=$(powershell -NoProfile -Command "(Get-CimInstance Win32_Process -Filter \"name='python.exe'\" | ? {\$_.CommandLine -like '*main.py*'}).Count")
  lives=$(cut -d, -f2 lives_latest.txt | tr -d '\r\n ')
  echo "$(date '+%H:%M:%S') log_age=${age}s bot_procs=${running} lives=${lives}"
  if [ "${running:-0}" -lt 1 ]; then echo "ALERT: bot not running"; exit 1; fi
  if [ "$age" -gt 480 ]; then echo "ALERT: bot log stale ${age}s"; exit 2; fi
  if [ -n "$lives" ] && [ "$lives" -lt 5 ]; then echo "ALERT: lives $lives"; exit 3; fi
  if [ -z "$lives" ] && [ -z "$SKIP_BLANK" ]; then echo "ALERT: lives unreadable (maybe <10)"; exit 4; fi
done
