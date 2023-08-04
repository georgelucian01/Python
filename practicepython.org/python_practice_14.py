## July 22nd 2023
## https://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html

## Program that takes list and creates a new list with no duplicates

from useful_functions import functions

print("______________________________________")
print(" ")
print("_____________Main Problem_____________")

list1 = functions.random_list_of_ints(30, 20) #gemerates a list of 20 nums in the range of 0 - 30 

list2 = list(set(list1)) # sets do not allow duplicates

print(list2)


## Extra - Write two different functions to do this 
    # one using a loop and constructing a list
    # and another using sets

print(" ")
print("________________Extra_________________")

def loop_for_list(range_of_nums, size_of_list):
    import random
    nums = []
    while size_of_list > 0:
        nums.append(random.randint(0, range_of_nums))
        size_of_list -= 1
    print(nums)
    return nums

def remove_duplicates(nums):
    nums = list(set(nums))
    print(nums)
    return nums


list3 = loop_for_list(10,5)
list4 = remove_duplicates(list3)

print("______________________________________")
print(" ")