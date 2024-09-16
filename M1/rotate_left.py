def rotLeft(arr, num_rotations):
    # Write your conum_rotationse here
    # Create a subset of the original array which is the length of the number of rotations
    # contact the remaining to this new array
    
    temp_array = [arr[i] for i in range(num_rotations)]
    print(f'Original Array: {arr}')
    print(f'Temporary Array: {temp_array}')
    
    beg_array = [arr[len(temp_array) + i] for i in range(len(arr) - num_rotations)]
           
    return beg_array + temp_array

print(rotLeft([3,4,6,5,7,9,8,1], 1))