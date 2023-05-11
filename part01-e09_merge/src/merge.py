#!/usr/bin/env python3
def sort(L):
    old_list = L
    sorted_list = []
    while old_list:
        min = old_list[0]  
        for x in old_list: 
            if x < min:
                min = x
        sorted_list.append(min)
        old_list.remove(min)  
    return sorted_list

def merge(L1, L2):
    new_l = [*L1, *L2]
    l4 = sort(new_l)
    return l4

def main():
    l1 = [1, 5, 9, 12]
    l2 = [2, 6, 10]
    print(merge(l1,l2))
    pass

if __name__ == "__main__":
    main()
