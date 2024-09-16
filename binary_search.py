"""
    Coding practice with binary search
"""
from typing import List

# Recursive vcersion

def find_target_index(arr: List, low: int, high: int, target: int) -> tuple:
    mid = (low + high) // 2

    if low > high:
        print(f"Searched all!")
        return False, None

    if arr[mid] == target:
        return True, mid

    if len(arr[low:high]) < 1:
        return False, None

    elif target > arr[mid]:
        return find_target_index(arr, mid +1, high, target)

    else:
        return find_target_index(arr, low, mid -1, target)



arr = sorted(list(set([4,56,7,23,1,4,90, 322, 65, 7, 1, 2])))
print(find_target_index(arr, 0, len(arr) -1, 6))



# Iterative approach

def get_index(arr: List, target: int) -> tuple:

    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (low + high) // 2

        if target > arr[mid]:
            low = mid + 1

        elif target < arr[mid]:
            high = mid - 1

        else:
            return True, mid

    return False, None

print(get_index(arr, 90))

