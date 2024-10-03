import math
import os
import random
import re
import sys

matrix = ["T%Mic&", "h%axr%", "iit#p!", "ssrst&"]

matrix = zip(*matrix)  # Flatten the matrix
matrix = "".join(["".join(x) for x in matrix])
print(matrix)
matrix = re.sub(r"([\w]\s?)[!@#$%&]+(\s?[\w])", r"\1 \2", matrix)
print(matrix)

# Passes
# for _ in range(n):
#     matrix_item = input()
#     matrix.append(matrix_item)
# matrix = zip(*matrix)
# matrix = "".join(["".join(x) for x in list(matrix)])
# matrix = re.sub(r"([\w]\s?)[!@#$%&]+(\s?[\w])", r"\1 \2", matrix)
# print(matrix)


"""
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

matrix = zip(*matrix)
matrix = "".join(["".join(x) for x in list(matrix)])
matrix = re.sub(r"([a-zA-Z0-9])[!@#$%&]([a-zA-Z0-9])", r"\1 \2", matrix)
matrix = re.sub(r"([a-zA-Z0-9]\s)[!@#$%&]([a-zA-Z0-9])", r"\1 \2", matrix)
matrix = re.sub(r"([a-zA-Z0-9])[!@#$%&][!@#$%&]([a-zA-Z0-9])", r"\1 \2", matrix)
matrix = re.sub(r"([a-zA-Z0-9])[!@#$%&][!@#$%&][!@#$%&]([a-zA-Z0-9])", r"\1 \2", matrix)
matrix = re.sub(r"([a-zA-Z0-9])[!@#$%&](\s[a-zA-Z0-9])", r"\1 \2", matrix)
print(matrix)
"""
