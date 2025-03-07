def max_non_adjacent_sum(arr):

    include = arr[0]
    exclude = 0

    for i in range(1, len(arr)):
        new_include = exclude + arr[i]
        new_exclude = max(include, exclude)
        print(f"Before => i={i}, Include: {include}, New_Include: {new_include}, Exclude: {exclude}, New Exclude:{new_exclude}")
        include = new_include
        exclude = new_exclude
        print(f"After => i={i}, Include: {include}, New_Include: {new_include}, Exclude: {exclude}, New Exclude:{new_exclude}")

    return max(include, exclude)



# Example usage

array = [5, 1, 1, 5]

print(max_non_adjacent_sum(array))  # Output: 10