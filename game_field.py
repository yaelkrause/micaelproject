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
        x = random.randint(LANDMINE_WIDTH, WINDOW_WIDTH - 3 * CELL_SIZE)
        y = random.randint(LANDMINE_HEIGHT, WINDOW_HEIGHT - CELL_SIZE)

        while True: #making sure they're not on one another
            x_locations = [location[0] for location in locations]
            y_locations = [location[1] for location in locations]

            for i in range(x, x+4):
                if i in x_locations:
                    x = random.randint(CELL_SIZE, WINDOW_WIDTH - 3 * CELL_SIZE)
                    y = random.randint(CELL_SIZE, WINDOW_HEIGHT - CELL_SIZE)
            if y in y_locations:
                x = random.randint(CELL_SIZE, WINDOW_WIDTH - 3 * CELL_SIZE)
                y = random.randint(CELL_SIZE, WINDOW_HEIGHT - CELL_SIZE)
            else:
                break

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