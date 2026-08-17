from consts import *
import pygame


screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


def draw_screen(locations, knight, img):
    screen.fill(FIELD_BACKGROUND_COLOR)

    grass = pygame.image.load(GRASS)
    sized_grass = pygame.transform.scale(grass, (BUSH_WIDTH, LANDMINE_HEIGHT))
    for grass in locations:
        grass_image_rect = sized_grass.get_rect(topleft=(grass[0], grass[1]))
        screen.blit(sized_grass, grass_image_rect)

    draw_flag(FLAG_IMAGE, (NUM_OF_COLS - 4) * CELL_SIZE, (NUM_OF_ROWS - 3.5) * CELL_SIZE)
    draw_soldier(img, knight['x'], knight['y'])

    pygame.display.flip()


def draw_welcome_message():
    font = pygame.font.SysFont('vivaldi', 30)
    welcome_str = 'Welcome to The Flag Game!\nHave fun!'
    txt_surface = font.render(welcome_str, True, color=(255, 255, 255))
    screen.blit(txt_surface, (3*CELL_SIZE, CELL_SIZE/2))
    pygame.display.flip()
    pygame.time.delay(3000)


def draw_soldier(img, x, y):
    knight = pygame.image.load(img)
    sized_knight = pygame.transform.scale(knight, (SOLDIER_WIDTH, SOLDIER_HEIGHT))
    knight_image_rect = sized_knight.get_rect(topleft=(x, y))
    screen.blit(sized_knight, knight_image_rect)


def draw_flag(img, x, y):
    flag = pygame.image.load(img)
    sized_flag = pygame.transform.scale(flag, (4 * CELL_SIZE, 3 * CELL_SIZE))
    flag_image_rect = sized_flag.get_rect(topleft=(x, y))
    screen.blit(sized_flag, flag_image_rect)


def add_flag_to_grid(game_grid):
    start_row = NUM_OF_ROWS - 3
    start_col = NUM_OF_COLS - 4
    for r in range(start_row, NUM_OF_ROWS):
        for c in range(start_col, NUM_OF_COLS):
            game_grid[r][c] = FLAG


def draw_explosion(x, y):
    explosion = pygame.image.load(EXPLOSION)
    sized_explosion = pygame.transform.scale(explosion, (SOLDIER_WIDTH, LANDMINE_HEIGHT))
    explosion_image_rect = sized_explosion.get_rect(bottomleft=(x, y))
    screen.blit(sized_explosion, explosion_image_rect)


def draw_win_lose_message(string, dest, font, size):
    font = pygame.font.SysFont(font, size)
    txt_surface = font.render(string, True, color=(255, 255, 255))
    screen.blit(txt_surface, dest)
    pygame.display.flip()
    pygame.time.delay(3000)