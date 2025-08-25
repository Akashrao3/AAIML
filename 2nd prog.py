import numpy as np
import random

def create_board():
    return np.full((3, 3), ' ')

def possibilities(board):
    return list(zip(*np.where(board == ' ')))

def random_place(board, player):
    board[random.choice(possibilities(board))] = player
    return board

def evaluate(board):
    for p in ['x', 'o']:
        if (np.all(board == p, axis=1).any() or
            np.all(board == p, axis=0).any() or
            np.all(np.diag(board) == p) or
            np.all(np.diag(np.fliplr(board)) == p)):
            return p
    return 'Tie' if np.all(board != ' ') else ' ' 

def get_user_move(board):
    while True:
        try:
            move = input("Enter your move (row, col): ")
            row, col = map(int, move.split(','))
            if (row, col) in possibilities(board):
                return (row, col)
            else:
                print("Invalid move. The spot is already taken or does not exist. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter in the format 'row,col', like '0,1'.")

def play_game():
    board = create_board()
    print("Initial Board:\n", board, "\n")
    while True:
        1,
        if evaluate(board) != ' ':
            return evaluate(board)
        if possibilities(board):
            user_move = get_user_move(board)
            board[user_move] = 'x'
            print(f"Player x moves:\n", board, "\n")
        
        
        if evaluate(board) != ' ':
            return evaluate(board)
        if possibilities(board):
            board = random_place(board, 'o')
            print(f"Player o moves:\n", board, "\n")
    
    return 'Tie'

if __name__ == "__main__":
    winner = play_game()
    print(f"Game over. Winner is: {winner}")