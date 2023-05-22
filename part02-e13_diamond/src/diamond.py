#!/usr/bin/env python3

import numpy as np

def diamond(n):
    a = np.eye(n, dtype=int)
    b = a[::-1]
    c = b.T[:n-1].T
    d = np.concatenate((c, a), axis=1)
    e = d[::-1]
    f = e[1:]
    full = np.concatenate((d,f))
    return full
def main():
    print(diamond(10))
    pass

if __name__ == "__main__":
    main()
