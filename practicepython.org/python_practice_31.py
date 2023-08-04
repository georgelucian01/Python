
## July 28th 2023
## Problem number 31
## https://www.practicepython.org/exercise/2017/01/02/31-guess-letters.html

# cpu gives ranmdom letter
# player has to guess letter by letter
# *** player can guess a letter 6 times
# *** player can guess a word 2 times
# make a word look like this _ _ _ _ _
# guessing the same letter or word doesnt count
# stop the game if the player won


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
            return

def main():
    word = 'EVAPORATE'
    start_game(word)


if __name__ == "__main__":
    main()
