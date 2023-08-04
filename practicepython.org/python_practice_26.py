
## July 27th 2023
## Problem number 26
## https://www.practicepython.org/exercise/2015/11/16/26-check-tic-tac-toe.html



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


def main():
    game = [[1, 2, 0],
            [2, 1, 0],
            [2, 1, 1]]

    for row in game:
        print(row)

    winner = check_winner(game)
    if winner is not None:
        print(f"Player {winner} wins!")
    else:
        print("No winner yet.")

# Run main()
if __name__ == "__main__":
    main()
