"""Returns the time delta between two timestamps (possibly different time zones) in seconds"""
from datetime import datetime

def time_delta(t1: str, t2: str) -> int:
    t1 = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    t2 = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')

    if t1>= t2:
        difference = t1 - t2
    else:
        difference = t2 - t1

    seconds_per_day = 24 * 60 * 60

    print(difference)

    return ((difference.days * seconds_per_day)
            + difference.seconds)

t1 = "Fri 11 Feb 2078 00:05:21 +0400"
t2 = "Mon 29 Dec 2064 03:33:48 -1100"

print(time_delta(t1, t2))
