#!/usr/bin/env python3

import numpy as np
import scipy.linalg

def vector_angles(X, Y):
    ##np.cos(x_square*y_square),
    x_norm = np.sqrt(np.sum(np.square(X)))
    y_norm = np.sqrt(np.sum(np.square(Y)))

    angle = np.arccos(np.sum((np.multiply(X, Y)))/(np.multiply(x_norm, y_norm)))
    result = angle * 180 / np.pi
    return  np.array(result)

def main():
    np.random.seed(0)
    x = np.array([[0,1,0], [1,1,0]])
    y = np.array([[0,0,1], [-1,1,0]])   
    print(vector_angles(x,y))

if __name__ == "__main__":
    main()
