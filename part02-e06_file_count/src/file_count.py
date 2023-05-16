#!/usr/bin/env python3

import sys

def file_count(filename):
    lines = 0
    words = 0
    characters = 0
    f = open(filename, "r")
    for line in f.readlines():
        lines += 1
        splitted_line = line.split()
        words += len(splitted_line)
        characters += sum(len(word) for word in line)

    return (lines, words, characters)

def main():
    files = sys.argv[1:]
    for file in files:
        result = file_count(file)
        print(result)
    pass

if __name__ == "__main__":
    main()
