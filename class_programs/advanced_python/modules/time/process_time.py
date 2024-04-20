import time
import numpy as np
start_time = time.process_time()
np.array(range(1, 10000000))
end_time = time.process_time()
print("process time taken for the function execution=", end_time-start_time)
