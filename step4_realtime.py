# STEP 4: Real-Time Loop
# ======================
# Instead of hardcoded times, cameras now capture
# frames continuously using the actual system clock.
# This is how a real monitoring system works.

import time
import random

FPS = 10  # keep low so you can see it updating
FRAME_INTERVAL = 1.0 / FPS
WARN_THRESHOLD  = 3.0   # ms
ERROR_THRESHOLD = 7.0   # ms
NUM_CAMERAS = 4

print(f"Starting real-time monitor — {NUM_CAMERAS} cameras @ {FPS}fps")
print("Press Ctrl+C to stop\n")

frame = 0

try:
    while True:
        frame += 1
        master_time = time.time()   # real system clock!

        print(f"--- Frame {frame} ---")

        for i in range(1, NUM_CAMERAS + 1):
            # Simulate each camera having slight hardware jitter
            jitter = random.gauss(0, 0.008)   # 2ms standard deviation
            cam_time = master_time + jitter
            drift_ms = abs(cam_time - master_time) * 1000

            if drift_ms > ERROR_THRESHOLD:
                status = "❌ ERROR"
            elif drift_ms > WARN_THRESHOLD:
                status = "⚠️  WARN"
            else:
                status = "✅ OK"

            print(f"  cam-{i:02d} | drift={drift_ms:.2f}ms | {status}")

        print()
        time.sleep(FRAME_INTERVAL)   # wait for next frame

except KeyboardInterrupt:
    print("Monitor stopped.")
