'''import soldier'''
from consts import *
import pygame


clock = pygame.time.Clock()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


def draw_screen(locations, knight):
    screen.fill(FIELD_BACKGROUND_COLOR)

    grass = pygame.image.load(GRASS)
    sized_grass = pygame.transform.scale(grass, (LANDMINE_WIDTH, LANDMINE_HEIGHT))
    for grass in locations:
        grass_image_rect = sized_grass.get_rect(center=(grass[0], grass[1]))
        screen.blit(sized_grass, grass_image_rect)

    '''soldier.get_knight_pos(knight)
    draw_soldier(SOLDIER, knight[0], knight[1])'''

    pygame.display.flip()
    clock.tick(30)


def draw_welcome_message():
    font = pygame.font.SysFont("Arial", 10)
    welcome_str = 'Welcome to The Flag Game!\nHave fun!'
    txt_surface = font.render(welcome_str, True, color=(0, 0, 0))
    screen.blit(txt_surface, (3*CELL_SIZE, 0))
    pygame.display.flip()
    pygame.time.delay(2000)


def draw_soldier(img, x, y):
    knight = pygame.image.load(img)
    sized_knight = pygame.transform.scale(knight, (SOLDIER_WIDTH, SOLDIER_HEIGHT))
    knight_image_rect = sized_knight.get_rect(center=(x + CELL_SIZE, y + 2*CELL_SIZE))
    screen.blit(sized_knight, knight_image_rect)