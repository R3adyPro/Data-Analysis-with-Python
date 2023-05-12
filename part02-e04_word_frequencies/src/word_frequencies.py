#!/usr/bin/env python3'

import re

def word_frequencies(filename="src/alice.txt"):
    f = open(filename, "r")
    read = f.read().lower()
    d = {}
    match = re.findall(r'\b[a-z]+\b', read)
    for word in match:
        count = d.get(word, 0)
        d[word] = count +1
        
    return d

def main():
    print(word_frequencies())
    pass

if __name__ == "__main__":
    main()
