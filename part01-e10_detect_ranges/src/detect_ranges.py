#!/usr/bin/env python3

def detect_ranges(L):
    s_list = sorted(L)
    new_list = []
    mini = 0
    previous = min(L)

    for i in s_list:
        if i != previous+1:
            new_list.append(i)
        elif type(new_list[-1]) is tuple:
            new_list[-1] = (mini, i + 1)
        else:
            new_list[-1] = (previous, i + 1)
            mini = previous
        previous = i

    return [new_list][0]

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)
if __name__ == "__main__":
    main()
