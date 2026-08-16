import random
from consts import *

game_grid = []
landmines_locations = []


def create():
    for row1 in range(NUM_OF_ROWS):
        grid_row = []

        for col1 in range(NUM_OF_COLS):
            grid_row.append(EMPTY)

        game_grid.append(grid_row)


def generate_landmines():
    for mine in range(NUM_OF_LANDMINES):
        x = random.randint(1, WINDOW_WIDTH - 3 * CELL_SIZE)
        y = random.randint(CELL_SIZE, WINDOW_HEIGHT)
        landmine_location = (x, y)

        while landmine_location in landmines_locations:
            x = random.randint(1, WINDOW_WIDTH - 3 * CELL_SIZE)
            y = random.randint(CELL_SIZE, WINDOW_HEIGHT)
            landmine_location = (x, y)

        landmines_locations.append(landmine_location)


def calc_row(y):
    return y//CELL_SIZE


def calc_col(x):
    return x//CELL_SIZE


def add_landmines_to_grid():
    for mine in landmines_locations:
        col1 = calc_col(mine[0])
        row1 = calc_row(mine[1])
        for i in range(col1, col1+3):
            game_grid[row1][i] = LANDMINE


create()
add_landmines_to_grid()


for row in range(len(game_grid)):
    for col in range(len(game_grid[row])):
        if col != len(game_grid[row])-1:
            print(game_grid[row][col], end=' ')
        else:
            print(game_grid[row][col])
