import os
import time

# 1. Create a 5x5 matrix filled with empty spaces "."
matrix = [
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."]
]

# Initial position of our object "X"
player_row = 0
player_col = 2
matrix[player_row][player_col] = "X"

def draw_matrix(grid):
    """Clears the terminal and prints the matrix cleanly."""
    os.system('cls')
    for row in grid:
        print(" ".join(row))
    print("\n-----------------")

def recalculate_matrix(grid, current_row, current_col):
    """Recalculates the grid by moving the 'X' down by one row."""
    # Erase the old position
    grid[current_row][current_col] = "."
    
    # Calculate new position (wrap around to the top if it goes off-screen)
    new_row = (current_row + 1) % 5
    
    # Place the object in the new position
    grid[new_row][current_col] = "X"
    
    return new_row

# Animation Loop (Recalculating 5 times)
for _ in range(5):
    draw_matrix(matrix)
    time.sleep(1) # Wait 1 second before the next frame
    
    # Recalculate the state of the matrix
    player_row = recalculate_matrix(matrix, player_row, player_col)

# 1%5
# 0.2
