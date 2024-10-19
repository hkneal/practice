"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.



Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""


def romanToInt(s: str) -> int:

    sum = 0

    while len(s) >= 1:

        indx = s.find("CM")
        if indx >=0:
            sum = sum + 900
            s = s[:indx] + s[indx+2:]
            print(f"CM Pulled: {s}, Indx: {indx}, Sum: {sum}")

        indx = s.find("CD")
        if indx >=0:
            sum = sum + 400
            s = s[:indx] + s[indx+2:]
            print(f"CD Pulled: {s}, Indx: {indx}, Sum: {sum}")

        indx = s.find("XC")
        if indx >=0:
            sum = sum + 90
            s = s[:indx] + s[indx+2:]
            print(f"XC Pulled: {s}, Indx: {indx}, Sum: {sum}")

        indx = s.find("XL")
        if indx >=0:
            sum = sum + 40
            s = s[:indx] + s[indx+2:]
            print(f"XL Pulled: {s}, Indx: {indx}, Sum: {sum}")

        indx = s.find("IX")
        if indx >=0:
            sum = sum + 9
            s = s[:indx] + s[indx+2:]

        indx = s.find("IV")
        if indx >=0:
            sum = sum + 4
            s = s[:indx] + s[indx+2:]

        indx = s.find("III")
        if indx >=0:
            sum = sum + 3
            s = s[:indx] + s[indx+3:]

        indx = s.find("II")
        if indx >=0:
            sum = sum + 2
            s = s[:indx] + s[indx+2:]

        indx = s.find("I")
        if indx >=0:
            sum = sum + 1
            s = s[:indx] + s[indx+1:]

        indx = s.find("V")
        if indx >=0:
            sum = sum + 5
            s = s[:indx] + s[indx+1:]

        indx = s.find("X")
        if indx >=0:
            sum = sum + 10
            s = s[:indx] + s[indx+1:]

        indx = s.find("L")
        if indx >=0:
            sum = sum + 50
            s = s[:indx] + s[indx+1:]

        indx = s.find("C")
        if indx >=0:
            sum = sum + 100
            s = s[:indx] + s[indx+1:]

        indx = s.find("D")
        if indx >=0:
            sum = sum + 500
            s = s[:indx] + s[indx+1:]

        indx = s.find("M")
        if indx >=0:
            sum = sum + 1000
            s = s[:indx] + s[indx+1:]

    return sum


print(romanToInt("MCDLXXVI" ))