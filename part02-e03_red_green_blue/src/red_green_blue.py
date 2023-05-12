#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    f = open(filename, "r")
    cleaned_list = []
    for i, line in enumerate(f):
        print(line)
        if i == 0:
            continue
        else:
            sorted_line = re.search(r"(\S+)\s+(\S+)\s+(\S+)\s+([a-zA-Z_ ]+)", line)
            cleaned_line = "\t".join(sorted_line.groups())
            cleaned_list.append(cleaned_line)
    
    f.close()
    return cleaned_list 


def main():
    print(red_green_blue())
    pass

if __name__ == "__main__":
    main()
