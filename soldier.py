from consts import *
import game_field

def create_soldier():
    return {
        "x": 0,
        "y": 0,
        "width_in_cells": 2,
        "height_in_cells": 4,
        "width": 2 * CELL_SIZE,
        "height": 4 * CELL_SIZE,
        "speed": CELL_SIZE
    }


def move_soldier(soldier, direction):
    if direction == "UP" and soldier["y"] > 0:
        soldier["y"] -= soldier["speed"]
    elif direction == "DOWN" and soldier["y"] < WINDOW_HEIGHT - soldier["height"]:
        soldier["y"] += soldier["speed"]
    elif direction == "LEFT" and soldier["x"] > 0:
        soldier["x"] -= soldier["speed"]
    elif direction == "RIGHT" and soldier["x"] < WINDOW_WIDTH - soldier["width"]:
        soldier["x"] += soldier["speed"]
    return soldier


def get_legs_cells(soldier):
    col = game_field.calc_col(soldier['x'])
    row = game_field.calc_row(soldier['y'])
    return [(row + 4, col), (row + 4, col + 1)]


def get_body_cells(soldier):
    col = game_field.calc_col(soldier['x'])
    row = game_field.calc_row(soldier['y'])
    return [(row + 1, col), (row + 1, col + 1), (row + 2, col), (row + 2, col + 1), (row + 3, col), (row + 3, col + 1)]


def check_collision(soldier_cells, game_grid, object_type):
    for tup in soldier_cells:
        if game_grid[tup[0]][tup[1]] == object_type:
            return True
    return False