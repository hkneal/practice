"""
Get all possible combinations of substrings from string
"""
import itertools
from itertools import combinations
x = '0100'
print(list(itertools.combinations(x)))
lst =[''.join(l) for i in range(len(x)) for l in itertools.combinations(x, 2)]

prodct = list(itertools.product(list(x)))

print(lst)

print(prodct)
# itertools.combinations_with_replacement

#If you want it in the reversed order, you can make the range function return its sequence in reversed order

lst = [''.join(l) for i in range(len(x),0,-1) for l in combinations(x, i)]
# print(lst)

### Get the longest
"""
    for i in range(len(s) -1):
        for j in range(i+1, len(s)):
            if s[i:j+1] == s[i:j+1][::-1]:
                if len(s[i:j+1]) > longest:
                    longest = len(s[i:j+1])
                    lngst_word = s[i:j+1]

"""

age = 20
if not age < 18:
    print("You are an adult") # Output: You are an adult