from consts import *
import pygame
import random

screen = pygame.display.set_mode(
        (WINDOW_WIDTH, WINDOW_HEIGHT))

def generate_bush(field_screen):
    bush_locations = []

    for bush in range(NUM_OF_LANDMINES):
        x = random.randint(1, WINDOW_WIDTH)
        y = random.randint(CELL_SIZE, WINDOW_HEIGHT)
        bush_location = (x, y)

        while bush_location in bush_locations:
            x = random.randint(1, WINDOW_WIDTH - 3 * CELL_SIZE)
            y = random.randint(CELL_SIZE, WINDOW_HEIGHT)
            bush_location = (x, y)

        bush_locations.append(bush_location)

    return bush_locations

def add_bushes_to_grid(bush_locations):
    for bush in bush_locations:
        col1 = calc_col(bush[0])
        row1 = calc_row(bush[1])
        for i in range(col1, col1+1):
            field_screen[row1][i] = BUSH
        return field_screen

def calc_row(y):
    return y//CELL_SIZE


def calc_col(x):
    return x//CELL_SIZE

def create_field():
        return [[EMPTY for i in range(NUM_OF_COLS)] for j in range(NUM_OF_ROWS)]

def add_bushes(bush_locations):

def draw_game(screen):
        screen.fill(FIELD_BACKGROUND_COLOR)
        pygame.display.flip()
        global field_screen
        field_screen= create_field()
        field_screen=generate_bush(field_screen)

bubble_image = pygame.image.load(bubble["image"])
    bubble_image = pygame.transform.scale(bubble_image, (consts.BUBBLE_WIDTH, consts.BUBBLE_HEIGHT))
    bubble_image_rect = bubble_image.get_rect(
            center=(bubble["center_x"], bubble["center_y"]))
    screen.blit(bubble_image, bubble_image_rect)