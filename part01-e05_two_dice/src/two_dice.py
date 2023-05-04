#!/usr/bin/env python3

def main():
    for dice1 in [1,2,3,4,5,6]:
        for dice2 in [1,2,3,4,5,6]:
            if (dice1+dice2 == 5):
                print((dice1, dice2))
    pass

if __name__ == "__main__":
    main()
