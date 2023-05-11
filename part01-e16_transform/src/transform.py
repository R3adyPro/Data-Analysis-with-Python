#!/usr/bin/env python3

def transform(s1, s2):
    L1 = list(map(int, s1.split()))
    L2 = list(map(int, s2.split()))
    L3 = []
    for x, y in zip(L1, L2):
        L3.append(x*y)
    return L3

def main():
    print(transform("1 5 3", "2 6 -1"))
    pass

if __name__ == "__main__":
    main()
