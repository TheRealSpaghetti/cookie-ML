# Starts the bot unattended, answering yes to every option and picking boost #1 (Double Coins).
# Answers: Fast Start, Cookie Relay, HP Extension, Power Jelly, Double XP,
# Desired Random Boost, boost number 1, Auto-jump, Detect Relic.
$env:PYTHONIOENCODING = 'utf-8'
Set-Location $PSScriptRoot
"y`ny`ny`ny`ny`ny`n1`ny`ny`n" | Set-Content -Encoding ascii bot_answers.txt
cmd /c "python -u main.py < bot_answers.txt"
