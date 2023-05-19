#!/usr/bin/env python3
import sys

def file_extensions(filename):
    empty = []
    file_list = {}
    f = open(filename, "r")
    for line in f.readlines():
        splitted = line.strip().split(".")
        if len(splitted) > 1:
            file_list.setdefault(splitted[len(splitted)-1], [])
            file_list[splitted[len(splitted)-1]].append(line.strip())
        else:
            empty.append(line.strip())
    f.close()
    return (empty, file_list)

def main():
    result = file_extensions('src/filenames.txt')
    print(f"{len(result[0])} files with no extension")
    for key, value in result[1].items():
        print(key, len(value))
    pass

if __name__ == "__main__":
    main()
