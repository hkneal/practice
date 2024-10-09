"""The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);


Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
"""

s = "PAYPALISHIRING"
numRows = 3

def convert(s: str, numRows: int) -> str:
    string_lst = iter(list(s))
    new_string = ""
    n = (len(s)//2)
    matrix = []
    diag = numRows -1

    rows = numRows
    cols = n
    matrix = []

    for i in range(rows):
        row = []  # Create a new row
        for j in range(cols):
            row.append('')  # Append a value to the row
        matrix.append(row)  # Append the row to the matrix

    print(matrix)

    for i in range(n):
        for j in range(numRows):
            if i %2 == 0 and i > 0:
                pass
                # Use Diag
            else:
                matrix[i][j] = ([next(string_lst)])
                print(i,j)
        for row in matrix:
            print(row)
        break

    return new_string

print(convert(s, numRows))

