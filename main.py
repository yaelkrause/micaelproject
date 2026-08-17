import pygame
import Screen
import UndergroundScreen
import game_field
import soldier
from consts import *


def main():
    # Initialize Pygame
    pygame.init()

    # Create the game grid and the soldier dictionary state
    game_grid = game_field.grid_create()
    knight = soldier.create_soldier()

    running = True
    show_mines = False
    mine_timer = 0

    # Initialize landmine locations and add them to the grid
    landmines_locations = []
    game_field.generate_locations(landmines_locations)
    game_field.add_objects_to_grid(landmines_locations)

    # Initialize grass locations for the background
    grass_locations = []
    game_field.generate_locations(grass_locations)

    # Draw the initial screen and the welcome message
    Screen.draw_screen(grass_locations, knight)
    Screen.draw_welcome_message()

    while running:
        # 1. Handle user events and inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                # Reveal landmines when Enter is pressed
                if event.key == pygame.K_RETURN:
                    show_mines = True
                    mine_timer = pygame.time.get_ticks()

                # Move soldier using arrow keys
                elif event.key == pygame.K_UP:
                    soldier.move_soldier(knight, "UP")
                elif event.key == pygame.K_DOWN:
                    soldier.move_soldier(knight, "DOWN")
                elif event.key == pygame.K_LEFT:
                    soldier.move_soldier(knight, "LEFT")
                elif event.key == pygame.K_RIGHT:
                    soldier.move_soldier(knight, "RIGHT")

        # 2. Game logic (behind the scenes)
        # Check if the soldier's legs hit a landmine
        if soldier.check_collision(soldier.get_legs_cells(knight), game_field.game_grid, LANDMINE):
            print("Game Over! You hit a landmine.")
            running = False  # Can be replaced with a game over screen call

        # Check if the soldier's body reached the flag
        if soldier.check_collision(soldier.get_body_cells(knight), game_field.game_grid, FLAG):
            print("Victory! You reached the flag.")
            running = False  # Can be replaced with a victory screen call

        # 3. Draw the appropriate screen based on current state
        if show_mines:
            UndergroundScreen.draw_underground_screen(landmines_locations, knight)
            # Hide mines after exactly one second (1000 milliseconds)
            if pygame.time.get_ticks() - mine_timer > 1000:
                show_mines = False
        else:
            Screen.draw_screen(grass_locations, knight)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()