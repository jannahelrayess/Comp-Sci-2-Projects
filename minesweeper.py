'''
minesweeper.py
Jannah El-Rayess
2020-12-02

This is a program for the game Minesweeper, where the objective is to
clear a rectangular board containing hidden mines without denotating
any of them using clues from neighboring cells.
'''

# _______Helper Functions and Imports_______ #

import random

# show: list ->
# Prints each row of the matrix on a separate line without punctuation
def show(mtrx):
    for i in range(len(mtrx)):
        for j in range(len(mtrx[0])):
            print(str(mtrx[i][j]) + ' ', end='')
        print()

# in_range: int int -> bool
# Says whether the desired row and column are out of range
def in_range(row, col):
    if row >= 0 and row <= 9 and col >= 0 and col <= 9:
        return True
    else:
        return False

# is_mine: str -> int
# Returns a 1 for a mine and a 0 otherwise
def is_mine(val):
    if val == 'M':
        return 1
    else:
        return 0

# covered: -> list
# Makes a 10 by 10 matrix filled with 'H's
def covered():
    mtrx = []
    
    for i in range(10):
        row = []
        for j in range(10):
            row.append('H')
        mtrx.append(row)
        
    return mtrx

# count_2D: list -> integer
# Counts the number of 'H' in the board
def count_2D(lst):
    num = 0
    
    for i in range(10):
        for j in range(10):
            if lst[i][j] != 'H':
                num += 1
                
    return num

# _______Main Functions_______ #

# place_mines: -> list
# Makes a 10 by 10 matrix filled with randomly placed mines (aka M)
def place_mines():
    lst = []

    # Until the matrix has a length of 100 keep adding a random integer between 
    # 0 and 100 to the list and make sure there are no repeats of integers
    while len(lst) != 100:
        val = random.randint(0,100)
        
        if val not in lst:
            lst.append(val)

    # For all the integers in the list that are under 10, change them to 'M'.
    # This causes 10 random mines to be placed because the numbers 0 thorugh 9 
    # Are randomly placed in the list.          
    for i in range(len(lst)):
        if lst[i] < 10:
            lst[i] = 'M'
        else:
            lst[i] = 0

    # Cited: https://realpython.com/list-comprehension-python/ (where I learned
    # List comprehension)
    mtrx = [lst[j:j+10] for j in range(0, 100, 10)]
    
    return mtrx

# make_clues: int int list -> int
# Indicates how many mines are found in the surrounding cells of the cell given
def make_clues(row, col, mtrx):
    surrounding_mines = 0

    if in_range(row - 1, col):
        surrounding_mines += is_mine(mtrx[row - 1][col])
    
    if in_range(row + 1, col):
        surrounding_mines += is_mine(mtrx[row + 1][col])
    
    if in_range(row, col + 1):
        surrounding_mines += is_mine(mtrx[row][col + 1])
    
    if in_range(row, col - 1):
        surrounding_mines += is_mine(mtrx[row][col - 1])
    
    if in_range(row - 1, col + 1):
        surrounding_mines += is_mine(mtrx[row - 1][col + 1])
    
    if in_range(row - 1, col - 1):
        surrounding_mines += is_mine(mtrx[row - 1][col - 1])
    
    if in_range(row + 1, col + 1):
        surrounding_mines += is_mine(mtrx[row + 1][col + 1])
    
    if in_range(row + 1, col - 1):
        surrounding_mines += is_mine(mtrx[row + 1][col - 1])
    
    return surrounding_mines

# hidden_board: list -> list
# Creates the hidden board with the clue values and mine placements
def hidden_board(mtrx):
    clue_board = []
    
    for row in range(10):
        rows = []
        clue_board.append(rows)
        for col in range(10):
            rows.append(make_clues(row, col, mtrx))
            if mtrx[row][col] == 'M':
                clue_board[row][col] = 'M'
                
    return clue_board

# uncover: int int list list -> 
# Recursively uncovers the chosen cell's surrounding cells if there 
# Are no mines and the cell is a 0. It stops uncovering cells once
# A number between (and including) 1 and 8 is reached. If the chosen
# Cell is a not a 0, only that cell is uncovered.
def uncover(row, col, clue_board, shown_board):
    if shown_board[row][col] != 'H':
        shown_board[row][col] = clue_board[row][col]

    else:
        if clue_board[row][col] == 0:
            shown_board[row][col] = clue_board[row][col]
            
            if in_range(row - 1, col):
                uncover(row - 1, col, clue_board, shown_board)
            
            if in_range(row + 1, col):
                uncover(row + 1, col, clue_board, shown_board)
            
            if in_range(row, col + 1):
                uncover(row, col + 1, clue_board, shown_board)
        
            if in_range(row, col - 1):
                uncover(row, col - 1, clue_board, shown_board)
        
            if in_range(row - 1, col + 1):
                uncover(row - 1, col + 1, clue_board, shown_board)
        
            if in_range(row - 1, col - 1):
                uncover(row - 1, col - 1, clue_board, shown_board)
        
            if in_range(row + 1, col + 1):
                uncover(row + 1, col + 1, clue_board, shown_board)
        
            if in_range(row + 1, col - 1):
                uncover(row + 1, col - 1, clue_board, shown_board)
        
        else:
           shown_board[row][col] = clue_board[row][col]

# colored: list int int -> str
# Colors the shown minefield based on the cell value and also returns
# Whether the game is lost or not depending on if the user picked a mine 
def colored(shown_board, r, c):
    game_over = 'n'

    print('\033[2J\033[H')

    for r in range(10):
        for c in range(10):
            if shown_board[r][c] == 'M':
                shown_board[r][c] = '\u001b[31m' + "M" + '\u001b[0m'
                print('You lost the game!')
                game_over = 'y'

            elif shown_board[r][c] == 0:
                shown_board[r][c] = '\u001b[34m' + "0" + '\u001b[0m'
            
            elif shown_board[r][c] == 1:
                shown_board[r][c] = '\u001b[36m' + "1" + '\u001b[0m'
            
            elif shown_board[r][c] == 2:
                shown_board[r][c] = '\u001b[35m' + "2" + '\u001b[0m'
            
            elif shown_board[r][c] == 3:
                shown_board[r][c] = '\u001b[32m' + "3" + '\u001b[0m'
            
            elif shown_board[r][c] in range(4, 9):
                shown_board[r][c] = '\u001b[33m' + "4" + '\u001b[0m'

    return game_over

# game: ->
# The function called to play the game that prompts the user for
# A row and column and continues this until a mine is activated or
# All the cells that are not mines are uncovered, which is 90 cells
def game():
    mtrx = place_mines()
    clue_board = hidden_board(mtrx)
    shown_board = covered()
    r = 10
    c = 10
    game_over = 'n'
    play_again = 'n'
    
    show(shown_board)

    while game_over != 'y':  
        if count_2D(shown_board) == 90:
            print('You won the game!')
            game_over = 'y'
            break
            
        while r not in range(0, 10):
            r = int(input('Enter a row (0 - 9): '))

        while c not in range(0, 10):
            c = int(input('Enter a column (0 - 9): '))

        if clue_board[r][c] != 'M' or count_2D(shown_board) != 90:
            uncover(r, c, clue_board, shown_board)
            game_over = colored(shown_board, r, c)
            show(shown_board)

        # r and c have to be reset so that way the program will ask 
        # Again to input values because 10 is invalid   
        r = 10
        c = 10
    
    play_again = input('Do you want to play again? (y/n): ')
    print('\033[2J\033[H')
    
    while play_again != 'n':
        game()
    print('Ok, thanks for playing! :)')

    # play_again and game_over are reset since the program doesn't 
    # Ask the user again whether they would like to play again or not 
    play_again = 'n'
    game_over = 'y'

game()