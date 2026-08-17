import pygame
from consts import *

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
    col = soldier["x"] // CELL_SIZE
    row = soldier["y"] // CELL_SIZE
    return [(row + 3, col), (row + 3, col + 1)]


def get_body_cells(soldier):
    col = soldier["x"] // CELL_SIZE
    row = soldier["y"] // CELL_SIZE
    return [(row, col), (row, col + 1), (row + 1, col), (row + 1, col + 1), (row + 2, col), (row + 2, col + 1)]


def check_collision(soldier_cells, game_grid, object_type):
    for row, col in soldier_cells:
        if 0 <= row < NUM_OF_ROWS and 0 <= col < NUM_OF_COLS:
            if game_grid[row][col] == object_type:
                return True
    return False