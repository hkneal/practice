from collections import Counter


def twoStrings(s1, s2):
    # Write your code here
    s1_con = Counter(s1)
    s2_con = Counter(s2)
    
    if len(s2) > len(s1):
        for letter in s1_con.elements():
            if letter in s2_con:
                return "YES"
    else:
        for letter in s2_con.elements():
            if letter in s1_con:
                return "YES"
    return "NO"

print(twoStrings("Hello", "World"))