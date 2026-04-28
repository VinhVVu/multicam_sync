# main.py
# =======
# Multi-Camera Sync Monitor — Full System
# Combines everything from steps 1-4 into
# one clean production-style script.
# Author: Vinh Vu

import time
import random

# ── Config ────────────────────────────────
NUM_CAMERAS     = 4
FPS             = 10
DURATION_SEC    = 5
WARN_THRESHOLD  = 3.0   # ms
ERROR_THRESHOLD = 7.0   # ms
NOISE_STD       = 0.002 # seconds (2ms jitter)
# ──────────────────────────────────────────

def check_status(drift_ms):
    if drift_ms > ERROR_THRESHOLD:
        return "ERROR"
    elif drift_ms > WARN_THRESHOLD:
        return "WARN"
    return "OK"

def run():
    # Track stats per camera
    stats = {
        f"cam-{i+1:02d}": {"ok": 0, "warn": 0, "error": 0, "drifts": []}
        for i in range(NUM_CAMERAS)
    }

    total_frames = int(FPS * DURATION_SEC)
    print(f"\n{'='*50}")
    print(f"  Multi-Camera Sync Monitor — Vinh Vu")
    print(f"  {NUM_CAMERAS} cameras | {FPS} FPS | {DURATION_SEC}s duration")
    print(f"{'='*50}\n")

    for frame in range(1, total_frames + 1):
        master_time = time.time()

        for i in range(NUM_CAMERAS):
            name = f"cam-{i+1:02d}"
            jitter = random.gauss(0, NOISE_STD)
            drift_ms = abs(jitter) * 1000
            status = check_status(drift_ms)
            stats[name][status.lower()] += 1
            stats[name]["drifts"].append(drift_ms)

        time.sleep(1.0 / FPS)

    # ── Summary Report ────────────────────
    print(f"{'='*50}")
    print(f"  SUMMARY REPORT")
    print(f"{'='*50}")
    print(f"  {'Camera':<10} {'OK':>6} {'WARN':>6} {'ERROR':>6} {'Avg Drift':>10}")
    print(f"  {'-'*44}")

    for name, s in stats.items():
        avg = sum(s["drifts"]) / len(s["drifts"])
        print(f"  {name:<10} {s['ok']:>6} {s['warn']:>6} {s['error']:>6} {avg:>9.2f}ms")

    total = sum(s["ok"] + s["warn"] + s["error"] for s in stats.values())
    total_ok = sum(s["ok"] for s in stats.values())
    sync_rate = (total_ok / total) * 100
    print(f"\n  Sync Rate: {sync_rate:.1f}%")
    print(f"{'='*50}\n")

if __name__ == "__main__":
    run()
