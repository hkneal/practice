"""Return the n value of fibonacci """
from datetime import datetime
from functools import lru_cache

def fib(n: int) -> int:

    if n == 0: return 0
    if n == 1: return 1

    return fib(n-1) + fib(n-2)

num = 42
timestamp = datetime.now()
print(fib(num))
time_spent = datetime.now() - timestamp
print(f"Ran fib {num}")
print(f"{time_spent.seconds} seconds, {time_spent.microseconds} microseconds")
print("\n")

#0 1 2 3 4 5 6  7 8  9  10
#0 1 1 2 3 5 8 13 21 34 55

#More efficiently

def build_fibs(n:int) ->int:
    fibs = [0,1]
    for i in range(2, n+1):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs[n]

num = 42
timestamp = datetime.now()
print(build_fibs(num))
time_spent = datetime.now() - timestamp
print(f"Ran build_fib {num}")
print(f"{time_spent.seconds} seconds, {time_spent.microseconds} microseconds")
print("\n")

# writing my own cache decorator

def fib_cache(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@fib_cache
def decorated_fib(n: int) -> int:
    if n <= 2:
        return 1
    return decorated_fib(n-1) + decorated_fib(n-2)

num = 42
timestamp = datetime.now()
print(decorated_fib(num))
time_spent = datetime.now() - timestamp
print(f"Ran decorated_fib {num}")
print(f"{time_spent.seconds} seconds, {time_spent.microseconds} microseconds")
print("\n")



# Dynamic top down programming using caching

@lru_cache(maxsize=None)
def cached_fib(n: int) -> int:
    if n <= 2:
        return 1
    return cached_fib(n-1) + cached_fib(n-2)

num = 42
timestamp = datetime.now()
print(cached_fib(num))
time_spent = datetime.now() - timestamp
print(f"Ran cached_fib {num}")
print(f"{time_spent.seconds} seconds, {time_spent.microseconds} microseconds")
