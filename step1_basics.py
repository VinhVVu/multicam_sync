# STEP 1: Basic Camera Timing
FPS = 60
frame_interval = 1.0 / FPS
print(f"At {FPS} FPS, one frame arrives every {frame_interval:.4f} seconds")

actual_times = [0.0167, 0.0340, 0.0491, 0.0672, 0.0833]
expected_times = [frame_interval * i for i in range(1, 6)]

print("\nFrame | Expected    | Actual      | Drift")
print("-" * 50)

for i in range(5):
    drift = actual_times[i] - expected_times[i]
    drift_ms = drift * 1000
    print(f"  {i+1}   | {expected_times[i]:.4f}s     | {actual_times[i]:.4f}s     | {drift_ms:+.2f}ms")
