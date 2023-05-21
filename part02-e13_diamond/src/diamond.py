#!/usr/bin/env python3

import numpy as np

def diamond(n):
    dia = np.array([])
    print(np.eye(6, n+2, 2, dtype=int))
    return dia
def main():
    print(diamond(3))
    pass

if __name__ == "__main__":
    main()
