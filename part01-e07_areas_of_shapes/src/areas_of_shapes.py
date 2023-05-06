#!/usr/bin/env python3

import math

def triangle(base, height):
    return int(base) * int(height) / 2

def rectangle(width, height):
    return int(width) * int(height)

def circle(radius):
    return 3.14159265359 * float(radius) * float(radius)

def main():
    while True:
        shape = input("Choose a shape (triangle, rectangle, circle): ").lower()
        if shape == "triangle":
            base = input("Give base of the triangle: ")
            height = input("Give height of the triangle: ")
            print(f"The area is {triangle(base, height):6f}")
        elif shape == "rectangle":
            width = input("Give base of the rectangle: ")
            height = input("Give height of the rectangle: ")
            print(f"The area is {rectangle(width, height):6f}")
        elif shape == "circle":
            radius = input("Give radius of the circle: ")
            print(f"The area is {circle(radius):6f}")
        elif len(shape) == 0:
            break
        else:
            print("Unknown shape!")

if __name__ == "__main__":
    main()
