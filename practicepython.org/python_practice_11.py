## July 22nd 2023
## https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html

## Ask user for number
## Prime or not?
## Use Exercise 4

    # Function using exercise 4
def PrimeOrNot (num):

    divisors = []
    for i in range(1,int(num/2)+1):
        if num % i == 0:
            divisors.append(i)
    divisors.append(num)

    if len(divisors) == 2:
        print("Number is Prime!")
    else: 
        print("Number is NOT Prime!")

    # Checking if input is integer
while True:
    num_str = input("Is this number Prime or NOT?\n")
    try:
        num = int(num_str)
        break
    except ValueError:
        print("Input an integer number!")
    
    # Calling function
PrimeOrNot(num)

    