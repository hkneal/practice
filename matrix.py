import math
import os
import random
import re
import sys

matrix = ['Tsi', 'h%x', 'i #', 'sM ', '$a ', '#t%', 'ir!']

def join_tuple_string(tups: tuple) -> str:
    return "".join(tups)


matrix = "".join(map(lambda *x: "".join(x), *matrix))
# matrix = zip(*matrix)  # Flatten the matrix
# matrix = "".join(map(join_tuple_string, matrix))
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
