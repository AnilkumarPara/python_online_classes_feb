import time
import numpy as np

start_time = time.time()
np.array(range(1, 1000000))
end_time = time.time()

print("Time taken to perform the function =", end_time-start_time)
