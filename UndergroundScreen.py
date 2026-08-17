from consts import *
import pygame
import Screen

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


def calc_y(row):
    return row * CELL_SIZE


def calc_x(col):
    return col * CELL_SIZE


def draw_underground_screen(landmines_locations, knight):
    screen.fill(UNDERGROUND_BACKGROUND_COLOR)

    for row in range(NUM_OF_ROWS):
        pygame.draw.line(screen, UNDERGROUND_GRID_COLOR, start_pos=(0, calc_y(row)),
                         end_pos=(WINDOW_WIDTH, calc_y(row)))

    for col in range(NUM_OF_COLS):
        pygame.draw.line(screen, UNDERGROUND_GRID_COLOR, start_pos=(calc_x(col), 0),
                         end_pos=(calc_x(col), WINDOW_HEIGHT))

    landmine = pygame.image.load(LANDMINE_IMAGE)
    sized_landmine = pygame.transform.scale(landmine, (LANDMINE_WIDTH, LANDMINE_HEIGHT))
    for mine in landmines_locations:
        # Align landmine drawing correctly based on its position
        landmine_image_rect = sized_landmine.get_rect(bottomleft=(mine[0], mine[1]))
        screen.blit(sized_landmine, landmine_image_rect)

    # Draw soldier on underground screen using night skin
    Screen.draw_soldier(UNDERGROUND_SOLDIER, knight["x"], knight["y"])

    pygame.display.flip()