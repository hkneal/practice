import numpy as np

def weakest_strong_link(strength):
    num_of_rows = len(strength)
    num_of_columns = len(strength[0])

    weakest_by_row = {}

    for row in range(num_of_rows):
        weakest = min(strength[row])
        weakest_ind = strength[row].index(weakest)
        weakest_by_row[row] = (weakest, weakest_ind)
    # print(weakest_by_row)


    strongest_by_column = {}
    for column in range(num_of_columns):
        strongest = 0
        for row in range(num_of_rows):
            temp = strength[row][column]
            # print(f"Temp: {temp}")
            if temp > strongest:
                strongest = temp
                strongest_ind = column
                strongest_by_column[column] = (strongest, strongest_ind)
    # print(strongest_by_column)

    weakest_by_row_values = weakest_by_row.values()
    strongest_by_column_values = strongest_by_column.values()
    for tup in weakest_by_row_values:
        if tup in strongest_by_column_values:
            return tup[0]

    return -1

def weakest_strong_link_with_numpy(strength):
    num_of_rows = len(strength)
    num_of_columns = len(strength[0])

    weakest_by_row = {}

    for row in range(num_of_rows):
        weakest = min(strength[row])
        weakest_ind = strength[row].index(weakest)
        weakest_by_row[row] = (weakest, weakest_ind)
    # print(weakest_by_row)

    np_matrix = np.array(strength)
    strongest_by_column = {}
    for column in range(num_of_columns):
        strongest = 0

        column_max = np.max(np_matrix[:,column])
        if column_max > strongest:
            strongest = column_max
            strongest_ind = column
            strongest_by_column[column] = (strongest, strongest_ind)
    # print(strongest_by_column)

    weakest_by_row_values = weakest_by_row.values()
    strongest_by_column_values = strongest_by_column.values()
    for tup in weakest_by_row_values:
        if tup in strongest_by_column_values:
            return tup[0]

    return -1

strength=[[1, 2, 3],[4, 5, 6],[7, 8, 9]]
strength = [[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]
print(weakest_strong_link(strength))
print(weakest_strong_link_with_numpy(strength))