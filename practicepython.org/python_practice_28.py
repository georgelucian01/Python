
## July 28th 2023
## Problem number 28
## https://www.practicepython.org/exercise/2016/03/27/28-max-of-three.html

## Implement fucntion that takes 3 input variables
# return the largest
# do this with max()

from useful_functions import functions

def maximum(a, b, c):
    return max(max(a, b),c)

# Main
def main():
    a = functions.int_input_msg('A = ')
    b = functions.int_input_msg('B = ')
    c = functions.int_input_msg('C = ')
    print(f'Max is {maximum(a, b, c)}')

# Run main()
if __name__ == "__main__":
    main()
