"""
Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.
"""

VOWELS = ["A", "E", "I", "O", "U"]

def get_count_stuart(string: str) -> int:
    """Stuarts substrings must start with a constant

    Args:
        string (str): lead string in which Stuart can make substrings

    Returns:
        int: The count of the total number of substrings Start can make
    """
    count = 0
    for i in range(len(string)):

        if string[i] not in VOWELS:
            print("Increasing count for: {}".format(string[i]))
            # count +=1

            count = count + (len(string) - i)
            # for j in range(i+1, len(string)):
            #     print("Increasing count for substring: {}".format(string[i:j+1]))
            #     count +=1

    return count

def get_count_kevin(string: str) -> int:
    """Stuarts substrings must start with a constant

    Args:
        string (str): lead string in which Stuart can make substrings

    Returns:
        int: The count of the total number of substrings Start can make
    """
    count = 0
    for i in range(len(string)):

        if string[i] in VOWELS:
            print("Increasing count for: {}".format(string[i]))
            # count +=1

            count = count + (len(string) - i)
            # for j in range(i+1, len(string)):
            #     print("Increasing count for substring: {}".format(string[i:j+1]))
            #     count +=1

    return count

def minion_game(string: str) -> tuple:
    stuart_count = (get_count_stuart(string))
    kevin_count = (get_count_kevin(string))
    print(kevin_count)
    return ("Stuart " + str(stuart_count)) if stuart_count > kevin_count else "Draw" if stuart_count == kevin_count else ("Kevin " + str(kevin_count))

print(minion_game("BANANA"))
