import random
from consts import *

game_grid = []

def create():
    global game_grid
    game_grid = [
        create_row(row, row_start=0, row_length=consts.BUBBLE_GRID_COLS)
        for row in
        range(consts.BUBBLE_GRID_START_ROWS)]

    # Create an empty row for future bubbles
    last_row = consts.BUBBLE_GRID_START_ROWS
    bubbles_grid.append(create_empty_row(last_row))

def generate_landmines():
    landmines_locations = []
    for mine in range(NUM_OF_LANDMINES):
        x = random.randint(WINDOW_WIDTH//2, WINDOW_WIDTH - 3*CELL_SIZE)
        y = random.randint(WINDOW_HEIGHT//2 - CELL_SIZE, WINDOW_HEIGHT)
        landmine_location = (x, y)
        while landmine_location in landmines_locations:
            landmines_locations.append(landmine_location)


def create_row(row_index, row_start, row_length):
    return [bush.create(bush.calc_center_x(col, row_index, row_start),
                          bush.calc_center_y(row_index),
                          random.choice(consts.bubble_colors)) for col in
            range(row_length)]
