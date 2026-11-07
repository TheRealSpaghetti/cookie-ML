"""Retired. Coin tracking is now built into the bot (coin_ledger.py) and runs on every boot.

Running this alongside the bot would log every run twice, so it only prints a pointer.
For the report, run:  python coin_ledger.py
"""
if __name__ == "__main__":
    print("coin_tracker.py is retired: the bot logs every run to ledger/runs.csv itself.")
    print("For the per-tweak report run:  python coin_ledger.py")
