import time

# This will immediately print each statement
for i in range(3):
    print(f"Number {i}", end=' ', flush=True)
    time.sleep(1)  # Simulating some work
