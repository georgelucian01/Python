
## July 23rd 2023
## Problem number 20
## https://www.practicepython.org/exercise/2014/11/11/20-element-search.html


## Function that takes in ordered list and another number
## Checks if the number is in the list and returns True of False
## Use Binary

def check_list(list, number):

    # Middle character using div
    mid = len(list) // 2

    # Checking if the list of 1 element is equal to a list of 1 element [number]
    if list == [number]:
        return True
    
    # If the middle is equal to the number
    if mid == 0:
        return False

    # If number is bigger or smaller than middle, go to the left or right in the list
    list = list[:mid] if number < list[mid] else list[mid:]
    print(list)
    
    # Recursing calling, until list becomes 0 or find the number
    return check_list(list, number)


def main():
    a = [1, 3, 5, 30, 32, 35, 40, 42, 43, 500, 600]
    print(a)
    print(check_list(a, 600))
    

if __name__ == "__main__":
    main()
