def remove_duplicates_of_size_k(s: str, k: int) -> str:
    """
    Removes consecutive duplicate substrings of size k from a string.

    Args:
        s: The input string.
        k: The size of the consecutive duplicate substring to remove.

    Returns:
        The string after removing the specified duplicates.
    """
    if k <= 0:
        return s

    stack = []  # Stores (character, count) pairs

    for char in s:
        if stack and stack[-1][0] == char:
            stack[-1][1] += 1  # Increment count if character matches top of stack
        else:
            stack.append([char, 1])  # Add new character with count 1

        if stack[-1][1] == k:
            stack.pop()  # Remove if count reaches k

    result = []
    for char, count in stack:
        result.append(char * count)  # Reconstruct string from remaining characters

    return "".join(result)

s = "deeedbbcccbdaa"
k = 3
print(remove_duplicates_of_size_k(s, k))

# 1209. Remove All Adjacent Duplicates in String II