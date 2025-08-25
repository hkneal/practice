"""Return the largest substring that is a palindrome"""
import itertools

x = "hellosannasmith"


def get_largest_pali(s: str) -> str:

    combos = list(reversed([''.join(l) for i in range(len(x)) for l in itertools.combinations(x, i+1)]))
    
    for word in combos:
        if word == word[::-1]:
            return word
            
    return "None"


print(get_largest_pali(x))