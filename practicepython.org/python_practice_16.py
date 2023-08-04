## July 22nd 2023
## https://www.practicepython.org/exercise/2014/05/28/16-password-generator.html

## July 23nd 2023
## https://www.practicepython.org/exercise/2014/05/28/16-password-generator.html

## Password generator
## Ask user for very easy/easy/medium/hard (I'll add very easy password)
## Very Easy passwords, have to be picked from a list of words
## Easy are to be 8 characters - random letters only
## Easy are to be 12 characters - random letters, numbers
## Easy are to be 18 characters - random letters, numbers, symbols
## Add run time code in main

# 1. Ask user for input
# 2. Use random
import random
import string

# Lists of chars
letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

# Ask proper input
def ask_input():
    while True:
        ans = input("What type of password do you want?\nVeryEasy/Easy/Medium/Hard (Exit to quit): ")
        ans = ans.lower()
        if ans == "veryeasy":
            return "veasy"
        elif ans == "easy":
            return "easy"
        elif ans == "medium":
            return "medium"
        elif ans == "hard":
            return "hard"
        elif ans == "exit":
            return "exit"
        else:
            print("Give a proper option!")

# generates random chars, add them, then it shuffles them around, then it joins the list into a string
def generate_password():
    while True:
        type = ask_input()
        if type == "veasy":
            print(random.choice(["cheese", "cucumber", "chococake", "metaldoor"]))
        elif type == "easy":
            easy_list = random.choices(letters, k=8)
            random.shuffle(easy_list)
            easy = ''.join(easy_list)
            print(easy)

        elif type == "medium":
            medium_list = random.choices(letters, k=6) + random.choices(numbers, k=6)
            random.shuffle(medium_list)
            medium = ''.join(medium_list)
            print(medium)

        elif type == "hard":
            hard_list = random.choices(letters, k=6) + random.choices(numbers, k=6) + random.choices(symbols, k=6)
            random.shuffle(hard_list)
            hard = ''.join(hard_list)
            print(hard)

        else:
            print("You have exited the program!")
            break


def main():
    generate_password()
