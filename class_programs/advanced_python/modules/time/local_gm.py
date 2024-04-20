import time
local_time = time.localtime()
# print(local_time)
# print(local_time.tm_hour)

gm_time = time.gmtime()
print(gm_time)
print(gm_time.tm_sec)