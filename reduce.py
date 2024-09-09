import functools, operator
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def add(a: int, b: int) -> int:
    return a + b

evens = [x for x in numbers if x % 2 == 0]
print(evens)

### Preferred, most Pythonic method
sum = sum(numbers)
print(sum)

reduced = functools.reduce( lambda a, b: a + b, numbers)
print(reduced)

reduced = functools.reduce( operator.add, numbers)
print(reduced)

reduced = functools.reduce( add, numbers)
print(reduced)
