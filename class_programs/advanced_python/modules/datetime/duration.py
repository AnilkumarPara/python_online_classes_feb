from datetime import datetime
# date1 = datetime(2023, 4, 22, 18,0,0)
# # date2 = datetime.today()
# date2 = datetime(2022,11,5,6,7,10)
# print(date1)
# print(date2)
# print(date1 - date2)

c_time = datetime.now()
utc_time = datetime.utcnow()
print(c_time - utc_time)
print(c_time.weekday())
