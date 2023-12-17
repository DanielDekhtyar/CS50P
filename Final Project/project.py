# Learning Python with CS50
# Final Project !!!
# https://cs50.harvard.edu/python/2022/project/

"""
Author : Daniel Dekhtyar
Email : denik2707@gmail.com
LinkedIn : https://www.linkedin.com/in/daniel-dekhtyar/
GitHub : https://github.com/DanielDekhtyar
"""


import sys
import pygame

from src import start_screen, game_loop


def main():
    """
    The main function initializes PyGame, sets the window title, 
    renders the start screen, and runs the main game loop until 
    the user clicks the exit button.

    It handles initializing PyGame, displaying the start screen, 
    tracking game state, and cleaning up when the game exits.
    """
    pygame.init()

    # This is like a header in HTMl
    pygame.display.set_caption("Hangman (Daniel's CS50P Final Project)")

    # Render the start screen with the background image and the title and buttons
    # Returns the buttons for later use in the game loop
    all_button_instances, exit_button = start_screen.render_start_screen()

    # Game runs until 'is_playing' is set to False. aka click the red X button
    is_playing: bool = True

    # The Game loop. It will run until 'is_playing' is set to False. aka exit the game
    while is_playing:
        for event in pygame.event.get():
            """
            Mouse position determined at the start of the game loop to save computer resources.
            Otherwise the pygame.mouse.get_pos() function would be called in every function.
            """
            mouse_pos: tuple[int, int]  = pygame.mouse.get_pos()
            
            # Making pointing hand cursor when hovering over a button
            game_loop.mouse_when_over_button(all_button_instances, mouse_pos)

            # If the X button is clicked, the game will exit
            is_playing = game_loop.exit_game(exit_button, event, mouse_pos)
            if is_playing is False:
                break

        # Updating the screen each time we change something
        pygame.display.flip()

    print("Thank you for playing Hangman!")

    pygame.quit()
    sys.exit(0)


def level_selection(all_button_instances: list[pygame.Rect], mouse_pos) -> int:
    # Get the position of the mouse
    mouse_x, mouse_y = mouse_pos
    
    # Iterate over all the buttons and check if the mouse is over any of them
    for button in all_button_instances:
        # Check if mouse is over the button and if the button is active
        if button.collidepoint(mouse_x, mouse_y) and button.is_clickable():
            ...


def guess_letter(letter: chr, word):
    ...


def function_n():
    ...


if __name__ == "__main__":
    main()
