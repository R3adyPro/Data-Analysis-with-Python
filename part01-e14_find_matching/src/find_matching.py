#!/usr/bin/env python3

def find_matching(L, pattern):
    l = []
    for i, x in enumerate(L):
        if pattern in L[i]:
            l.append(i)
    return [l][0]

def main():
    print(find_matching(["sensitive", "engine", "rubbish", "comment"], "en"))
    pass

if __name__ == "__main__":
    main()
