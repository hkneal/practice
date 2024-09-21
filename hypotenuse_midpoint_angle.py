"""Returns the angle of the hypotenuse midpoint at the right angle"""
import math
AB = int(input())
BC = int(input())

print(round(math.degrees((math.atan(AB / BC)))), chr(176),sep="")