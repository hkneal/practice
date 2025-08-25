""" Traverse a matrix in a zig zag pattern"""


# Knowing if you should increment or decrement during loop
# Ensure you are not hitting values you have already hit, - start and stop values for the loop


# Variables to be used in the loop to gate direction and start/stop
# Toggle direction flag when you hit stop
from enum import Enum
class Direction(Enum):
    RIGHT = "r"
    LEFT = "l"
    UP = "u"
    DOWN = "d"


matrix = [
    [0,1,2],
    [1,2,3],
    [2,3,4]
]

direction = Direction.RIGHT
operation = False # False = increment, True = decrement
row_ind = 0
column_ind = 0
stop_value = 0
counter = 0
# (N * 2) + 1)

while counter < (len(matrix) * len(matrix[0])):

    match direction
        stop_value

    counter += 1
