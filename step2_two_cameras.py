# STEP 2: Two Cameras — Are They In Sync?
# =========================================
# Now we have 2 cameras. Both should capture at the same moment.
# If camera 1 captures at t=0.0167s but camera 2 captures at t=0.0185s
# that 1.8ms difference will break 3D reconstruction.

FPS = 60
frame_interval = 1.0 / FPS

# Each camera has slightly different actual capture times (real hardware is never perfect)
cam1_times = [0.0167, 0.0334, 0.0500, 0.0667, 0.0834]
cam2_times = [0.0169, 0.0331, 0.0508, 0.0661, 0.0839]

print("Frame | Cam1        | Cam2        | Sync Drift  | Status")
print("-" * 65)

for i in range(5):
    sync_drift = abs(cam1_times[i] - cam2_times[i]) * 1000  # ms
    status = "OK" if sync_drift < 3.0 else "WARNING"
    print(f"  {i+1}   | {cam1_times[i]:.4f}s     | {cam2_times[i]:.4f}s     | {sync_drift:.2f}ms       | {status}")
