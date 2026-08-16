from consts import *
import pygame


clock = pygame.time.Clock()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


def draw_screen(locations):
    screen.fill(FIELD_BACKGROUND_COLOR)

    grass = pygame.image.load(GRASS)
    sized_grass = pygame.transform.scale(grass, (LANDMINE_WIDTH, LANDMINE_HEIGHT))
    for grass in locations:
        grass_image_rect = sized_grass.get_rect(center=(grass[0], grass[1]))
        screen.blit(sized_grass, grass_image_rect)

    pygame.display.flip()
    clock.tick(30)
