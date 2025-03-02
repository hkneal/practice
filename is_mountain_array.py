from typing import List
def is_mountain_array(arr: List[any]) -> bool:

    if len(arr) < 3:
        return False

    i = 1
    while( i< len(arr) and arr[i-1] < arr[i]):
        i += 1

    if i == 1 or i == len(arr):
        return False

    while (i < len(arr) and arr[i-1] > arr[i]):
        i += 1
    return i == len(arr)


print(is_mountain_array([1,2,3,5,3,2,1]))