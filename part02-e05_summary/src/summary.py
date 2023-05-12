#!/usr/bin/env python3

import sys

def tes(file):
    f = open(file, "r")
    sum = 0
    num = []
    for i, line in enumerate(f):
        num = int(line)
        print(num)
    return sum
    
def summary(filename="src/example.txt", filename2="src/example2.txt", filename3="src/example3.txt"):

    return (f"File: {filename} Sum: {tes(filename)}")

def main():
    print(summary())
    pass

if __name__ == "__main__":
    main()
