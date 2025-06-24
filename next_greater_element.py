def next_greater_element(arr):
    stack =  []
    response = [-1] * len(arr)

    for i in range(len(arr)):

        while stack and arr[i] > arr[stack[-1]]:
            response[stack.pop()] = arr[i]

        stack.append(i)

    return response




arr = [1,4,6,3,2,7]
print(next_greater_element(arr))