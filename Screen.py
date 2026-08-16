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


def draw_welcome_message():
    font = pygame.font.SysFont("Arial", 10)
    welcome_str = 'Welcome to The Flag Game!\nHave fun!'
    txt_surface = font.render(welcome_str, True, color=(0, 0, 0))
    screen.blit(txt_surface, (3*CELL_SIZE, 0))
    pygame.display.flip()
    pygame.time.delay(2000)

#edit
def draw_soldier():
    soldier = pygame.image.load(SOLDIER)
    sized_grass = pygame.transform.scale(soldier, (LANDMINE_WIDTH, LANDMINE_HEIGHT))
    grass_image_rect = sized_grass.get_rect(center=(CELL_SIZE, 2*CELL_SIZE))
    screen.blit(sized_grass, grass_image_rect)