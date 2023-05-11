#!/usr/bin/env python3
def interleave(*lists):
    s_list = []

    for ls in zip(*lists):
        s_list.extend(ls)

    return [s_list][0]

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
