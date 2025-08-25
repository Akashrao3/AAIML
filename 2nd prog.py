import numpy as np
import random
import time

def create_board():
    """Initializes and returns an empty 3x3 Tic-Tac-Toe board."""
    return np.full((3, 3), ' ')

def possibilities(board):
    """Returns a list of all empty spots (row, col) on the board."""
    return list(zip(*np.where(board == ' ')))

def evaluate(board):
    """
    Checks the current state of the board.
    Returns 'x' if player 'x' has won, 'o' if player 'o' has won,
    'Tie' if the board is full with no winner, and ' ' if the game is still in progress.
    """
    for p in ['x', 'o']:
        if (np.all(board == p, axis=1).any() or
            np.all(board == p, axis=0).any() or
            np.all(np.diag(board) == p) or
            np.all(np.diag(np.fliplr(board)) == p)):
            return p
    return 'Tie' if np.all(board != ' ') else ' ' 


def minimax(board, current_player):
    """
    Recursive function that implements the Minimax algorithm.
    It evaluates all possible moves to find the optimal one.
    """
    score = evaluate(board)
    
    
    if score == 'o':
        return 1
    elif score == 'x':
        return -1
    elif score == 'Tie':
        return 0
    
    is_maximizer = (current_player == 'o')
    
    if is_maximizer:
        best_val = -np.inf
        for move in possibilities(board):
            board[move] = 'o'
            best_val = max(best_val, minimax(board, 'x'))
            board[move] = ' ' 
        return best_val
    else:  
        best_val = np.inf
        for move in possibilities(board):
            board[move] = 'x'
            best_val = min(best_val, minimax(board, 'o'))
            board[move] = ' ' 
        return best_val

def find_best_move(board, player):
    """
    Iterates through all possible moves and calls the minimax function
    to find the one with the highest score.
    """
    if player == 'o':
        best_val = -np.inf
        
        moves = possibilities(board)
        random.shuffle(moves)
        
        best_move = None
        for move in moves:
            board[move] = 'o'
            move_val = minimax(board, 'x')
            board[move] = ' ' 
            
            if move_val > best_val:
                best_val = move_val
                best_move = move
        return best_move
    else:  
        best_val = np.inf
        
        moves = possibilities(board)
        random.shuffle(moves)

        best_move = None
        for move in moves:
            board[move] = 'x'
            move_val = minimax(board, 'o')
            board[move] = ' ' 
            
            if move_val < best_val:
                best_val = move_val
                best_move = move
        return best_move


def play_automated_game():
    """Main function to run the automated Tic-Tac-Toe game."""
    board = create_board()
    current_player = 'x'
    
    print("Welcome to Automated Tic-Tac-Toe! Both players ('x' and 'o') are controlled by Minimax.\n")
    print("Initial Board:\n", board, "\n")
    time.sleep(2)
    
    while True:
       
        game_result = evaluate(board)
        if game_result != ' ':
            return game_result
            

        move = find_best_move(board, current_player)
        board[move] = current_player
        
        print(f"Player {current_player} moves:")
        print(board, "\n")
        
     
        current_player = 'o' if current_player == 'x' else 'x'
        time.sleep(2)
    
    return 'Tie'

if __name__ == "__main__":
    winner = play_automated_game()
    print(f"Game over. Winner is: {winner}")
