"""Using counter to keep track of string occurrences vs characters of a string"""

from collections import Counter


my_string_lst = ["bcdef",
                "abcdefg",
                "bcde",
                "bcdef"
                ]

str_counter = Counter(my_string_lst)

print(len(str_counter))
for i in str_counter.keys():
    print(str_counter[i], end=" ")