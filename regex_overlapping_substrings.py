"""Regex practice

Get the indices of all overlapping substrings using regex

Sample Input

aaadaa
aa
Sample Output

(0, 1)
(1, 2)
(4, 5)

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

if __name__ == "__main__":
    source, pattern = input().strip(), input().strip()
    # print(source, pattern)
    matches = re.finditer(fr"(?=({pattern}))", source)
    if pattern not in source:
        print((-1, -1))

    elif matches:
        for match in matches:
            print((match.start(1), match.end(1)-1) or (-1, -1))