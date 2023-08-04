
## July 28th 2023
## Problem number 30
## https://www.practicepython.org/exercise/2016/09/24/30-pick-word.html

# Write function hta picks a random word from txt file

import random
# Read file, transform into a list, pick random word, then remove \n
def random_sowpods(file):
    with open(f'{file}.txt', 'r') as read_file:
        word_list = read_file.readlines()
        word = random.choice(word_list).strip()
    return word
# Main
def main():
    # file sowpods.txt
    print(random_sowpods('sowpods'))
    
# Run main()
if __name__ == "__main__":
    main()
