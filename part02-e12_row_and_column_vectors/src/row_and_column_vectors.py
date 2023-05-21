#!/usr/bin/env python3

import numpy as np

def get_row_vectors(a):
    rows = []
    parts=np.split(a, len(a))
    for r in parts:
        rows.append(r)
    return rows

def get_column_vectors(a):
    column = []
    parts = a.T
    shape = parts.shape
    new = shape[1]
    for i, p in enumerate(parts):
        column.append(np.array(p.reshape(new, 1)))
    return column

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Row vectors:", get_row_vectors(a))
    print("Column vectors:", get_column_vectors(a))

if __name__ == "__main__":
    main()
