def gridChallenge(grid):
    # Write your code here
    num_of_columns = len(grid[0])

    for indx, str in enumerate(grid):
        grid[indx] = sorted(str)

    for row in grid:
        print(row)

    for i in range(num_of_columns):
        column_num = i
        row_num = 0
        while row_num < num_of_columns -1:
            print(f"Row Num: {row_num}, column_num: {column_num}, Number of columns: {num_of_columns}")
            print(f"Testing {grid[row_num][column_num]} and {grid[row_num+1][column_num]}")
            if grid[row_num][column_num] > grid[row_num+1][column_num]:
                print(f"False at: row {row_num}, column {column_num}")
                return False
            else:
                row_num += 1
    return True





grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
grid = ['abc', 'hjk', 'mpq', 'rtv']
print(gridChallenge(grid))