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
    '''show_mines = False
    mine_timer = 0'''

    #get landmine location
    landmines_locations = []
    game_field.generate_locations(landmines_locations)
    game_field.add_objects_to_grid(landmines_locations)

    #get grass location
    grass_locations = []
    game_field.generate_locations(grass_locations)

    #draw welcome screen
    Screen.draw_screen(grass_locations, knight)
    Screen.draw_welcome_message()

    Screen.draw_screen(grass_locations, knight)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                UndergroundScreen.draw_underground_screen(landmines_locations, knight)
                Screen.draw_screen(grass_locations, knight)

            key_pressed = pygame.key.get_just_pressed()
            if key_pressed[pygame.K_UP]:
                soldier.move_soldier(knight, "UP")
            elif key_pressed[pygame.K_DOWN]:
                soldier.move_soldier(knight, "DOWN")
            elif key_pressed[pygame.K_LEFT]:
                soldier.move_soldier(knight, "LEFT")
            elif key_pressed[pygame.K_RIGHT]:
                soldier.move_soldier(knight, "RIGHT")

        '''if not show_mines:'''
        if soldier.check_collision(soldier.get_legs_cells(knight), game_field.game_grid, LANDMINE):
            print("Game Over! You hit a landmine.")
            pygame.time.delay(3000)
            running = False

        elif soldier.check_collision(soldier.get_body_cells(knight), game_field.game_grid, FLAG):
            print("Victory! You reached the flag.")
            pygame.time.delay(3000)
            running = False

        '''if show_mines:
            UndergroundScreen.draw_underground_screen(landmines_locations, knight)
            if pygame.time.get_ticks() - mine_timer > 1000:
                show_mines = False
        else:'''
        pygame.display.flip()

    pygame.quit()




if __name__ == "__main__":
    main()