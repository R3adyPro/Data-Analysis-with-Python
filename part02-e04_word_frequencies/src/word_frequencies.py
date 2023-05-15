#!/usr/bin/env python3'

import re

def word_frequencies(filename="src/alice.txt"):
    f = open(filename, "r")
    d = {}

    for i, line in enumerate(f):
        splitted = line.split()
        for word in splitted:
            count = d.get(word.strip("""!"#$%&'()*,-./:;?@[]_"""), 0)
            d[word.strip("""!"#$%&'()*,-./:;?@[]_""")] = count +1
        
    return d

def main():
    print(word_frequencies())
    pass

if __name__ == "__main__":
    main()
