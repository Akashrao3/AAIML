import numpy as np
import time

def display_grid(grid, agent_pos):
    display_board = np.copy(grid)
    display_board[agent_pos] = 'A'
    print("\n".join([" ".join(row) for row in display_board]))

def get_user_move(grid, pos):
    valid_moves = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
    while True:
        move = input("Enter a move (up, down, left, right): ").lower()
        if move in valid_moves:
            dr, dc = valid_moves[move]
            new_r, new_c = pos[0] + dr, pos[1] + dc
            if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]) and grid[new_r, new_c] != '#':
                return (new_r, new_c)
            else:
                print("Invalid move. You hit a wall or obstacle.")
        else:
            print("Invalid input. Please enter 'up', 'down', 'left', or 'right'.")

def navigate_grid_user(grid, start_pos):
    pos = start_pos
    for _ in range(20):
        display_grid(grid, pos)
        pos = get_user_move(grid, pos)
        if grid[pos] == 'T':
            print("Task completed!")
            grid[pos] = '.'
        time.sleep(0.5)
grid = np.array([
    ['.', '.', '.', '#', '.'],
    ['#', '.', '.', '#', '.'],
    ['.', '.', '#', '.', '.'],
    ['.', '#', '.', '.', '.'],
    ['.', '.', '.', '.', 'T']
])

print("Welcome to Grid Navigation! Navigate to 'T' and avoid '#'.")
navigate_grid_user(grid, (0, 0))
print("\nSimulation ended.")