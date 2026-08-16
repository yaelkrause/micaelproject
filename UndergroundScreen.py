import pygame
from consts import *

screen = pygame.display.set_mode(
        (WINDOW_WIDTH, WINDOW_HEIGHT))

def draw_screen():
    screen.fill(UNDERGROUND_BACKGROUND_COLOR)
    for row in range(NUM_OF_ROWS):
        pygame.draw.line(screen, consts.BORDER_COLOR, start_pos=(0, ), end_pos=(consts.WINDOW_WIDTH, line_y))