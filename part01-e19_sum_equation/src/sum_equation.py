#!/usr/bin/env python3

def sum_equation(L):
    if len(L) == 0:
        L.append(0)
    summ = sum(L)
    return f"{' + '.join(str(e) for e in L)} {'='} {summ}"

def main():
    pass

if __name__ == "__main__":
    main()
