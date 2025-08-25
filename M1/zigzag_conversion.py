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

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        num_rows = numRows
        num_columns = len(s)//2
        matrix = [['' for _ in range(num_columns)] for _ in range(num_rows)]
            
        j = 0
        i = 0
        diag = False
        for c in s:
            matrix[i][j] = c
            
            if i == numRows - 1:
                i = i - 1
                j += 1
                diag = True

            elif diag:
                i = i - 1
                j += 1
                if i == 0:
                    diag = False

            elif i > 0 and j > 0 and (i > j or i == j):
                i -= 1
                j += 1

            else:
                i +=1
        prnt_str = ""
        for i in range(num_rows):
            print(matrix[i])
            prnt_str += "".join(matrix[i])
        print(prnt_str)

test = Solution().convert(s, numRows)