#!/usr/bin/env python3

import sys
import statistics

def stddev (files):
    std = 0
    sample = []
    f = open(files, "r")
    for num in f.readlines():
        try:
            sample.append(float(num.strip()))
        except:
            continue
    std = statistics.stdev(sample)
    f.close()
    return std

def average(files):
    sum = 0
    avg = 0
    f = open(files, "r")
    for lenght, num in enumerate(f):
        try:
            sum += float(num.strip())
        except:
            continue
    avg = sum/(lenght+1)
    f.close()
    return avg

def sum(files):
    sum = 0
    f = open(files, "r")
    for num in f.readlines():
        try:
            sum += float(num.strip())
        except:
            continue
    f.close()
    return sum
    
def summary(filename):
    return (sum(filename), average(filename), stddev(filename))

def main():
    files = sys.argv[1:]
    for file in files:
        result = summary(file)
        print(f"File: {file} Sum: {result[0]:.6f} Average: {result[1]:.6f} Stddev: {result[2]:.6f}")
    pass

if __name__ == "__main__":
    main()
