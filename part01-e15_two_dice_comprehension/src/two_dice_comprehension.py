#!/usr/bin/env python3

def main():
    print('\n'.join(f"({d1}, {d2})" for d1 in range(1,7) for d2 in range(1,7) if d1+d2 == 5))
    pass

if __name__ == "__main__":
    main()
