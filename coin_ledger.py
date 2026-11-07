"""Coin ledger: built-in coin tracking for every run, in one records.csv.

The bot creates one CoinLedger at boot. It:
  - works out the bot "version" (V1, V2, ...): a new version is opened whenever the run
    settings or VERSION_NOTE in config.py change (kept in ledger/versions.csv, internal),
  - prints a per-version comparison report,
  - reads the coin balance at the main menu after every run and appends one row per run
    to records.csv, including running averages for the current version.

Every bot session starts with a fresh baseline: the first main-menu balance after boot is
only a starting point, so coins spent by hand while the bot is off never show up as a loss.

Run `python coin_ledger.py` at any time to print the report without starting the bot.
Coin reads use Windows OCR (ocr_coins.ps1) and must agree on two separate frames.
"""
import csv
import hashlib
import json
import math
import os
import re
import statistics
import subprocess
import tempfile
import threading
import time
from datetime import datetime

import cv2

import config

HERE = os.path.dirname(os.path.abspath(__file__))
RECORDS_PATH = os.path.join(HERE, "records.csv")
LEDGER_DIR = os.path.join(HERE, "ledger")
VERSIONS_PATH = os.path.join(LEDGER_DIR, "versions.csv")
LEGACY_RUNS_PATH = os.path.join(HERE, "coin_runs.csv")  # written by the old standalone coin_tracker.py
LIVES_PATH = os.path.join(HERE, "lives_latest.txt")
OCR_SCRIPT = os.path.join(HERE, "ocr_coins.ps1")

RECORD_FIELDS = [
    "time", "version", "version_note", "session", "run", "status",
    "coins_earned", "run_s", "relay_at_s", "cycle_s", "coins_per_sec", "jumps",
    "balance", "extra_lives",
    "version_runs", "avg_coins_per_run", "avg_coins_per_sec", "lifetime_coins",
]
VERSION_FIELDS = ["version", "started", "note", "changes", "fingerprint", "settings"]

COIN_BOX = (545, 12, 695, 56)  # x1, y1, x2, y2 of the coin counter in 1280x720
LIVES_BOX = (955, 14, 1035, 50)
# A per-run net outside this range is treated as a misread, not a real result.
PLAUSIBLE_NET_PER_RUN = (-100_000, 500_000)
# Rows with these statuses count toward averages; the others are kept only for the record.
COUNTED_STATUSES = {"ok", "backfill", "legacy"}
# Old-tracker rows have no run markers; a gap longer than this is not one clean cycle.
LEGACY_MAX_CYCLE_S = 450


# -------------------
# SETTINGS / VERSIONS
# -------------------
def settings_snapshot(options):
    """Everything that defines a version: run options, auto-jump config and the version note."""
    opts = {k: v for k, v in options.items() if k != "desired_boost_template"}
    return {
        "note": getattr(config, "VERSION_NOTE", ""),
        "options": opts,
        "auto_jump_interval": list(config.AUTO_JUMP_INTERVAL),
        "stop_jumping_after_relay": config.STOP_JUMPING_AFTER_RELAY,
        "jump_button": list(config.JUMP_BUTTON),
    }


def fingerprint(settings):
    return hashlib.sha1(json.dumps(settings, sort_keys=True).encode()).hexdigest()[:10]


def _flatten(d, prefix=""):
    out = {}
    for k, v in d.items():
        if isinstance(v, dict):
            out.update(_flatten(v, f"{prefix}{k}."))
        else:
            out[f"{prefix}{k}"] = v
    return out


def describe_changes(old, new):
    if old is None:
        return "first version"
    a, b = _flatten(old), _flatten(new)
    parts = [f"{k}: {a.get(k)} -> {b.get(k)}" for k in sorted(set(a) | set(b)) if a.get(k) != b.get(k)]
    return "; ".join(parts) or "no change"


# -------------------
# FILES
# -------------------
def _read_csv(path):
    if not os.path.exists(path):
        return []
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def _append_csv(path, fields, row):
    new_file = not os.path.exists(path)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        if new_file:
            w.writeheader()
        w.writerow(row)


def load_records():
    return _read_csv(RECORDS_PATH)


def load_versions():
    return _read_csv(VERSIONS_PATH)


def _blank(v, digits=0):
    if v is None or v == "":
        return ""
    return round(v, digits) if digits else round(v)


def append_record(time_str, version, note, session, run, status, coins, run_s, relay_s, cycle_s,
                  jumps, balance, lives):
    """Append one run to records.csv, filling in the running averages for its version."""
    records = load_records()
    counted = [r for r in records if r["status"] in COUNTED_STATUSES and r["coins_earned"]]
    if status in COUNTED_STATUSES and coins is not None:
        counted.append({"version": version, "coins_earned": str(coins), "cycle_s": "" if cycle_s is None else str(round(cycle_s))})
    mine = [r for r in counted if r["version"] == version]
    nets = [int(r["coins_earned"]) for r in mine]
    timed = [(int(r["coins_earned"]), int(r["cycle_s"])) for r in mine if r["cycle_s"] and int(r["cycle_s"]) > 0]
    row = {
        "time": time_str, "version": version, "version_note": note, "session": session, "run": run,
        "status": status, "coins_earned": "" if coins is None else coins,
        "run_s": _blank(run_s), "relay_at_s": _blank(relay_s), "cycle_s": _blank(cycle_s),
        "coins_per_sec": _blank(coins / cycle_s, 1) if coins is not None and cycle_s else "",
        "jumps": "" if jumps is None else jumps,
        "balance": "" if balance is None else balance, "extra_lives": "" if lives is None else lives,
        "version_runs": len(nets),
        "avg_coins_per_run": round(statistics.mean(nets)) if nets else "",
        "avg_coins_per_sec": round(sum(n for n, _ in timed) / sum(c for _, c in timed), 1) if timed else "",
        "lifetime_coins": sum(int(r["coins_earned"]) for r in counted),
    }
    _append_csv(RECORDS_PATH, RECORD_FIELDS, row)
    return row


def import_legacy_runs(version, note):
    """Pull rows from the old tracker's coin_runs.csv that are newer than records.csv, then archive it."""
    if not os.path.exists(LEGACY_RUNS_PATH):
        return 0
    last_time = max((r["time"] for r in load_records()), default="")
    added, prev_time = 0, None
    for r in _read_csv(LEGACY_RUNS_PATH):
        t = r["time"]
        gap = (datetime.fromisoformat(t) - datetime.fromisoformat(prev_time)).total_seconds() if prev_time else None
        prev_time = t
        if t <= last_time:
            continue
        append_record(t, version, note, "old tracker", int(r["run"]), "legacy", int(r["net"]), None, None,
                      gap if gap is not None and gap <= LEGACY_MAX_CYCLE_S else None, None, int(r["balance"]), None)
        added += 1
    archive = os.path.join(LEDGER_DIR, "archive", f"coin_runs_legacy_{datetime.now():%Y%m%d_%H%M%S}.csv")
    os.makedirs(os.path.dirname(archive), exist_ok=True)
    os.replace(LEGACY_RUNS_PATH, archive)
    return added


# -------------------
# OCR
# -------------------
def _ocr(path):
    try:
        return subprocess.run(["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", OCR_SCRIPT, path],
                              capture_output=True, text=True, timeout=30).stdout
    except Exception:
        return ""


def read_coins(img):
    x1, y1, x2, y2 = COIN_BOX
    # Windows OCR sometimes misses 7-digit numbers at one scale, so try a few.
    for scale in (1, 1.5, 3, 2):
        crop = cv2.resize(img[y1:y2, x1:x2], None, fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)
        _, bw = cv2.threshold(cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY), 200, 255, cv2.THRESH_BINARY_INV)
        bw = cv2.copyMakeBorder(bw, 60, 60, 60, 60, cv2.BORDER_CONSTANT, value=255)
        path = os.path.join(tempfile.gettempdir(), "coin_ledger_crop.png")
        cv2.imwrite(path, bw)
        digits = re.sub(r"[^0-9]", "", _ocr(path))
        if 3 <= len(digits) <= 9:
            return int(digits)
    return None


def read_extra_lives(img):
    """Read the '+N' extra-lives number next to the hearts. None if not readable (e.g. fewer than 10)."""
    x1, y1, x2, y2 = LIVES_BOX
    crop = cv2.resize(img[y1:y2, x1:x2], None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)
    _, bw = cv2.threshold(cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY), 120, 255, cv2.THRESH_BINARY)
    bw = cv2.copyMakeBorder(bw, 40, 40, 40, 40, cv2.BORDER_CONSTANT, value=255)
    path = os.path.join(tempfile.gettempdir(), "coin_ledger_lives.png")
    cv2.imwrite(path, bw)
    digits = re.sub(r"[^0-9]", "", _ocr(path))
    return int(digits) if digits else None


# -------------------
# LEDGER
# -------------------
class CoinLedger:
    def __init__(self, options, capture_screen, is_main_menu):
        """capture_screen() returns a fresh frame; is_main_menu(img) says whether it shows the main menu."""
        self._capture = capture_screen
        self._is_main_menu = is_main_menu
        self._lock = threading.Lock()
        self._worker = None
        self.session = datetime.now().strftime("%Y-%m-%d %H:%M")
        # No balance carries over from an earlier session: the first menu read is a fresh baseline.
        self.balance = None
        self.balance_time = None
        self.runs_pending = 0
        self.run_stats = None
        self.run_in_session = 0

        self.version, self.note = self._register_version(settings_snapshot(options))
        imported = import_legacy_runs(self.version, self.note)
        if imported:
            print(f"📒 Imported {imported} run(s) from the old coin_runs.csv into {self.version}.")
        print_report()
        print(f"📒 Coin ledger on. Logging every run to records.csv as {self.version}.")

    def _register_version(self, settings):
        versions = load_versions()
        fp = fingerprint(settings)
        last = versions[-1] if versions else None
        if last and last["fingerprint"] == fp:
            print(f"📒 Settings unchanged: continuing {last['version']} ({last['note'] or 'no note'}).")
            return last["version"], last["note"]
        version = f"V{len(versions) + 1}"
        changes = describe_changes(json.loads(last["settings"]) if last else None, settings)
        _append_csv(VERSIONS_PATH, VERSION_FIELDS, {
            "version": version, "started": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "note": settings["note"], "changes": changes, "fingerprint": fp,
            "settings": json.dumps(settings, sort_keys=True),
        })
        print(f"📒 New version {version}: {settings['note'] or 'no note'}")
        print(f"   Changes: {changes}")
        if last and settings["note"] == json.loads(last["settings"]).get("note"):
            print("   ⚠️ Settings changed but VERSION_NOTE in config.py did not. Update it so the record says why.")
        return version, settings["note"]

    # Called by the bot ------------------------------------------------------
    def on_run_start(self):
        with self._lock:
            self.runs_pending += 1
            self.run_stats = None

    def on_run_complete(self, run_s, relay_s, jumps):
        with self._lock:
            self.run_stats = (run_s, relay_s, jumps)

    def on_main_menu(self):
        """Start a background balance read if a run finished since the last read (or no balance yet)."""
        with self._lock:
            if self._worker is not None and self._worker.is_alive():
                return
            if self.balance is not None and self.runs_pending == 0:
                return
            runs, stats = self.runs_pending, self.run_stats
            self.runs_pending, self.run_stats = 0, None
        self._worker = threading.Thread(target=self._safe_read_and_log, args=(runs, stats), daemon=True)
        self._worker.start()

    # Internals --------------------------------------------------------------
    def _safe_read_and_log(self, runs, stats):
        try:
            self._read_and_log(runs, stats)
        except Exception as e:  # tracking must never take the bot down
            print(f"📒 ⚠️ Coin ledger error (bot unaffected): {e}")

    def _confirmed_balance(self):
        """Read the balance on fresh main-menu frames until two reads agree. Returns (balance, frame)."""
        reads, frame = [], None
        for _ in range(5):
            img = self._capture()
            if img is not None and self._is_main_menu(img):
                frame = img
                value = read_coins(img)
                if value is not None:
                    if value in reads:
                        return value, frame
                    reads.append(value)
            time.sleep(1)
        return None, frame

    def _read_and_log(self, runs, stats):
        balance, frame = self._confirmed_balance()
        now = datetime.now()
        lives = None
        if frame is not None:
            lives = read_extra_lives(frame)
            with open(LIVES_PATH, "w") as f:
                f.write(f"{now:%Y-%m-%d %H:%M:%S},{'' if lives is None else lives}\n")

        prev_balance, prev_time = self.balance, self.balance_time
        if balance is None:
            print("📒 ⚠️ Could not confirm the coin balance (two reads never agreed).")
            self.balance = self.balance_time = None
            if runs and prev_balance is not None:
                self._log_run(now, None, None, stats, None, lives, "unread")
            return
        self.balance, self.balance_time = balance, now
        if prev_balance is None:
            print(f"📒 Coin balance: {balance:,} (starting point for the next run)")
            return
        if runs == 0:
            return

        net = balance - prev_balance
        cycle = (now - prev_time).total_seconds()
        lo, hi = PLAUSIBLE_NET_PER_RUN
        if not (lo * runs <= net <= hi * runs):
            status = "suspect"
            self.balance = self.balance_time = None  # take a fresh starting point at the next menu visit
        elif runs > 1:
            status = f"multi ({runs} runs)"
        elif stats is None:
            status = "incomplete"  # run started but the results screen was never seen
        else:
            status = "ok"
        self._log_run(now, balance, net, stats, cycle, lives, status)

    def _log_run(self, now, balance, net, stats, cycle, lives, status):
        self.run_in_session += 1
        run_s, relay_s, jumps = stats if stats else (None, None, None)
        row = append_record(now.strftime("%Y-%m-%d %H:%M:%S"), self.version, self.note, self.session,
                            self.run_in_session, status, net, run_s, relay_s, cycle, jumps, balance, lives)
        if net is None:
            print(f"📒 Run {self.run_in_session} [{self.version}]: balance unreadable, not counted ({status}).")
            return
        rate = f", {row['coins_per_sec']:,} coins/s" if row["coins_per_sec"] != "" else ""
        note = "" if status == "ok" else f" ({status}, not counted in averages)"
        print(f"📒 Run {self.run_in_session} [{self.version}]: {net:+,} coins{rate}{note}. "
              f"{self.version} avg {row['avg_coins_per_run']:,}/run, {row['avg_coins_per_sec']}/s "
              f"over {row['version_runs']} runs.")


# -------------------
# REPORT
# -------------------
def print_report():
    versions, records = load_versions(), load_records()
    if not versions:
        print("📒 No versions recorded yet.")
        return
    print("📒 ===== Coin records: results per version =====")
    print(f"   {'ver':<4} {'runs':>4} {'avg/run':>9} {'±95%':>7} {'coins/s':>8} {'coins/h':>7} "
          f"{'run s':>5} {'relay':>5} {'jumps':>5}  vs prev")
    prev = None
    for v in versions:
        rows = [r for r in records if r["version"] == v["version"] and r["status"] in COUNTED_STATUSES
                and r["coins_earned"]]
        if not rows:
            print(f"   {v['version']:<4} {0:>4}   (no counted runs)  {v['note']}")
            continue
        nets = [int(r["coins_earned"]) for r in rows]
        mean = statistics.mean(nets)
        ci = 1.96 * statistics.stdev(nets) / math.sqrt(len(nets)) if len(nets) > 1 else None
        timed = [(int(r["coins_earned"]), int(r["cycle_s"])) for r in rows if r["cycle_s"] and int(r["cycle_s"]) > 0]
        cps = sum(n for n, _ in timed) / sum(c for _, c in timed) if timed else None
        avg = lambda col: statistics.mean(int(r[col]) for r in rows if r[col]) if any(r[col] for r in rows) else None
        fmt = lambda x, f: f.format(x) if x is not None else "-"
        delta = ""
        if prev:
            delta = f"{(mean / prev[0] - 1) * 100:+.0f}%/run"
            if cps and prev[1]:
                delta += f", {(cps / prev[1] - 1) * 100:+.0f}%/s"
        print(f"   {v['version']:<4} {len(nets):>4} {mean:>9,.0f} {fmt(ci, '{:,.0f}'):>7} {fmt(cps, '{:,.0f}'):>8} "
              f"{fmt(cps and cps * 3600 / 1e6, '{:.2f}M'):>7} {fmt(avg('run_s'), '{:.0f}'):>5} "
              f"{fmt(avg('relay_at_s'), '{:.0f}'):>5} {fmt(avg('jumps'), '{:.0f}'):>5}  {delta}")
        print(f"         {v['started'][:16]}  {v['note']}")
        prev = (mean, cps)
    print("   (coins/s = coins earned / real time between menu visits, so menus, lives and resets count.)")
    print("📒 ==============================================")


if __name__ == "__main__":
    print_report()
