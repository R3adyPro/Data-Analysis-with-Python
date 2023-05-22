#!/usr/bin/env python3

import numpy as np
import scipy.linalg
import statistics
#import scipy.linalg


def vector_lengths(a):
    b = np.square(a)
    c = np.sum(b, axis=1)
    
    return np.sqrt(c)

def main():    
    np.random.seed(0)
    a=np.random.randint(0,10, (4,2))
    print(vector_lengths(a))
    pass

if __name__ == "__main__":
    main()
