"""Practicing converting complex numbers into polar form"""

import cmath

line = input()
complex_num = (complex(line))

print(abs(complex_num))
print(cmath.phase(complex_num))