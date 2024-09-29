"""Practicing with groups, hackerrank
https://www.hackerrank.com/challenges/re-group-groups/problem?isFullScreen=true

"""
import re
pattern = r"(?=[^aeiou]([aeiou]{2,})[^aeiou])"
s = "raabcdeefgyYhFjkIoomnpOeorteeeeet"
m = re.findall(pattern, s, re.IGNORECASE)
if m:
    for grp in m:
        print("".join(grp))