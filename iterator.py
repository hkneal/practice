import itertools
my_string = "Close"
sum = 0


# print([lambda x, sum: sum + ord(x) for x in my_string])
my_iterator = itertools.accumulate(itertools.cycle([ord(x) for x in "Close"]))

for i in range(100):
    print(next(my_iterator))