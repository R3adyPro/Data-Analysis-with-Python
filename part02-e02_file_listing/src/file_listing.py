#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
    f = open(filename, "r")
    new_list = []
    for i in range(1,48):
        line = f.readline()
        sorted_line = re.search(r"\s+(\d+)\s+([a-zA-Z]{3})\s+(\d{1,2})\s+(\d{2}):(\d{2})\s+(.*)", line)

        size = int(sorted_line.group(1))
        month = sorted_line.group(2)
        day = int(sorted_line.group(3))
        hour = int(sorted_line.group(4))
        min = int(sorted_line.group(5))
        file_name = sorted_line.group(6)
        correct_format = (size, month, day, hour, min, file_name)

        new_list.append(correct_format)

    return new_list

def main():
    print(file_listing())
    pass

if __name__ == "__main__":
    main()
