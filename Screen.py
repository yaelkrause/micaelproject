from consts import *
import pygame
import random

booly = False
screen = pygame.display.set_mode(
        (WINDOW_WIDTH, WINDOW_HEIGHT))

def generate_bush():
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

def add_bushes_to_screen(bush_locations, bush_img):
        for place in bush_locations:
                bush_image_rect = bush_img.get_rect(
                        center=(place[0], place[1]))
                screen.blit(bush_img, bush_image_rect)

def bush_img_create():
        bush_image = pygame.image.load(GRASS)
        bush_image = pygame.transform.scale(bush_image, (LANDMINE_WIDTH, LANDMINE_HEIGHT))
        return bush_image

def draw_game_field(screen):
        if not booly:
                screen.fill(FIELD_BACKGROUND_COLOR)
                bush_locations= generate_bush()
                global field_screen
                field_screen= create_field()
                field_screen=add_bushes_to_grid(bush_locations)
                bush_img= bush_img_create()
                add_bushes_to_screen(bush_locations, bush_img)
                pygame.display.flip()
                booly = True
        else:
                screen.fill(FIELD_BACKGROUND_COLOR)
                add_bushes_to_screen(bush_locations, bush_img)
                pygame.display.flip()

