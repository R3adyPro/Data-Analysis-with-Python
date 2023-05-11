#!/usr/bin/env python3

def reverse_dictionary(d):
    reverse = {}

    for key, value in d.items():
        if ((len(reverse) != 0 and value[0] in reverse.keys())):
            reverse[value[0]].append(key)
            continue
        if len(value) > 1:
            for i in value:
                reverse[i] = [key]
        else:
            reverse[value[0]] = [key]   
        
    print(reverse)
    return reverse

def main():
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    reverse_dictionary(d)
    pass

if __name__ == "__main__":
    main()
