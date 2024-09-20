"""Practacting some more with sets"""

def average(array):
    # your code goes here
    array_set = set(array)
    return (sum(array_set) / len(array_set))


print(average([161, 182, 161, 154, 176, 170, 167, 171, 170, 174]))