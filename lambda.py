lst = [30, 35, 67, 99, 102, 66, 45, 92]
print(lst)

# Lambda to only print even values
lst = list(filter(lambda x: x % 2 == 0, lst))
print(lst)

# reduce each value by one using list comprehension
lst = [x - 1 for x in lst]
print(lst)
