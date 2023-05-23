#!/usr/bin/env python3

import numpy as np

def first_half_second_half(a):
    half = a.shape[1]//2
    bigger = np.sum(a[:, :half], axis=1) > np.sum(a[:len(a), half:],axis=1)
    return a[bigger]

def main():
    a = np.array([[1, 3, 4, 2],
              [2, 2, 1, 2],
              [2, 2, 4, 2],
              [2, 3, 4, 8],
              [1, 9, 1, 2]])
    print(first_half_second_half(a))
    pass

if __name__ == "__main__":
    main()
