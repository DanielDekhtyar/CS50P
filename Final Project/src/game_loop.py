"""
game_loop.py contains the functions for the main game loop of the game.
"""

import pygame

import project
from src import game_screen
from src import hangman_game


# Making pointing hand cursor when hovering over a button
def mouse_when_over_button(all_button_instances, mouse_pos: tuple[int, int]):
    """
    The function `mouse_when_over_button` checks if the mouse is over any active button
    and changes the cursor type accordingly.

    Args:
    all_button_instances: all_button_instances is a list that contains instances of
    all the buttons in the game.
    """
    # Get the mouse position
    mouse_x, mouse_y = mouse_pos

    # Default the cursor to arrow cursor
    cursor_type = pygame.SYSTEM_CURSOR_ARROW

    # Iterate over all the buttons and check if the mouse is over any of them
    for button in all_button_instances:
        # Check if mouse is over the button and if the button is active
        if button.collidepoint(mouse_x, mouse_y) and button.clickable:
            # Change cursor to pointing hand when hovering over an active button
            cursor_type = pygame.SYSTEM_CURSOR_HAND
            break  # Exit the loop once we find a mouse is over a button

    # Set the cursor
    pygame.mouse.set_cursor(cursor_type)


def exit_game(
    X_button_rect: pygame.Rect, event: pygame.event, mouse_pos: tuple[int, int]
) -> bool:
    """
    The `exit_game` function checks if the X button or the ESC key is pressed to exit the game.

    Args:
    X_button_rect (pygame.Rect): The X_button_rect parameter is a pygame.Rect object that represents
    the rectangular area of the X button in the game. It is used to check if the mouse is hovering
    over the X button and if the X button is clicked.
    event (pygame.event): The `event` parameter is an instance of the `pygame.event.Event` class. It
    represents an event that has occurred in the game, such as a mouse click or a key press.

    Returns:
    a boolean value indicating whether the game should continue playing or not. If the game is
    exited (either by clicking the X button, pressing the ESC key, or triggering the QUIT event),
    the function returns False. Otherwise, it returns True to indicate that
    the game should continue playing.
    """
    # Get the position of the mouse
    mouse_x, mouse_y = mouse_pos

    # Check if the mouse is over the button
    is_hovering: int = X_button_rect.collidepoint(mouse_x, mouse_y)

    # QUIT event triggered when the user exits the app using Alt+F4 or the X button (windows button. not the in-game)
    is_game_exited = event.type == pygame.QUIT

    # Checks if the in-game X button was clicked
    is_x_button_pressed = (
        event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and is_hovering
    )

    # Checks if the ESC key was pressed
    is_esc_key_pressed = event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE

    # If the game is exited, the next 'while is_playing' loop in project.py would not execute
    if is_game_exited or is_x_button_pressed or is_esc_key_pressed:
        return False
    else:
        return True
