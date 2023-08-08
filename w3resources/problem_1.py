
## https://www.w3resource.com/python-exercises/puzzles/index.php
## August 09th 2023
## Problem number 1

# 1. Write a Python program to find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five. Return True otherwise False.

def check_list(nums):

    count19 = 0
    count5 = 0
    
    for num in nums:
        if num == 19:
            count19 += 1
        if num == 5:
            count5 += 1

    if count19 == 2 and count5 >= 3:
        return True
    
    return False

# Main
def main():
    a = [19, 19, 15, 5, 3, 5, 5, 2]
    print(check_list(a))

    b = [19, 15, 15, 5, 3, 3, 5, 2]
    print(check_list(b))


# Run main()
if __name__ == "__main__":
    main()
