#!/usr/bin/env python3

import numpy as np

def get_rows(a):
    rows = []
    for row in a:
        rows.append(row)
    return rows

def get_columns(a):
    columns = []
    b = a.T
    for row in b:
        columns.append(row)
    return columns

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Rows:", get_rows(a))
    print("Columns:", get_columns(a))

if __name__ == "__main__":
    main()
