import pygame
import Screen
import UndergroundScreen
import game_field
import soldier
from consts import *


def main():
    pygame.init()

    game_grid = game_field.grid_create()
    knight = soldier.create_soldier()

    game_field.add_flag_to_grid()

    running = True
    show_mines = False
    mine_timer = 0
    clock = pygame.time.Clock()

    landmines_locations = []
    game_field.generate_locations(landmines_locations)
    game_field.add_objects_to_grid(landmines_locations)

    grass_locations = []
    game_field.generate_locations(grass_locations)

    Screen.draw_screen(grass_locations, knight)
    Screen.draw_welcome_message()
    Screen.draw_screen(grass_locations, knight)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not show_mines:
                    show_mines = True
                    mine_timer = pygame.time.get_ticks()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            soldier.move_soldier(knight, "UP")
        if keys[pygame.K_DOWN]:
            soldier.move_soldier(knight, "DOWN")
        if keys[pygame.K_LEFT]:
            soldier.move_soldier(knight, "LEFT")
        if keys[pygame.K_RIGHT]:
            soldier.move_soldier(knight, "RIGHT")

        if not show_mines:
            if soldier.check_collision(soldier.get_legs_cells(knight), game_field.game_grid, LANDMINE):
                Screen.draw_explosion(knight['x'], knight['y'] - 4*CELL_SIZE)
                Screen.draw_soldier(INJURED_SOLDIER, knight['x'], knight['y'])
                Screen.draw_win_lose_message("Game Over! You hit a landmine.")
                running = False

            elif soldier.check_collision(soldier.get_body_cells(knight), game_field.game_grid, FLAG):
                Screen.draw_win_lose_message("Victory! You reached the flag.")
                running = False

        if show_mines:
            UndergroundScreen.draw_underground_screen(landmines_locations, knight)

            if pygame.time.get_ticks() - mine_timer > 1000:
                show_mines = False
        else:
            Screen.draw_screen(grass_locations, knight)

        pygame.display.flip()

        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()