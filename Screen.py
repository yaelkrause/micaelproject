from consts import *
import pygame
import random

screen = pygame.display.set_mode(
        (WINDOW_WIDTH, WINDOW_HEIGHT))

def draw_bush():
        bush_image = pygame.image.load(GRASS)
        bush_image = pygame.transform.scale(bush_image, (60, 20))

        for i in range(25):
                random_x=random.randint(0,WINDOW_WIDTH)
                random_y=random.randint(0,WINDOW_HEIGHT)
                bush_image_rect = bush_image.get_rect(
                        center=(random_x, random_y))
                screen.blit(bush_image, bush_image_rect)

def draw_game(game_state):
        screen.fill(FIELD_BACKGROUND_COLOR)