def index_sort(arr):

    arr2 = sorted(arr)
    mapa = {}
    for j in range(len(arr2)):
        mapa[arr2[j]] = j
    print(mapa)
    i = 0
    swap = 0
    while i < len(arr):
        print(f'Original Array {arr}, Arr2[i] {arr2[i]}, Arr[i] {arr[i]}')
        if arr2[i] != arr[i]:
            k = mapa[arr[i]]
            print(f'K {k}')
            arr[i], arr[k] = arr[k], arr[i]
            swap += 1
            print('Swapped!', arr)
        else:
            i += 1
    print(swap)

# Driver code to test above
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]

    index_sort(arr)

    print("Sorted array:")
    # for i in range(len(arr)):
    print(" ".join([str(x) for x in arr]))