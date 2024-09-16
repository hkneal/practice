def bubbleSort(arr):

    arr2 = sorted(arr)
    mapa = {}
    for j in range(len(arr2)):
        mapa[arr2[j]] = j
    print(mapa)
    i = 0
    swap = 0
    while i < len(arr):
        if arr2[i] != arr[i]:
            k = mapa[arr[i]]
            arr[i], arr[k] = arr[k], arr[i]
            swap += 1
        else:
            i += 1
    print(swap)

    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        swapped = False
        # print(n-i-1)

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break

# Driver code to test above
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]

    bubbleSort(arr)

    print("Sorted array:")
    # for i in range(len(arr)):
    print(" ".join([str(x) for x in arr]))