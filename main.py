import pygame

import UndergroundScreen
import game_field

def main():
    pygame.init()
    game_field.create()
    running = True
    underground_screen = UndergroundScreen.screen

    while running:

        #create grid
        game_grid = game_field.game_grid
        game_field.create()

        #get landmines location
        landmines_locations = game_field.landmines_locations()
        game_field.generate_landmines()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                UndergroundScreen.draw_underground_screen(landmines_locations)
main()