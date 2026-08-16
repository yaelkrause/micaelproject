import pygame
import Screen
import UndergroundScreen
import game_field
import soldier


def main():
    pygame.init()

    game_grid = game_field.grid_create()
    knight_grid = soldier.create_knight_grid()

    running = True

    # get landmines location
    landmines_locations = []
    game_field.generate_locations(landmines_locations)
    game_field.add_objects_to_grid(landmines_locations)

    # get grass locations
    grass_locations = []
    game_field.generate_locations(grass_locations)

    # print welcome mess
    Screen.draw_screen(grass_locations, knight_grid)
    Screen.draw_welcome_message()

    Screen.draw_screen(grass_locations, knight_grid)

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                UndergroundScreen.draw_underground_screen(landmines_locations, knight_grid)
                Screen.draw_screen(grass_locations, knight_grid)

            if pygame.key == pygame.K_UP:
                knight_grid = soldier.up(knight_grid)
            elif pygame.key == pygame.K_DOWN:
                knight_grid = soldier.down(knight_grid)
            elif pygame.key == pygame.K_LEFT:
                knight_grid = soldier.left(knight_grid)
            elif pygame.key == pygame.K_RIGHT:
                knight_grid = soldier.right(knight_grid)

        pygame.display.flip()

    pygame.quit()

main()