#!/usr/bin/env python3

class Prepend(object):
    # Add the methods of the class here
    def __init__(self, param) :
        self.start = param

    def write(self, param):
        print(self.start + param)


def main():
    p = Prepend("+++ ")
    p.write("Hello")
    pass

if __name__ == "__main__":
    main()
