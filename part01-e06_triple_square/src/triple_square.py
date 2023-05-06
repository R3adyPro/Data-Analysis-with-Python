#!/usr/bin/env python3

def triple(num):
    return num * 3

def square(num):
    return num ** 2 

def main():
    for number in range(1,11):
        triple_result = triple(number)
        square_result = square(number)
        if square_result > triple_result:
            break
        else:
            print(f"triple({number})=={triple_result} square({number})=={square_result}")
    pass

if __name__ == "__main__":
    main()
