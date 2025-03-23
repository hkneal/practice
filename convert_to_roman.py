"""Roman numerals are formed by appending the conversions of decimal place values from highest to lowest.
Converting a decimal place value into a Roman numeral has the following rules:

1) If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted
from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.

2) If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following
symbol, for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following
subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).

3) Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of
10. You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use
the subtractive form.

Seven different symbols represent Roman numerals with the following values:

Symbol	Value
I	1
V	5
X	10
L	50
C	100
D	500
M	1000


Given an integer, convert it to a Roman numeral.

"""
import math

class Solution:
    def intToRoman(self, num: int) -> str:

        romans = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }

        roman_numeral = ""
        count = 0

        for number_key, symbol in romans.items():
            count = int(num / number_key)
            if count >= 1:
                roman_numeral += symbol * count
            num = num % number_key

        return roman_numeral




num = 3749  # Expected Output "MMMDCCXLIX"
num = 1001
print(Solution().intToRoman(num))


# Ugly method
# def process_remainder(remainder: int) -> str:
#     roman_numral = ""
#     if remainder == 0:
#         return ""

#     value = ""
#     if remainder >= 500:
#         value += parse_five_hundred(remainder)
#     elif remainder >= 100:
#         value += parse_hundred(remainder)
#     elif remainder >= 50:
#         value += parse_fifty(remainder)
#     elif remainder >= 10:
#         value += parse_tens(remainder)
#     elif remainder > 0:
#         value += parse_single_digits(remainder)
#     return value

# def parse_single_digits(num: int) -> str:
#     if num >= 10:
#         return parse_tens(num)

#     if num == 0:
#         return ""

#     if num == 9:
#         return 'IX'
#     elif num == 8:
#         return 'VIII'
#     elif num == 7:
#         return 'VII'
#     elif num == 6:
#         return 'VI'
#     elif num == 5:
#         return 'V'
#     elif num == 4:
#         return 'IV'
#     elif num == 3:
#         return 'III'
#     elif num == 2:
#         return 'II'
#     else:
#         return 'I'

# def parse_tens(num: int) -> str:
#     if num >= 50:
#         return parse_fifty(num)

#     tens = ""
#     if num / 40 >= 1:
#         tens += 'XL'
#     else:
#         tens += 'X' * math.floor(num / 10)
#     tens += process_remainder(num % 10)
#     return tens

# def parse_fifty(num: int) -> str:
#     if num >= 100:
#         return parse_hundred(num)

#     fifty = ""
#     if num / 90 >= 1:
#         fifty += 'XC'
#         fifty += process_remainder(num % 90)
#     else:
#         fifty += "L"
#         fifty += process_remainder(num % 50)
#     return fifty

# def parse_hundred(num: int) -> str:  #400 (CD)
#     if num >= 500:
#         return parse_five_hundred(num)

#     hundred = ""
#     if num / 400 >= 1:
#         hundred += "CD"
#         hundred += process_remainder(num % 400)
#     else:
#         hundred += "C" * math.floor(num / 100)
#         hundred += process_remainder(num % 100)
#     return hundred

# def parse_five_hundred(num: int) -> str:  # 900 (CM)
#     if num >= 1000:
#         return parse_thousand(num)

#     five_hundred = ""
#     if num / 900 >= 1:
#         five_hundred += "CM"
#         five_hundred += process_remainder(num % 900)
#     else:
#         five_hundred += "D"
#         five_hundred += process_remainder(num % 500)
#     return five_hundred

# def parse_thousand(num: int) -> str: # M
#     thousand = ""
#     thousand += "M" * math.floor(num/1000)
#     thousand += process_remainder(num % 1000)
#     return thousand

# if num >= 1000:
#     roman_numeral += parse_thousand(num)

# elif num >= 500:
#     roman_numeral += parse_five_hundred(num)

# elif num >= 100:
#     roman_numeral += parse_hundred(num)

# elif num >= 50:
#     roman_numeral += parse_fifty(num)

# elif num >= 10:
#     roman_numeral += parse_tens(num)

# else:
#     roman_numeral += parse_single_digits(num)
# return roman_numeral
