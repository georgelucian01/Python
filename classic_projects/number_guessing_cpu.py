
class functions:

    def int_input_msg(message):
        while True:
            try:
                user_input = input(message)
                number = int(user_input)
                return number
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

import random

def guess_number(interval, number_to_be_guessed, number_of_guesses):
    a = interval[0]
    b = interval[1]
    print(f'Current inteval is {interval}')
    # generate random number from start to finish 10 to 30, 0 to 100 etc
    guess = random.randint(a, b)
    print(f'Computer guess was {guess}!')
    print('-----')

    if number_to_be_guessed == guess:
        print(f"The number was {guess}!\nThe computer guessed the answer!")
        print('')
        return number_of_guesses + 1
    
    # increase number of guesses
    number_of_guesses += 1
    
    
    if number_to_be_guessed < guess:
        # if the guess was bigger or lower than my number, make the interval smaller excluding the computer guess
        print("Number was bigger!")
        return guess_number([a, guess-1], number_to_be_guessed, number_of_guesses)
    else:
        print("Number was smaller!")
        return guess_number([guess+1, b], number_to_be_guessed, number_of_guesses)
   

# Main
def main():
    print("Guessing interval [a, b]: ")
    a = functions.int_input_msg('A: ')
    b = functions.int_input_msg('B: ')
    
    interval = [a, b]
    
    number = functions.int_input_msg("Number to be guessed: ")

    number_of_guesses = guess_number(interval, number, 0)
    print(f'It took {number_of_guesses} tries to get it right!')
    print('*****')
    

    
# Run main()
if __name__ == "__main__":
    main()
