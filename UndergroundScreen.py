import pygame
from consts import *

screen = pygame.display.set_mode(
        (WINDOW_WIDTH, WINDOW_HEIGHT))


def calc_y(row):
    return row * CELL_SIZE


def calc_x(col):
    return col * CELL_SIZE


def draw_underground_screen():
    screen.fill(UNDERGROUND_BACKGROUND_COLOR)

    for row in range(NUM_OF_ROWS):
        pygame.draw.line(screen, UNDERGROUND_GRID_COLOR, start_pos=(0, calc_y(row)),
                         end_pos=(WINDOW_WIDTH, calc_y(row)))

    for col in range(NUM_OF_COLS):
            pygame.draw.line(screen, UNDERGROUND_GRID_COLOR, start_pos=(calc_x(col), 0),
                             end_pos=(calc_x(col), WINDOW_HEIGHT))

    pygame.display.flip()
    pygame.time.wait(1000)

draw_underground_screen()
pygame.quit()