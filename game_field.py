import random
from consts import *

game_grid = []

def create():
    global game_grid



def generate_landmines():
    landmines_locations = []
    for mine in range(NUM_OF_LANDMINES):
        x = random.randint(WINDOW_WIDTH//2, WINDOW_WIDTH - 3*CELL_SIZE)
        y = random.randint(WINDOW_HEIGHT//2 - CELL_SIZE, WINDOW_HEIGHT)
        landmine_location = (x, y)
        while landmine_location in landmines_locations:
            landmines_locations.append(landmine_location)
