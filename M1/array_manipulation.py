def arrayManipulation(n, queries):
    # Write your code here
    arr = [0]*n
    # print(arr)
    for row in range(len(queries)):
        operation_value = queries[row][-1]
        start = queries[row][0] - 1
        end = queries[row][1]

        # print('Start value is {}, end value is {}'.format(start, end))

        for col in range(start, end):
            arr[col] = arr[col] + operation_value
            # print(arr)

    return max(arr)
    
n = 10
queries = [[1,5,3], [4,8,7], [6,9,1]]
result = arrayManipulation(n, queries)
print(result)