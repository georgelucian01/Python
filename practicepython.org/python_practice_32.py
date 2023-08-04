
## July 28th 2023
## Problem number 32
## https://www.practicepython.org/exercise/2017/01/10/32-hangman.html

import random
# Read file, transform into a list, pick random word, then remove \n
def random_sowpods(file):
    with open(f'{file}.txt', 'r') as read_file:
        word_list = read_file.readlines()
        word = random.choice(word_list).strip()
    return word

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def start_game(word):
    attempts_left = 6
    word_attempts_left = 2
    guessed_letters = set()
    guessed_words = set()

    print("Welcome to the letter guessing game!")
    print("Word to guess:", display_word(word, guessed_letters))

    while "_" in display_word(word, guessed_letters):
        guess = input("Enter your guess (a letter or a word): ").upper()

        if len(guess) == 1:  # Guessing a letter
            if guess in guessed_letters:
                print("You already guessed this letter.")
            else:
                guessed_letters.add(guess)
                if guess in word:
                    print("Correct guess!")
                else:
                    attempts_left -= 1
                    print("Incorrect guess.")
                print("Word to guess:", display_word(word, guessed_letters))
                print(f"Attempts left: {attempts_left}")

        else:  # Guessing a word
            if guess in guessed_words:
                print("You already guessed this word.")
            else:
                guessed_words.add(guess)
                if guess == word:
                    print("Congratulations! You guessed the word correctly.")
                    return
                else:
                    word_attempts_left -= 1
                    print("Incorrect word guess.")
                if word_attempts_left > 0:
                    print(f"Word attempts left: {word_attempts_left}")
                else:
                    print("You have no more attempts to guess the word.")

        if attempts_left == 0:
            print("Game over. You ran out of attempts.")
            print(f"The was was {word}!")
            return

def main():
    word = random_sowpods('sowpods')
    start_game(word)


if __name__ == "__main__":
    main()
