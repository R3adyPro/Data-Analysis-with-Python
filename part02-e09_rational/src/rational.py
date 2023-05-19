#!/usr/bin/env python3

class Rational(object):
    def __init__(self, param1, param2):
        self.n = param1
        self.d = param2

    def __add__(self, second):
        new_n = (self.n * second.d) + (second.n * self.d)
        new_d = self.d * second.d
        return Rational(new_n, new_d)
    
    def __sub__(self, second):
        new_n = (self.n * second.d) - (second.n * self.d)
        new_d = self.d * second.d
        return Rational(new_n, new_d)
    
    def __mul__(self, second):
        new_n = self.n * second.n
        new_d = self.d * second.d
        return Rational(new_n, new_d)
    
    def __truediv__(self, second):
        new_n = self.n / second.n
        new_d = self.d / second.d
        return Rational(new_n, new_d)
    
    def __lt__(self, second):
        new_n = self.n / second.n
        new_d = self.d / second.d
        return new_n < new_d
    
    def __gt__(self, second):
        new_n = self.n / second.n
        new_d = self.d / second.d
        return new_n > new_d
    
    def __eq__(self, second):
        new_n = self.n / second.n
        new_d = self.d / second.d
        return new_n == new_d
    
    def __str__(self):
        return f"{self.n}/{self.d}"
    

def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1+r2)
    print(r1-r2)
    print(r1*r2)
    print(r1/r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()
