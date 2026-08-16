from consts import *
import pygame

screen = pygame.display.set_mode(
        (WINDOW_WIDTH, WINDOW_HEIGHT))

def draw_game(game_state):
        screen.fill(FIELD_BACKGROUND_COLOR)