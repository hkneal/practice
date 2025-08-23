input_matrix = [
    [42, 7, 13, 99],
    [6, 42, 7, 13],
    [1, 6, 42, 7]
]
# input_matrix = [[8, 23], [69, 1]]

def same_stripes(matrix) -> bool:
    num_of_rows = len(matrix)
    num_of_columns = len(matrix[0])
    if num_of_rows <= 1:
        return True

    for row in range(num_of_rows):

        for column in range(num_of_columns):
            if row + 1 < num_of_rows and column + 1 < num_of_columns:
                if matrix[row + 1][column + 1] != matrix[row][column]:
                    return False

    return True


print(same_stripes(input_matrix))