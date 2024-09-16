def hourglassSum(arr):  
   # Write your code here
   max = arr[0][0] + arr[0][1] + arr[0][2] + arr[1][1] + arr[2][0] + arr[2][1] + arr[2][2]
   for i in range(len(arr)-2):
       for j in range(4):
           top_row = arr[i][j] + arr[i][j+1] + arr[i][j+2]
           mid_i = arr[i+1][j+1]
           bottom = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
           if top_row + mid_i + bottom > max:
               max = top_row + mid_i + bottom
   return max
    
if __name__ == '__main__':
    arr = []

    # for _ in range(6):
    #     arr.append(list(map(int, input().rstrip().split())))

    arr = [[-1, -1, 0, -9, -2, -2], 
           [-2, -1, -6, -8, -2, -5], 
           [-1, -1, -1, -2, -3, -4], 
           [-1, -9, -2, -4, -4, -5], 
           [-7, -3, -3, -2, -9, -9], 
           [-1, -3, -1, -2, -4, -5]]

    result = hourglassSum(arr)
    print(result)