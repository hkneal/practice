"""Practice with complex numbers and python"""
import math, copy

class Complex(object):
    def _get_data(self, no):
        new_complex = copy.deepcopy(self)
        x1 = new_complex.real
        x2 = no.real
        y1 = new_complex.imaginary
        y2 = no.imaginary
        return new_complex, x1, x2, y1, y2
    
    def __pow__(self, no):
        no.real *= no.real
        no.imaginary *= no.imaginary
        return no

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        new_complex = copy.deepcopy(self)
        new_complex.real += no.real
        new_complex.imaginary += no.imaginary
        return new_complex
     
    def __sub__(self, no):
        new_complex = copy.deepcopy(self)
        new_complex.real -= no.real
        new_complex.imaginary -= no.imaginary
        return new_complex
        
    def __mul__(self, no):
        new_complex, x1, x2, y1, y2 = self._get_data(no)
        new_complex.real = (x1*x2) - (y1*y2)
        new_complex.imaginary = (x1*y2) + (x2*y1) 
        return new_complex
    
    def __truediv__(self, no):
        new_complex, x1, x2, y1, y2 = self._get_data(no)
        new_no = copy.deepcopy(no)
        no_pow = self.__pow__(new_no)
        new_complex.real = ((x1 * x2) + (y1 * y2)) / (no_pow.real + no_pow.imaginary)
        new_complex.imaginary = ((y1 * x2) - (x1 * y2)) /(no_pow.real + no_pow.imaginary)
        return new_complex

    def mod(self):
        new_complex = copy.deepcopy(self)
        no_pow = self.__pow__(new_complex)
        new_complex = Complex(math.sqrt(no_pow.real + no_pow.imaginary), 0)
        return new_complex

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
