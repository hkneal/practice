arr = [1,2,3,4,5,6,7]
arr = [-2,0,3,-5,2,-1]

def find_sum_at_indicies(i: int, j: int) -> int:
# Returns the sum of values in the range i - j

    # create a prefix list
    p = [None] * len(arr)
    p[0] = arr[0]
    for k in range(1, len(arr)):
        p[k] = arr[k] + p[k-1]
    print(p)

    if i is 0:
        return p[j]
    return p[j] - p[i-1]


def find_sum_inplace(i: int, j: int) -> int:
    # Get prefix inplace
    for k in range(1, len(arr)):
        arr[k] += arr[k-1]
    if i == 0:
        return arr[j]
    return arr[j] - arr[i-1]


print(find_sum_at_indicies(0,2))
print(find_sum_inplace(0,2))

