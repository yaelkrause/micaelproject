import pygame

import Screen
import UndergroundScreen
import game_field
import soldier

def main():
    pygame.init()

    game_grid = game_field.grid_create()

    running = True

    # get landmines location
    landmines_locations = []
    game_field.generate_locations(landmines_locations)
    game_field.add_objects_to_grid(landmines_locations)

    # get grass locations
    grass_locations = []
    game_field.generate_locations(grass_locations)

    Screen.draw_screen(grass_locations)

    # print welcome mess
    Screen.draw_welcome_message()

    Screen.draw_screen(grass_locations)

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                UndergroundScreen.draw_underground_screen(landmines_locations)

            dr, dc = 0, 0

            if event.key == pygame.K_UP:
                dr = -1
            elif event.key == pygame.K_DOWN:
                dr = 1
            elif event.key == pygame.K_LEFT:
                dc = -1
            elif event.key == pygame.K_RIGHT:
                dc = 1


        pygame.display.flip()

    pygame.quit()

main()