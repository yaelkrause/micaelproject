import pygame

import Screen
import UndergroundScreen
import game_field

def main():
    pygame.init()
    game_field.create()
    running = True

    # get landmines location
    landmines_locations = []
    game_field.generate_locations(landmines_locations)

    # get grass locations
    grass_locations = []
    game_field.generate_locations(grass_locations)

    while running:

        #create grid
        game_grid = game_field.game_grid
        game_field.create()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                UndergroundScreen.draw_underground_screen(landmines_locations)

        Screen.draw_screen(grass_locations)

    pygame.quit()

main()