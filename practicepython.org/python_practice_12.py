## July 22nd 2023
## https://www.practicepython.org/exercise/2014/04/25/12-list-ends.html

## Program that takes in a list of numbers
## Makes new list of only the first and last elements
## Write in a function


    # Function that returns the contents for the 2nd list
def make_list(list):
    return list[::len(list)-1]

import random

    # random list
a = random.sample(range(20), 15)
print(a)

    # calling function
b = make_list(a)
print(b)