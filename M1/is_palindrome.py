""" Tests if a string is a palindrome """
s = "A man, a plan, a canal: Panama"

def is_palindrome(input_str: str) -> bool:
    clean_str = "".join(char.lower()for char in input_str if char.isalnum())
    print(clean_str, clean_str[::-1])
    return clean_str == clean_str[::-1]

print(is_palindrome(s))


