grid = [
          ["1","1","1","1","0"],
          ["1","1","0","1","0"],
          ["1","1","0","0","0"],
          ["0","0","0","0","1"],
          ["0","0","0","1","1"],
          ["0","0","1","1","1"],
          ["0","0","0","1","1"],
          ["0","1","0","0","0"],
          ["0","1","1","0","0"],
          ["0","1","0","0","0"],
          ["0","0","0","0","0"],
        ]

def getNumIslands(grid):
    
    my_sets = []
    for row_ind, row in enumerate(grid):
        for col_ind, col in enumerate(row):
            found_island = False
            if col == "1":
                if col_ind == 0 and row_ind == 0:
                    new_set = {str(row_ind) + '' + str(col_ind)}
                    print(f'Zero Set: {new_set}')
                    my_sets.append( new_set)
                    found_island = True
                    continue

                if col_ind > 0: # check previous in row
                    for island in my_sets:
                        if str(row_ind) + str(col_ind-1) in island:
                            island.add(str(row_ind) + '' + str(col_ind))
                            found_island = True
                            continue

                if row_ind > 0 and col_ind + 1 < len(row): # check previous row next column
                    if row[col_ind + 1] == "1":
                        if str(row_ind - 1) + str(col_ind + 1) in island:
                                island.add(str(row_ind) + '' + str(col_ind))
                                found_island = True
                                continue

                if row_ind > 0:
                    for island in my_sets:
                        if str(row_ind - 1) + str(col_ind) in island:
                            island.add(str(row_ind) + '' + str(col_ind))
                            found_island = True
                            continue

                if not found_island:
                    new_set = {str(row_ind) + '' + str(col_ind)}
                    print(new_set)
                    my_sets.append( new_set)
    print(my_sets)
    return len(my_sets)


print(f'Number of Islands: {getNumIslands(grid)}')
