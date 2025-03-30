from collections import Counter
import time

class TimerContext:
  def __enter__(self):
    self.start_time = time.time()
    return self

  def __exit__(self, exc_type, exc_value, traceback):
    self.end_time = time.time()
    self.elapsed_time = self.end_time - self.start_time
    print(f"Total Elapsed Time: {self.elapsed_time} Seconds")


def get_odd(counter_dict) -> int: #index value
    for num, value in counter_dict.items():
        if value % 2 != 0:
            return num # This assumes only one odd value exsists
    return None


A = [9,3,9,3,9,7,9]
A_count = Counter(A)

with TimerContext():
#   print("Value returned is:", get_odd(A_count))


    my_dict = {'key1': 'val1', 'key2':'val2', 'key3':'val3'}
    values = [value for value in my_dict.values()]
    # values = list(my_dict.values())
    print(values)

# Dictionary unpacking
def detail(name, age):
    print(name, age)

d = {"name": "Alice", "age": 30}
detail(**d)
# Output: Alice 30

# Unpacking only Keys
d = {"a": 1, "b": 2, "c": 3}
print(*d)
# Output: a b c

# Quickly create a list of the keys
keys_list = [*d]
print(keys_list)
# Output: ['a', 'b', 'c']

# Tuple Unpacking
my_tuple = (1, 2, 3, 4, 5)
a, b, *rest = my_tuple

print(a) # Output: 1
print(b) # Output: 2
print(rest) # Output: [3, 4, 5]

ans = [f(2) for f in [lambda x: x * i for i in range(5)]]
print(ans)

ll = []
for i in range(5):
    print(f"In loop, i: {i}")
    def f(x):
        print(f'In f function, x: {x}, i: {i}')
        return x * i
    ll.append(f)
    print(ll)


print([f(2) for f in ll])

output = []
i = 0
for f in ll:
    output.append(f(2))
    i += 1
print(output)