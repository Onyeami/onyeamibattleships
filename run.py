# Import the random module to generate random numbers
import random
import time


# Function to create a grid of given size filled with 'o'
def create_grid(size):
    return [['o'] * size for _ in range(size)]


# Function to print the grid in a nice format
def print_grid(grid):
    size = len(grid)
    # Print column headers (A, B, C, ...)
    print("   " + " ".join([chr(65+i) for i in range(size)]))
    for i in range(size):
        # Print each row with row number
        print(str(i+1).rjust(2) + "|" + " ".join(grid[i]) + "|")
        print("-" * (2*size+5))  # Print line separator


# Function to place a given number of ships ('s') randomly in the grid
def place_ships(grid, num_ships):
    size = len(grid)
    max_ships = size * size - 2  # Maximum number of ships allowed

    if num_ships > max_ships:
        print("Invalid number of ships! Maximum allowed ships:", max_ships)
        return

    for _ in range(num_ships):
        ship_row = random.randint(0, size - 1)
        ship_col = random.randint(0, size - 1)
        while grid[ship_row][ship_col] == 's':
            ship_row = random.randint(0, size - 1)
            ship_col = random.randint(0, size - 1)
        grid[ship_row][ship_col] = 's'
