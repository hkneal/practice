"""Practicing regex"""
import re
try:

    pattern = re.compile(".*+ ")
    print(pattern)
except Exception:
    print("False")

x = int(input())

for _ in range(x):
    try:
        re.compile(input())
        print("True")
    except Exception:
        print("False")


# pattern = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
"""
emailValidator = re.compile("^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+.[a-zA-Z]{1,3}$")

def fun(s): return emailValidator.match(s)
"""

