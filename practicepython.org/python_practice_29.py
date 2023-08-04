
## July 28th 2023
## Problem number 29
## https://www.practicepython.org/exercise/2016/08/03/29-tic-tac-toe-game.html



import random
from useful_functions import functions

# Check winner function
def check_winner(game):
    winning_combos = [[1, 1, 1], [2, 2, 2]]

    for row in game:
        if row in winning_combos:
            return row[0]  # Return the first element of the winning row (1 or 2)

    columns = [[game[0][i], game[1][i], game[2][i]] for i in range(3)]
    diagonals = [[game[0][0], game[1][1], game[2][2]], [game[0][2], game[1][1], game[2][0]]]
    positions = columns + diagonals

    for pos in positions:
        if pos in winning_combos:
            return pos[0]  # Return the first element of the winning position (1 or 2)

    return None  # If no winner is found, return None

# Inser Value on board function
def insert_value(game):
    # Getting 1 or 2 value and checking if spot is already taken
    while True:
        print("Position to input X (row, column): ")
        x = functions.int_input_msg("Row:")
        y = functions.int_input_msg("Column:")
        if 1 <= x <= 3 and 1 <= y <= 3:
            if game[x-1][y-1] == 0:
                break
            else:
                print("Spot is already taken! Try again!")
                continue
        else: continue
    # Put an X on position 
    game[x-1][y-1] = 1

    # Return game board
    for row in game:
        print(row)
    return game

# Checking if there are any 0's on the board (empty space)
def check_board_not_full(game):
    for row in game:
        if 0 in row:
            return True
    print("Draw")
    return False

# CPU, has to be redone IN A MORE INTELLIGENT WAY
def cpu(game):
    
    while True:
        x = random.randint(1, 3)
        y = random.randint(1, 3)
        if game[x - 1][y - 1] == 0:
            game[x - 1][y - 1] = 2
            print(f"CPU plays: row {x}, column {y}")
            for row in game:
                print(row)
            return game

# Main
def main():
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    while check_board_not_full(game):
        game = insert_value(game)
        winner = check_winner(game)
        if winner is not None:
            print(f"Player {winner} wins!")
            break

        game = cpu(game)
        winner = check_winner(game)
        if winner is not None:
            print(f"Player {winner} wins!")
            break
        
        
        
# Run main()
if __name__ == "__main__":
    main()
