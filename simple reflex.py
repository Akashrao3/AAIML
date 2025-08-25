import numpy as np
import time
import random

def display_grid(grid, agent_pos):
    """Displays the grid with the agent's position."""
    display_board = np.copy(grid)
    display_board[agent_pos] = 'A'
    print("\n" + "\n".join([" ".join(row) for row in display_board]))

def get_target_pos(grid, target='T'):
    """Finds the coordinates of the target 'T'."""
    target_pos = np.argwhere(grid == target)
    if target_pos.size > 0:
        return tuple(target_pos[0])
    return None

def get_agent_move(grid, pos, target_pos):
    """
    Determines the best move for the agent to reach the target.
    It prioritizes moves that decrease the Manhattan distance to the target.
    """
    rows, cols = grid.shape
    r, c = pos
    
    possible_moves = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1)
    }
    
   
    current_dist = abs(pos[0] - target_pos[0]) + abs(pos[1] - target_pos[1])
    
    best_moves = []
    

    for move_name, (dr, dc) in possible_moves.items():
        new_r, new_c = r + dr, c + dc
        
        if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r, new_c] != '#':
            new_pos = (new_r, new_c)
            new_dist = abs(new_pos[0] - target_pos[0]) + abs(new_pos[1] - target_pos[1])
            
            if new_dist < current_dist:
                best_moves.append(new_pos)
                

    if best_moves:
        return random.choice(best_moves)
    

   
    valid_moves = []
    for move_name, (dr, dc) in possible_moves.items():
        new_r, new_c = r + dr, c + dc
        if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r, new_c] != '#':
            valid_moves.append((new_r, new_c))
    
    if valid_moves:
        return random.choice(valid_moves)
        
    return pos

def navigate_grid(grid, start_pos, target='T', max_steps=20):
    """Simulates the agent navigating the grid to find the target."""
    pos = start_pos
    target_pos = get_target_pos(grid, target)
    
    if target_pos is None:
        print("Error: Target not found on the grid.")
        return

    print("Welcome to Grid Navigation! The agent is programmed to reach 'T' as efficiently as possible.")
    
    for step in range(1, max_steps + 1):
        display_grid(grid, pos)
        

        if grid[pos] == target:
            print("\nTask completed! Agent reached the target.")
            grid[pos] = '.'
            break
            
        new_pos = get_agent_move(grid, pos, target_pos)
        pos = new_pos
        
        time.sleep(0.5) 
    
    else:
        print(f"\nSimulation ended after {max_steps} steps. Target was not reached.")

grid = np.array([
    ['.', '.', '.', '#', '.'],
    ['#', '.', '.', '#', '.'],
    ['.', '.', '#', '.', '.'],
    ['.', '#', '.', '.', '.'],
    ['.', '.', '.', '.', 'T']
])

navigate_grid(grid, (0, 0))
