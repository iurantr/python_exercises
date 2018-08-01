import time
print(time.time())
print(time.localtime())
# tm_dst - heur d'ètè
print(time.strftime("%A %d %B %Y, %H:%M:%S"))
time.sleep(2) # in seconds


import calendar
cal = calendar.month(2018,8)
print("Août 2018 : {}".format(cal))

import datetime
today = datetime.date.today()
print(today)
print(datetime.datetime.now())


