# Import the random module to generate random numbers
import random
import time


# Function to create a grid of given size filled with 'o'
def create_grid(size):
    return [['o'] * size for _ in range(size)]
