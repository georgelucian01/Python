## July 22nd 2023
## https://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html

## Asks user how many Fibonnaci numbers to generate
## Use functions

    
    # class I created with useful functions such as "int user input"
from useful_functions import functions

    # Function that generates fibonnaci list
def Fibonnaci(num):
    if num == 0: return 0
    elif num == 1: return [1]
    else:
        result = [1, 1]

    # add the last 2 numbers sum
    for i in range(2, num):
        result.append(result[i-2] + result[i-1])
    return result
    
    
## Main
num = functions.int_input() # int input from a class I created
print(Fibonnaci(num))