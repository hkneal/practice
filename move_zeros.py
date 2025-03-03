from typing import List
import timeit


arr = [0,0,1]

def move_zeros(arr: List[int]) -> list:
    i = 0

    for num in arr:
        if num is not 0:
            arr[i] = num
            i +=1

    for j in range(i, len(arr)):
        arr[j] = 0

    return arr

start = timeit.default_timer()
print(move_zeros(arr))
time_taken = (timeit.default_timer() - start) * 1000
print(f"Time taken: {time_taken} seconds")
