import time
import datetime
from datetime import datetime as dt


a = datetime.datetime(100,1,1,5,30,00)
b = datetime.timedelta(hours=1,minutes=30)
c = datetime.timedelta(hours=9)
d = a-c

e = dt.strptime(str(a.time()), "%H:%M:%S")
print(e.strftime("%I:%M:%S %p"))

print("Time Get up : %s" % a.time())
print("Time sleep : %s" % d.time())
print("Time sleep : %s" % (d+b).time())
print("Time sleep : %s" % (d+b+b).time())
print("Time sleep : %s" % (d+b+b+b).time())


def sleepy(hour, minute):
    hour_get_up = datetime.datetime(100,1,1,hour, minute,00)
    hour_get_up = dt.strptime(str(hour_get_up.time()), "%H:%M:%S")
    hour_get_up = hour_get_up.strftime("%I:%M:%S %p")
    return("Time Get up : %s" % hour_get_up)

print(sleepy(5,50))
