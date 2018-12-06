import time
import datetime
from datetime import datetime as dt


a = datetime.datetime(100,1,1,5,30,00)
b = datetime.timedelta(hours=1,minutes=30)
c = datetime.timedelta(hours=9)
d = a - c

e = dt.strptime(str(a.time()), "%H:%M:%S")
print(e.strftime("%I:%M:%S %p"))

print("Time Get up : %s" % a.time())
print("Time sleep : %s" % d.time())
print("Time sleep : %s" % (d + b).time())
print("Time sleep : %s" % (d + b + b).time())
print("Time sleep : %s" % (d + b + b + b).time())

def time_format(time_str):
    time_str = dt.strptime(str(time_str), "%H:%M:%S")
    time_str = time_str.strftime("%I:%M:%S %p")
    return (time_str)

def sleepy(hour, minute):
    time_get_up = datetime.datetime(100,1,1,hour, minute,00)
    night_time = datetime.timedelta(hours=9)
    night_time = time_get_up - night_time
    rule_ninety = datetime.timedelta(hours=1, minutes=30)

    first_time = night_time + rule_ninety
    second_time = night_time + rule_ninety + rule_ninety
    third_time = night_time + rule_ninety + rule_ninety + rule_ninety

    time_get_up = time_format(time_get_up.time())
    night_time = time_format(night_time.time())
    first_time = time_format(first_time.time())
    second_time = time_format(second_time.time())
    third_time = time_format(third_time.time())
    return(time_get_up, night_time, first_time, second_time, third_time)

print(sleepy(5,50))
