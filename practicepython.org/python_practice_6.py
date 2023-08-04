## July 21st 2023
## https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html

## Ask user for string
## Check if string is palindrome

## First version
"""
text = str(input("Enter an word:"))

y = len(text)-1 ## Position of last char

check = True ## if the check changes it means the str isnt a palindrome

for i in range(y):
    if text[i] != text[y]: 
        check = False
        break ## if the chars on either side aren't equal, then the str isnt palindrome
    y -= 1

if(check): print("It's palindrome")
else: print("It's not palindrome") """

## Second version - shorter, stops potential bugs

    # Asking for input if its empty
while True:
    text = str(input("Word for checking palindrome: "))
    if len(text) == 0: print("It's empty!")
    else: break

toCheck = text.lower() # A != a

if toCheck == toCheck[::-1]:
    print("It is a palindrome string!")
else:
    print("It is not a palindrome string!")

