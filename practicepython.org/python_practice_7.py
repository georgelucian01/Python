## July 21st 2023
## https://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html

## 1 line of code
## create a new list with only even numbers

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

b = [num for num in a if num % 2 == 0]
print(b)

## More compact
print([num for num in a if num % 2 == 0]) 