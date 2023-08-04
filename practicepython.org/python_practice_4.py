## July 21st 2023
## https://www.practicepython.org/exercise/2014/02/26/04-divisors.html


## Ask user for a number
## Print out a list of all the divisors of that number

num = int(input("Input a number: "))
divisors = []


for i in range(1,int(num/2)+1): ## Half the number, there aren't any divisors after num/2+1
    if num % i == 0:
        divisors.append(i)

## add the number itself to the list
divisors.append(num)

print(divisors)