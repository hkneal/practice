import math
from collections import Counter

def makeAnagram(a, b):
    a = Counter(a)
    b = Counter(b)

    a.subtract(b)

    return sum(map(abs, a.values()))

a = 'fcrxzwscanmligyxyvym'
b = 'jxwtrhvujlmrpdoqbisbwhmgpmeoke'

print(makeAnagram(a,b))
print("Hello" == "hello")
# for t in range(10, -1, -1):
#     print(t)

print(math.floor(7 / 2))
# def makeAnagram(a, b):
#     a = Counter(a)
#     b = Counter(b)
#     a.subtract(b)
#     return sum(map(abs, a.values()))

a = '3'
b = a
b = '2'
print(b, a)


a = 3
b = a
b = 2
print(b, a)

# object are reference addressible or pass by reference
a = {'count' : 3}
b = a
b['count'] = 2
print(b, a)