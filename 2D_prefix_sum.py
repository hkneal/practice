"""Using prefix sum to solve 2d range sum"""
from typing import List



class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
       ROWS, COLS = len(matrix), len(matrix[0])
       self.prefixMatix = [[0] * (COLS + 1) for row in range(ROWS + 1)]

       for row in range(ROWS):
           prefix = 0
           for col in range(COLS):
               print(row, col)
               prefix += matrix[row][col]
               above = self.prefixMatix[row][col + 1]
               self.prefixMatix[row +1][col + 1] = prefix + above

    def __repr__(self):
        str_matrix = "".join([str(x) for x in [y for y in matrix]])
        return str_matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, row2 = row1 + 1, row2 + 1
        col1, col2 = col1 + 1, col2 + 1

        bottomRight = self.prefixMatix[row2][col2]
        above = self.prefixMatix[row1 - 1][col2]
        left = self.prefixMatix[row2][col1 -1]
        topLeft = self.prefixMatix[row1 - 1][col1 -1]
        return bottomRight - above - left + topLeft


matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
matrix = [[[-4,-5]]]
numMatrix = NumMatrix(matrix)
print(numMatrix.prefixMatix)
# print(numMatrix.sumRegion(2,1,4,3))
print(numMatrix.sumRegion(0,0,0,1))

