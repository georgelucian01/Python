
## https://www.w3resource.com/python-exercises/puzzles/index.php
## August 09th 2023
## Problem number 2

# 2. Write a Python program that accepts a list of integers and calculates the length and the fifth element. 
# Return true if the length of the list is 8 and the fifth element occurs thrice in the said list.

def check_list(nums):
    
    if len(nums) < 8:
        return False
    
    fifth = nums[4]
    countf = 0

    for n in nums:
        if n == fifth:
            countf += 1

    if countf == 3:
        return True
    
    return False

# Main
def main():
    a = [19, 19, 15, 5, 5, 5, 1, 2]
    print(check_list(a))

    b = [19, 15, 5, 7, 5, 5, 2]
    print(check_list(b))

    c = [1, 3]
    print(check_list(c))
    
# Run main()
if __name__ == "__main__":
    main()
