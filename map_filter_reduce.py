"""Practicing the Map, Reduce, Filter functions"""

from functools import reduce

my_list = list(range(10))
print(my_list)
#>>>[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Map applies a function to every value in the iterable.
my_list = list(map(lambda x: x*x, my_list))
print(my_list)
#>>>[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Filter returns filter object of values that returned true from given test function (test function only returns true/false)
my_list = list(filter(lambda x: x > 10 and x < 80, my_list))
print(my_list)
#>>>[16, 25, 36, 49, 64]

# Reduce applies a function to every value in an iterable to reduce the iterable to one value
my_list = reduce(lambda x, y: x + y, my_list)
print(my_list)
#>>>190