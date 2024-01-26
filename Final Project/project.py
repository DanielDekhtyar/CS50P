"""
Learning Python with CS50
Final Project !!!
https://cs50.harvard.edu/python/2022/project/


Author : Daniel Dekhtyar
Email : denik2707@gmail.com
LinkedIn : https://www.linkedin.com/in/daniel-dekhtyar/
GitHub : https://github.com/DanielDekhtyar
"""

from typing import Tuple

import pygame
from utils.resource_path import resource_path
from src import start_screen
from src import game_loop
from src import hangman_game
from utils import util_functions
from classes.word import Word
from classes.button import Button


def main(screen: pygame.Surface, is_playing: bool) -> bool:
    """
    The main function controls the flow of the game by rendering the start screen, handling button
    clicks, and calling the hangman game logic.

    Args:
    screen: The screen parameter is the Pygame surface object that represents the game window. It is
    used to render and update the game graphics.
    is_playing: A boolean variable that indicates whether the game is currently being played or not.

    Returns:
    the value of the variable "is_playing", which is a boolean value.
    """
    # Render the main screen of the game where you can choose the level
    all_button_instances, exit_button = start_screen.render_start_screen(screen)

    # The main game loop. If is_playing is False the game will quit.
    while is_playing:
        # Get the current mouse position
        mouse_pos: list[int, int, int] = pygame.mouse.get_pos()

        # Check if the mouse hovers over any of the buttons.
        # If so the mouse pointer will be set to a pointy hand
        game_loop.mouse_when_over_button(all_button_instances, mouse_pos)

        # Get the button.name of the button that was clicked.
        # If no button was clicked, None will be returned
        button_name: str = util_functions.button_clicked(
            all_button_instances, mouse_pos
        )

        # A set of the button.names of the level buttons.
        # On the screen you will see them as Easy, Medium, Hard, Very Hard
        level_names: dict[str] = {"Level 1", "Level 2", "Level 3", "Level 4"}

        """
        If one of the level buttons is clicked, the game will start the level.
        When the exit button on the game screen is clicked, game_logic will return False,
        The game loop will stop and the game will exit

        The If Else statement is written in the way that it does because otherwise
        you need to click the exit button twice to exit the game.
        One time to exit the game_logic loop and the second time to exit the main game loop.
        """
        # ^^^^^ For explanation of the IF statement read the docstring above ^^^^^
        if button_name in level_names:
            # Start the level and move to the game screen
            is_playing = hangman_game.game_logic(screen, button_name, all_button_instances)

        for event in pygame.event.get():
            is_playing = game_loop.exit_game(exit_button, event, mouse_pos)

        pygame.display.update()

    is_playing = False
    return is_playing


def is_letter_guessed(word: Word, button: Button):
    """
    The function checks if a letter guessed by the player is present in the word and updates the
    guessed_letters_index accordingly.

    Args:
    word (Word): The parameter "word" is of type "Word", which is likely a custom class representing a
    word in a game or some other context. It probably has properties like "word" (the actual word), and
    "guessed_letters_index" (a list or array indicating which letters have been guessed correctly
    button (Button): The `button` parameter is an object of the `Button` class. It represents the
    button that was clicked or pressed by the user.

    Returns:
    a boolean value indicating whether the guessed letter is present in the word.
    """
    # Initialize to False initially
    is_guessed = False

    for i, char in enumerate(word.word):
        # If the letter that was guessed is in the word, change the guessed_letters_index to True
        if char == button.name:
            # Make the letter visible in the masked word
            word.guessed_letters_index[i] = True
            is_guessed = True

    return is_guessed


# Make restart and exit buttons clickable
def make_restart_and_exit_clickable(all_button_instances: list[Button]):
    """
    The function makes the "Restart" and "Exit" buttons clickable by setting their clickable attribute
    to True.

    Args:
    all_button_instances (list[Button]): A list of Button instances.
    """
    for button in all_button_instances:
        if button.name == "Restart" or button.name == "Exit":
            button.clickable = True


def make_all_main_screen_button_unclickable(all_button_instances: list[pygame.Rect]) -> None:
    """
    The function makes all the buttons from the main screen unclickable.

    Args:
    all_button_instances (list[pygame.Rect]): A list of instances of the pygame.Rect class
    representing all the buttons on the main screen.
    """
    # Make all the buttons from the main screen unclickable
    for button in all_button_instances:
        button.clickable = False


if __name__ == "__main__":
    """
    Initializes the Pygame library, sets the caption for the game window, creates a resizable
    game window, and starts the game loop.

    Inputs: The game starts running from here
    Outputs: The game exits here when is_playing is set to False.
    """

    # Initialize pygame
    pygame.init()

    # Initialize pygame playing sound
    pygame.mixer.init()
    # This is like a header in HTMl
    pygame.display.set_caption("Hangman (Daniel's CS50P Final Project)")

    # Set screen size and alow the screen to be resizable
    # (0, 0) means that the screen size will be set automatically
    screen: pygame.Surface = pygame.display.set_mode((0, 0), pygame.RESIZABLE)

    # A boolean variable that tracks if the game is still playing
    # When is_playing is set to False, the game will exit
    is_playing = True

    while is_playing:
        is_playing = main(screen, is_playing)

    # Exit the game
    print("Thank you for playing Hangman!")
    pygame.quit()
