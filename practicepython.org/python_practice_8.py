## July 21st 2023
## https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html

## Two player Rock Paper Scissors

actions = ['rock', 'paper', 'scissors']

    # winning combinations
wins = {'rock':'scissors', 'paper':'rock', 'scissors':'paper'} 

while True:
    # get player 1 action
    while True:
        p1 = (input("Action for player 1: ")).lower()
        if p1 in actions: break
        else: print("Enter a proper action")

    # get player 2 action
    while True:
        p2 = (input("Action for player 2: ")).lower()
        if p2 in actions: break
        else: print("Enter a proper action")

    if p1 == p2:
        print("Draw")
        continue
    if wins[p1] == p2: # if p1 is rock, it can only win against scissors, wins[rock] is scissors
        print("Player 1 Wins")
    else:
        print("Player 2 Wins")

    # Asking for continuation y/n
    while True:
        next = (input("Continue to play? y/n: ")).lower()
        if next == 'y' or next == 'n': break
        else: print("Enter y or n, for YES and NO")
    if next == 'y': continue
    # It breaks automaticly if next isn't y
    break