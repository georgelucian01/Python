
## July 27th 2023
## Problem number 24
## https://www.practicepython.org/exercise/2014/12/27/24-draw-a-game-board.html

## Print a board game
"""
 --- --- --- 
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- --- 
"""
## ask user for dimension 3x3, 8x8 etc

def draw_board(n):
    # number of elements in each list
    num = n*2+1
   
    # matrix of num,num size
    board = [['' for _ in range(num)] for _ in range(num)]
    for i in range(num):
        for j in range(num):
            # if i is odd print ' ' or '-'
            if i % 2 == 0:
                # if j is divisible by 4 then print ' ', else '-'
                if j % 2 == 0:
                    board[i][j] = ' '
                else:
                    board[i][j] = '---'
            else: 
                if j % 2 == 0:
                    board[i][j] = '|'
                else:
                    board[i][j] = '   '

    for row in board:
        print("".join(row))        

# Main
def main():
    draw_board(3)
    
# Run main()
if __name__ == "__main__":
    main()
