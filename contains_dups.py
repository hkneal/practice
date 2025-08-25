def contains_duplicate(input)-> bool:
    if len(input) == len(set(input)):
        return False
    return True

input = [1,3,5,7,1]
input = [1,3,5,7]
print(contains_duplicate(input))