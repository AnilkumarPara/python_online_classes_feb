import time

time_string = "2023-11-12 17:16:00"
# print(type(time_string))
time_format = "%Y-%m-%d %H:%M:%S"
time_obj = time.strptime(time_string, time_format)
print(type(time_obj))


time_s = time.strftime(time_format, time_obj)
print(type(time_s))
print(time_s)
print(time_s.split('-'))





