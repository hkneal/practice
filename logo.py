"""Find three most common chars in a string sort by count then letter"""

s = "qwertyuiopasdfghjklzxcvbnm"

from collections import Counter



if __name__ == '__main__':
    counter_s = Counter(s)
    counter_s = sorted(counter_s.items(), key=lambda x: (-x[1], x[0]))[:3]
    for c in counter_s:
        print("{} {}".format(c[0], c[1]))