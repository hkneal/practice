"""Return the n value of fibonacci """
from datetime import datetime

def fib(n: int) -> int:

    if n == 0: return 0
    if n == 1: return 1

    return fib(n-1) + fib(n-2)

timestamp = datetime.now()
print(fib(40))
time_spent = datetime.now() - timestamp
print(f"{time_spent.min} minutes, {time_spent.seconds} seconds, {time_spent.microseconds} microseconds")

#0 1 2 3 4 5 6  7 8  9  10
#0 1 1 2 3 5 8 13 21 34 55

#More efficiently

def build_fibs(n:int) ->int:
    fibs = [0,1]
    for i in range(2, n+1):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs[n]

timestamp = datetime.now()
print(build_fibs(1000))
time_spent = datetime.now() - timestamp
print(f"{time_spent.seconds} seconds, {time_spent.microseconds} microseconds")