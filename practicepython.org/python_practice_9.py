## July 21st 2023
## https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html

## Generate random number between 1 and 9 (including)
## Ask user to guess
## Msg if its too low, too high or exactly right

    # 1. Generate the number with random
    # 2. Get user input
    # 3. Give answer with ifs

""" 
import random
num = random.randint(1, 9)
print("The Number Has Been Chosen!")

# checking if input is number
while True:
    guess = input("Guess the number: ")
    try:
        guess = int(guess)
    except ValueError:
        print("Enter a number!!!")
        continue  # Go back to the start of the loop if the input is not a number

    if guess < num:
        print("Too Low")
    elif guess > num:
        print("Too High")
    else:
        print("You guessed right!")
        break  # Exit the loop if the guessed number is correct """


## Extra 1 - Keep the game going until the user types “exit”
## Extra 2 - Keep track of how many guesses the user has taken, and when the game ends, print this out.

""" 1. While True loop
    2. Keep the game going until user types "exit"
        use an if in the input loop
    3. Keep track of wins 
        use a variable to track wins, wins++ in the else """


import random

wins = 0  # tracking wins
total = 0 # tracking numbers
stop = False


while True:
    num = random.randint(1, 9)
    
    # checking if input is number
    while True:
        guess_str = input("Guess the number: ")
        if guess_str == "exit":
            stop = True
            break
        try:
            guess_int = int(guess_str)
            break
        except ValueError:
            print("Enter a number")
        
    if stop: break  # Exit the outer loop if the input was "exit"

    if guess_int < num:
        print("Too Low")
    elif guess_int > num:
        print("Too High")
    else:
        print("You guessed right")
        wins += 1
    total += 1    

    # added a % because its cool
    # stopped division by 0, if user decided to exit without guessing
if total == 0:
    print("You guessed correctly " + str(wins) + " times!")
else: 
    print("You guessed correctly " + str(wins) + " times out of " + str(total) + ", thats aprox " +str(int(wins / total * 100)) + "% out of all numbers")