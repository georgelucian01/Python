## July 23nd 2023
## https://www.practicepython.org/exercise/2014/07/05/18-cows-and-bulls.html

## Cows and Bulls
## Generate 4 digit number (ill using 1000-2000 numbers so its easier to guess)
## Guess a 4 digit number
## 1245 is hte generated number, if i guess 1959 the program has to give me 1 cow 1 bull
## cow for every corect digit in the right place
## bull for every corect digit in the wrong place


import random
from useful_functions import functions

def cow_bull(number, guess):
    cows = 0
    bulls = 0
    matched_indices = []  # To keep track of matched indices

    for i in range(len(number)):
        for j in range(len(guess)):
            if number[i] == guess[j]:  # If digits are equal
                if i == j:  # If digits are equal and on the same index
                    cows += 1
                elif j not in matched_indices:  # If digits are equal and on the wrong index
                    bulls += 1
                    matched_indices.append(j)  # Mark this index as matched to avoid duplicate bulls

    print(f"{cows} cows, {bulls} bulls")  # Printing the number of cows and bulls we got

def main():
    number = str(random.randint(1000, 1999))
    print("The number has been chosen")
    tries = 0

    while True:
        guess = str(functions.int_input_x_digit(4)) # function I wrote myself in a class
        cow_bull(number, guess)
        tries += 1
        if number == guess: # if we guess corectly stop while
            print(f"You won! The number was indeed {guess}.\nYou got it right after {tries} tries.")
            break

if __name__ == "__main__":
    main()

    

    

