#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):
    plus = (-b + math.sqrt((b**2)- 4 * a * c)) / (2 * a)
    minus = (-b - math.sqrt((b**2)- 4 * a * c)) / (2 * a)
    return plus, minus

def main():
    print(solve_quadratic(1, -3, 2))

if __name__ == "__main__":
    main()
