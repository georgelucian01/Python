## July 22nd 2023
## https://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html

## ask user for a long string
## Print back to the user the same string
## with the words in backwards order



text = input("Give me a long sentence: ")
words = text.split(' ') # Split the str in words using a space

print("\n Version 1")
print(" ".join(reversed(words))) # 1 line
print(' '.join(text.split()[::-1])) # 1 line


print("\n Version 2")
backwards = [word for word in reversed(words)] # reverse list words
result = " ".join(backwards) # join the list elems with " " in between
print(result)
