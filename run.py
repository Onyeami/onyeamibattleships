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
        # Ensure not to place a ship on top of another
        while grid[ship_row][ship_col] == 's':
            ship_row = random.randint(0, size - 1)
            ship_col = random.randint(0, size - 1)
        grid[ship_row][ship_col] = 's'  # Place the ship


# Function to check if a guess is within the grid boundaries
def is_valid_guess(guess, size):
    row, col = guess
    return row >= 0 and row < size and col >= 0 and col < size


# Function to check if a guess hits a ship
def is_hit(guess, grid):
    row, col = guess
    return grid[row][col] == 's'


# Function for the computer's turn to guess
def computer_guess(size, guessed_cells):
    while True:
        guess_row = random.randint(0, size-1)
        guess_col = random.randint(0, size-1)
        guess = (guess_row, guess_col)
        if guess not in guessed_cells:
            return guess


# Function to check if a computer hits a ship
def check_ship_hit(guess, grid):
    row, col = guess
    return grid[row][col] == 's'


# Function to play the game
def play_game(size, num_ships, level, time_limit):
    size = get_user_input(
        "Enter the grid size: ", type_=int, min_=1
    )
    num_ships = get_user_input(
        "Enter the number of ships: ",  type_=int, min_=1, max_=size * size
    )
    player_score = 0  # Initialize player's score
    computer_score = 0  # Initialize computer's score
    player_grid = create_grid(size)  # Create the player's game grid
    computer_grid = create_grid(size)  # Create the computer's game grid
    place_ships(player_grid, num_ships)  # Place the player's ships
    place_ships(computer_grid, num_ships)  # Place the computer's ships
    print("Welcome to Onyeami's Battleships game!")  # Welcome message
    print("Try to sink all the ships.")  # Game instructions
    print("Your grid:")
    print_grid(player_grid)  # Print the initial game state
    turns = 0  # Initialize turn counter
    player_guessed_cells = set()  # Keep track of player's guessed cells
    computer_guessed_cells = set()  # Keep track of computer's guessed cells
    player_hits = 0
    player_misses = 0
    computer_hits = 0
    computer_misses = 0
    player_ships = num_ships
    computer_ships = num_ships
    game_history = []
    in_game_menu = False  # Flag to indicate whether in-game menu is active

    while True:  # Game loop
        if not in_game_menu:
            # Player's turn
            print("Player's turn:")
            start_time = time.time()
            guess = input(
                "Enter your guess(e.g., A1)
                or type 'status' to check the current status: "
            ).upper()

            if guess == 'STATUS':
                display_game_status(
                    player_hits, player_misses, player_ships, computer_hits,
                    computer_misses, computer_ships
                )
                continue

            guess_col = ord(guess[0]) - ord('A')
            guess_row = int(guess[1:]) - 1
            guess_coords = (guess_row, guess_col)

            if not is_valid_guess(guess_coords, size):
                print("Invalid guess. Try again.")
                continue

            elapsed_time = time.time() - start_time

            if elapsed_time > time_limit:
                print("Time's up! It's the computer's turn now.")
            else:
                if guess_coords in player_guessed_cells:
                    print("You already guessed that cell. Try again.")
                    continue

                player_guessed_cells.add(guess_coords)
                game_history.append(("Player", guess_coords))

                if is_hit(guess_coords, computer_grid):
                    print("You hit a ship!")
                    player_score += 1
                    player_hits += 1
                    computer_ships -= 1
                    computer_grid[guess_row][guess_col] = 'x'
