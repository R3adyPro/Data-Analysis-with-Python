#!/usr/bin/env python3


def main():
    for row in [1,2,3,4,5,6,7,8,9,10]:
        for column in [1,2,3,4,5,6,7,8,9,10]:
            sum = row * column
            if column == 10:
                print(f"{sum:4d}")
            else:
                print(f"{sum:4d}", end="")
    pass

if __name__ == "__main__":
    main()
