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
    This function initializes the Pygame module, sets up the game window, loads and displays the
    background image, renders the title and buttons on the screen, and runs the game loop until the
    player clicks the X button to exit the game.
    """
    pygame.init()
    # This is like a header in HTMl
    pygame.display.set_caption("Hangman (Daniel's CS50P Final Project)")
    # Set screen size and alow the screen to be resizable
    # (0, 0) means that the screen size will be set automatically
    screen: pygame.Surface = pygame.display.set_mode(
        (0, 0), pygame.RESIZABLE, pygame.FULLSCREEN
    )
    screen_width: int = screen.get_width()
    screen_height: int = screen.get_height()

    # Select the background image
    bg_image_path: str = "CS50P/Final Project/images/background_image.png"
    # Load the background image
    bg_image: pygame.Surface = pygame.image.load(bg_image_path)
    # Clean the screen. Make it completely white
    screen.fill((255, 255, 255))
    # Scale the background image to the size of the screen
    bg_image: pygame.Surface = pygame.transform.scale(
        bg_image, (screen_width, screen_height)
    )
    # Draw the background image.(0, 0) the image will render at the top left corner of the screen
    screen.blit(bg_image, (0, 0))

    # Render the title "HANGMAN"
    title_rect: pygame.Rect = start_screen.render_title(screen)
    # Render the buttons "Level 1", "Level 2", "Level 3", "Level 4"
    level_buttons_rect: pygame.Rect = start_screen.render_buttons(screen, title_rect)
    # Render the X button on the top right corner
    X_button_rect: pygame.Rect = start_screen.render_X_button(screen)
    # Game runs until 'is_playing' is set to False. aka click the red X button
    is_playing: bool = True

    # The Game loop. It will run until 'is_playing' is set to False. aka click the X button.
    while is_playing:
        for event in pygame.event.get():
            # Making pointing hand cursor when hovering over a button
            game_loop.mouse_when_over_button(X_button_rect, level_buttons_rect)
            # If the X button is clicked, the game will exit
            is_playing = game_loop.exit_game(X_button_rect, event)
            if is_playing is False:
                break

        # Updating the screen each time we change something
        pygame.display.flip()

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
