import random
from consts import *


game_grid = []


def grid_create():
    for row1 in range(NUM_OF_ROWS):
        grid_row = []

        for col1 in range(NUM_OF_COLS):
            grid_row.append(EMPTY)

        game_grid.append(grid_row)


def generate_locations(locations):
    for mine in range(NUM_OF_LANDMINES):
        x = random.randint(CELL_SIZE, WINDOW_WIDTH - 3 * CELL_SIZE)
        y = random.randint(CELL_SIZE, WINDOW_HEIGHT - CELL_SIZE)
        location = (x, y)

        while location in locations:
            x = random.randint(CELL_SIZE, WINDOW_WIDTH - 3 * CELL_SIZE)
            y = random.randint(CELL_SIZE, WINDOW_HEIGHT - CELL_SIZE)
            location = (x, y)

        locations.append(location)

    return locations


def calc_row(y):
    return y//CELL_SIZE


def calc_col(x):
    return x//CELL_SIZE


def add_objects_to_grid(locations):
    for mine in locations:
        col1 = calc_col(mine[0])
        row1 = calc_row(mine[1])
        for i in range(col1, col1+3):
            game_grid[row1][i] = LANDMINE