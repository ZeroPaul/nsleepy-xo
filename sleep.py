import time
import datetime


a = datetime.datetime(100,1,1,6,00,00)
b = datetime.timedelta(hours=1,minutes=30)
c = datetime.timedelta(hours=9)
d = a-c

print (a.time())
print(d.time())
print((d+b).time())
print((d+b+b).time())
print((d+b+b+b).time())
