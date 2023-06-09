#!/usr/bin/env python3


import re

def integers_in_brackets(s):
    reg = re.findall(r"\[\s*([+-]?\d+)\s*\]", s)
    numbers = list(int(x) for x in reg)
    return numbers

def main():
    print(integers_in_brackets(" afd [asd] [12 ] [a34] [ -43 ]tt [+12]xxx"))
    pass

if __name__ == "__main__":
    main()
