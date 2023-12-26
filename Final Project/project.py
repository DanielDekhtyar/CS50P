"""
Learning Python with CS50
Final Project !!!
https://cs50.harvard.edu/python/2022/project/


Author : Daniel Dekhtyar
Email : denik2707@gmail.com
LinkedIn : https://www.linkedin.com/in/daniel-dekhtyar/
GitHub : https://github.com/DanielDekhtyar
"""


import pygame

from src import start_screen
from src import game_loop
from src import hangman_game


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

    # Set screen size and alow the screen to be resizable
    # (0, 0) means that the screen size will be set automatically
    screen: pygame.Surface = pygame.display.set_mode((0, 0), pygame.RESIZABLE)

    # Render the start screen with the background image and the title and buttons
    # Returns the buttons for later use in the game loop
    # HACK: make it return just the button list without the exit button separately using return_button_clicked
    all_button_instances, exit_button = start_screen.render_start_screen(screen)

    # The Game loop. It will run until 'is_playing' is set to False. aka exit the game
    is_playing: bool = True

    # The main game loop
    while is_playing:
        # Mouse position determined at the start of the game loop to save computer resources.
        # Otherwise, the pygame.mouse.get_pos() function would be called in every function.
        mouse_pos: tuple[int, int] = pygame.mouse.get_pos()

        # Making pointing hand cursor when hovering over a button
        game_loop.mouse_when_over_button(all_button_instances, mouse_pos)

        # Get the name of the button that was clicked. If no button clicked, it gets None
        button_name = button_clicked(all_button_instances, mouse_pos)

        # Create a set of all the names of the level buttons
        level_names = {"Level 1", "Level 2", "Level 3", "Level 4"}

        for event in pygame.event.get():
            """
            If one of the level buttons is clicked, the game will start the level.
            When the exit button on the game screen is clicked, game_logic will return False,
            The game loop will stop and the game will exit

            The If Else statement is written in the way that it does because otherwise
            you need to click the exit button twice to exit the game.
            One time to exit the game_logic loop and the second time to exit the main game loop.
            """
            # For explanation of the IF statement read the docstring above ^^^^^
            if button_name in level_names:
                is_playing = hangman_game.game_logic(
                    screen, button_name, all_button_instances
                )
            else:
                # If the X button is clicked, the game will exit
                is_playing = game_loop.exit_game(exit_button, event, mouse_pos)

        # Updating the screen each time we change something
        pygame.display.update()

    # Outside the loop, when the game is supposed to end
    print("Thank you for playing Hangman!")
    pygame.quit()


def button_clicked(all_button_instances: list[pygame.Rect], mouse_pos) -> str:
    """
    The function `button_clicked` checks if a button was clicked and returns the name of
    the button, otherwise it returns None.

    Args:
    all_button_instances (list[pygame.Rect]): The parameter `all_button_instances` is a list of
    `pygame.Rect` objects representing the bounding rectangles of all the buttons on the screen. Each
    `pygame.Rect` object contains the coordinates and dimensions of a button.
    mouse_pos: The parameter `mouse_pos` represents the current position of the mouse on the screen.
    It is expected to be a tuple containing the x and y coordinates of the mouse position.

    Returns:
    the name of the button that was clicked, as an integer. If no button is clicked, it returns None.
    """
    # Filter out non-clickable buttons before the loop
    clickable_buttons = [button for button in all_button_instances if button.clickable]

    # Get the list of all mouse button pressed.
    # [0] is the left mouse button, [1] is the middle mouse button, [2] is the right mouse button.
    mouse_click: list[int] = pygame.mouse.get_pressed()

    # Iterate over clickable buttons and check if the mouse is over any of them
    for button in clickable_buttons:
        if button.collidepoint(mouse_pos):
            if mouse_click[0] == 1:
                return button.name

    # If no button is clicked, return None
    else:
        return None


def guess_letter(letter: chr, word):
    ...


def function_n():
    ...


if __name__ == "__main__":
    main()
