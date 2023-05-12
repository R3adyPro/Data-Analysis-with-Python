# Enter you module contents here
__doc__ = "triangle calculations"

from math import sqrt

__author__ = "Tatu Miinalainen"
__version__ = "1.0"

def hypotenuse(a, b):
    '''Calculates triangles hypetenuse'''
    return sqrt(a**2 + b**2)

def area(a, b):
    '''Calculates triangles area'''
    return (a/2)*b
