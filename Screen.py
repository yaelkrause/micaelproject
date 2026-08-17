from consts import *
import pygame


clock = pygame.time.Clock()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


def draw_screen(locations, knight):
    screen.fill(FIELD_BACKGROUND_COLOR)

    grass = pygame.image.load(GRASS)
    sized_grass = pygame.transform.scale(grass, (LANDMINE_WIDTH, LANDMINE_HEIGHT))
    for grass in locations:
        grass_image_rect = sized_grass.get_rect(topleft=(grass[0], grass[1]))
        screen.blit(sized_grass, grass_image_rect)

    draw_soldier(SOLDIER, knight['x'], knight['y'])

    pygame.display.flip()
    clock.tick(30)


def draw_welcome_message():
    font = pygame.font.SysFont("Arial", 10)
    welcome_str = 'Welcome to The Flag Game!\nHave fun!'
    txt_surface = font.render(welcome_str, True, color=(0, 0, 0))
    screen.blit(txt_surface, (3*CELL_SIZE, 0))
    pygame.display.flip()
    pygame.time.delay(3000)


def draw_soldier(img, x, y):
    knight = pygame.image.load(img)
    sized_knight = pygame.transform.scale(knight, (SOLDIER_WIDTH, SOLDIER_HEIGHT))
    knight_image_rect = sized_knight.get_rect(topleft=(x, y))
    screen.blit(sized_knight, knight_image_rect)


def add_flag_to_grid(game_grid):
    start_row = NUM_OF_ROWS - 3
    start_col = NUM_OF_COLS - 4
    for r in range(start_row, NUM_OF_ROWS):
        for c in range(start_col, NUM_OF_COLS):
            game_grid[r][c] = FLAG