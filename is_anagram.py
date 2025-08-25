def is_anagram(s, t):
    if len(s) != len(t):
        return False

    if set(s) == set(t):
        return True
    return False

s = "listen"
t = "silent"
s = "lemur"
t = "lemer"
print(is_anagram(s, t))