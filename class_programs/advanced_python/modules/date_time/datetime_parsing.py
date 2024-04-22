from datetime import datetime

date_string = "2023-11-12 14:30:00"
# print(type(date_string))
date_format = "%Y-%m-%d %H:%M:%S"
date_time_obj = datetime.strptime(date_string, date_format)
# print(type(date_time_obj))
print(date_time_obj)
print(date_time_obj.time().minute)

str_dt = datetime.strftime(date_time_obj, date_format)
print(type(str_dt))
print(str_dt)
