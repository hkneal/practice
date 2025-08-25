"""Is a palindrome"""
l = "123454321"

def is_pal(s: str) -> bool:
    return s[::-1] == s


print(is_pal(l))