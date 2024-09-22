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

