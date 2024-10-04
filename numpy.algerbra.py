"""Common Numpy Algerbra functions"""

"""
linalg.det

The linalg.det tool computes the determinant of an array.

print numpy.linalg.det([[1 , 2], [2, 1]])       #Output : -3.0
"""

import numpy

if __name__ == "__main__":
    n = int(input().rstrip())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(float, list(input().split()))))
    print(round(numpy.linalg.det(matrix), 2))

"""
mean

The mean tool computes the arithmetic mean along the specified axis.

import numpy

my_array = numpy.array([ [1, 2], [3, 4] ])

print numpy.mean(my_array, axis = 0)        #Output : [ 2.  3.]
print numpy.mean(my_array, axis = 1)        #Output : [ 1.5  3.5]
print numpy.mean(my_array, axis = None)     #Output : 2.5
print numpy.mean(my_array)                  #Output : 2.5
By default, the axis is None. Therefore, it computes the mean of the flattened array.

var

The var tool computes the arithmetic variance along the specified axis.

import numpy

my_array = numpy.array([ [1, 2], [3, 4] ])

print numpy.var(my_array, axis = 0)         #Output : [ 1.  1.]
print numpy.var(my_array, axis = 1)         #Output : [ 0.25  0.25]
print numpy.var(my_array, axis = None)      #Output : 1.25
print numpy.var(my_array)                   #Output : 1.25
By default, the axis is None. Therefore, it computes the variance of the flattened array.

std

The std tool computes the arithmetic standard deviation along the specified axis.

import numpy

my_array = numpy.array([ [1, 2], [3, 4] ])

print numpy.std(my_array, axis = 0)         #Output : [ 1.  1.]
print numpy.std(my_array, axis = 1)         #Output : [ 0.5  0.5]
print numpy.std(my_array, axis = None)      #Output : 1.11803398875
print numpy.std(my_array)                   #Output : 1.11803398875
By default, the axis is None. Therefore, it computes the standard deviation of the flattened array.

"""

print(numpy.mean(matrix, axis=1))
print(numpy.var(matrix, axis=0))
print(round(numpy.std(matrix), 11))

"""
dot

The dot tool returns the dot product of two arrays.

import numpy

A = numpy.array([ 1, 2 ])
B = numpy.array([ 3, 4 ])

print numpy.dot(A, B)       #Output : 11
cross

The cross tool returns the cross product of two arrays.

import numpy

A = numpy.array([ 1, 2 ])
B = numpy.array([ 3, 4 ])

print numpy.cross(A, B)     #Output : -2
"""

# print(reduce(np.dot, matrix))