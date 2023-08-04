## July 21st, 2023
## https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html
## Exercise 3 List Less than Ten

## Write a program that prints out all the elements of the list that are less than 5.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for x in a:
    if x < 5:
        print(x)


## Extras 1 - make a new list that has all the elements less than 5

b = []
for x in a:
    if x < 5:
        b.append(x)
print(b)

## Extras 2 - Write this in one line of Python.

c = [num for num in a if num < 5] ## if the condition is true, then num is added to the list
print(c)

## Extras 3 - Ask the user for a number to compare

check = int(input("Number for comparison: "))
d = [num for num in a if num < check]
print(d)