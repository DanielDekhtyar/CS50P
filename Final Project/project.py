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
    The main function runs the Hangman game until the player chooses to exit.
    It initializes pygame
    Renders the initial start screen and runs and game loop
    """
    pygame.init()
    
    # This is like a header in HTMl
    pygame.display.set_caption("Hangman (Daniel's CS50P Final Project)")
    
    # Render the start screen with the background image and the title and buttons
    # Returns the buttons for later use in the game loop
    all_button_instances, X_button = start_screen.render_start_screen()

    # Game runs until 'is_playing' is set to False. aka click the red X button
    is_playing: bool = True

    # The Game loop. It will run until 'is_playing' is set to False. aka exit the game
    while is_playing:
        for event in pygame.event.get():
            # Making pointing hand cursor when hovering over a button
            game_loop.mouse_when_over_button(all_button_instances)
            
            # If the X button is clicked, the game will exit
            is_playing = game_loop.exit_game(X_button, event)
            if is_playing is False:
                break

        # Updating the screen each time we change something
        pygame.display.flip()

    print("Thank you for playing Hangman!")

    pygame.quit()
    sys.exit(0)


def level_setter(level: int):
    ...


def guess_letter(letter: chr, word):
    ...


def function_n():
    ...


if __name__ == "__main__":
    main()
