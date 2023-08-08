
## https://www.w3resource.com/python-exercises/puzzles/index.php
## August 09th 2023
## Problem number 3

# 3. Write a Python program that accepts an integer and determines 
# whether it is greater than 4^4 and which is 4 mod 34.


def number(n):
    return n > 4**4 and n % 34 == 4

# Main
def main():
    a = 922
    b = 914
    print(number(a))
    print(number(b))
    
# Run main()
if __name__ == "__main__":
    main()
