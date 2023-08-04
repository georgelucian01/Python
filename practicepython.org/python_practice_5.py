## July 21st 2023
## https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html

## 2 Lists
## Print the DISTINCT common elements from both lists
## Make sure your program works on two lists of different sizes

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


c = [x for x in a if x in b] ## Making a third list
c_set = set(c) ## Sets do not allow duplicates
c = list(c_set) ## Transforming it back into a list

print(c)

## Extra 1 - Randomly generate two lists to test this

import random
d = random.sample(range(1,100),50)
e = random.sample(range(1,100),30)

f = [x for x in d if x in e] ## Making a third list
f_set = set(f) ## Sets do not allow duplicates
f = list(f_set) ## Transforming it back into a list

print(f)

## Extra 2 - Write this in one line of Python

common_elems = list(set(a) & set(b))
print(common_elems)