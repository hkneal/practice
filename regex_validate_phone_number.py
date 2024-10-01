"""A valid mobile number is a ten digit number starting with a  or .

Concept

A valid mobile number is a ten digit number starting with a  or .

Regular expressions are a key concept in any programming language. A quick explanation with Python examples is available here. You could also go through the link below to read more about regular expressions in Python.

https://developers.google.com/edu/python/regular-expressions

Input Format

The first line contains an integer , the number of inputs.
 lines follow, each containing some string.

Constraints



Output Format

For every string listed, print "YES" if it is a valid mobile number and "NO" if it is not on separate lines. Do not print the quotes.

Sample Input

2
9587456281
1252478965
Sample Output

YES
NO
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
pattern = r"(^[7,8,9]{1}[0-9]{9})$"

if __name__ == "__main__":
    for _ in range(int(input().rstrip())):
        s = input()
        if re.match(pattern, s):
            print("YES")
        else:
            print("NO")