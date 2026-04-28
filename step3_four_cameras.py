# STEP 3: Four Cameras + Auto Status Detection
# ==============================================
# Now we scale to 4 cameras.
# We pick one camera as the MASTER (cam1) and check
# if all others are in sync with it.

FPS = 60

# Simulated capture times for 4 cameras (one frame each)
cameras = {
    "cam-01": 0.0167,   # master reference
    "cam-02": 0.0169,   # slightly late
    "cam-03": 0.0181,   # getting close to warning
    "cam-04": 0.0240,   # too far — out of sync!
}

WARN_THRESHOLD  = 3.0   # ms
ERROR_THRESHOLD = 7.0   # ms

master_time = cameras["cam-01"]

print("Camera  | Timestamp   | Drift from Master | Status")
print("-" * 55)

for name, timestamp in cameras.items():
    drift_ms = abs(timestamp - master_time) * 1000

    if drift_ms > ERROR_THRESHOLD:
        status = "❌ ERROR"
    elif drift_ms > WARN_THRESHOLD:
        status = "⚠️  WARN"
    else:
        status = "✅ OK"

    print(f"{name}  | {timestamp:.4f}s     | {drift_ms:.2f}ms             | {status}")
