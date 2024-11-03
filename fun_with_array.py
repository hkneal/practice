"""Practice with Arrays"""

from array import array

my_arr = array("i", [1,2,3,4,5,6,7])

print(my_arr)
for i in my_arr:
    print(i)

my_arr.pop(3)
print(my_arr)