import random
from consts import *

game_grid = []

def create():
    for row in range(NUM_OF_ROWS):
        grid_row = []
        for col in range(NUM_OF_COLS):
            grid_row.append('empty')
        game_grid.append(grid_row)

def generate_landmines():
    landmines_locations = []
    for mine in range(NUM_OF_LANDMINES):
        x = random.randint(WINDOW_WIDTH//2, WINDOW_WIDTH - 3*CELL_SIZE)
        y = random.randint(WINDOW_HEIGHT//2 - CELL_SIZE, WINDOW_HEIGHT)
        landmine_location = (x, y)
        while landmine_location in landmines_locations:
            landmines_locations.append(landmine_location)
    return landmines_locations

def calc_row(y):
    return y//CELL_SIZE

def calc_col(x):
    return x//CELL_SIZE

def add_landmines_to_grid(landmines_locations):
    for mine in landmines_locations:
        col = calc_col(mine[0])
        row = calc_row(mine[1])
