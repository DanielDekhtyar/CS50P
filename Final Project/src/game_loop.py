"""
The `exit_game` function checks if the user has clicked the in-game X button, pressed the ESC key,
or exited the app using Alt+F4 or the X button, and returns `False` if any of these conditions are
met, indicating that the game should exit.

Args:
all_button_instances: `all_button_instances` is a list of all the button instances in the current
scene or screen. Each button instance should have a `collidepoint` method to check if the mouse is
over the button and a `clickable` attribute to determine if the button is active or clickable.
mouse_pos (tuple[int, int]): The `mouse_pos` parameter is a tuple containing the x and y
coordinates of the mouse cursor on the screen. It is used to determine the position of the mouse
when checking if it is over a button or the X button.
"""

import pygame
from classes.button import Button


# Making pointing hand cursor when hovering over a button
def mouse_when_over_button(all_button_instances: list[Button], mouse_pos: tuple[int, int]) -> None:
    """
    The function `mouse_when_over_button` checks if the mouse is over any active button and changes the
    cursor type accordingly.
    
    Args:
    all_button_instances: all_button_instances is a list of all the button instances in the current
    scene or screen. Each button instance should have a `collidepoint` method to check if the mouse is
    over the button and a `clickable` attribute to determine if the button is active or clickable.
    mouse_pos (tuple[int, int]): The mouse_pos parameter is a tuple containing the x and y coordinates
    of the mouse cursor on the screen.
    """
    # Default the cursor to arrow cursor
    cursor_type = pygame.SYSTEM_CURSOR_ARROW

    # Iterate over all the buttons and check if the mouse is over any of them
    for button in all_button_instances:
        # Check if mouse is over the button and if the button is active
        if button.collidepoint(mouse_pos) and button.clickable:
            # Change cursor to pointing hand when hovering over an active button
            cursor_type = pygame.SYSTEM_CURSOR_HAND
            break  # Exit the loop once we find a mouse is over a button

    # Set the cursor
    pygame.mouse.set_cursor(cursor_type)


def exit_game(
    X_button_rect: pygame.Rect,
    event: pygame.event,
    mouse_pos: tuple[int, int]
) -> bool:
    """
    The `exit_game` function checks if the user has clicked the in-game X button, pressed the ESC key,
    or exited the app using Alt+F4 or the X button, and returns `False` if any of these conditions are
    met, indicating that the game should exit.
    
    Args:
    X_button_rect (pygame.Rect): The `X_button_rect` parameter is a `pygame.Rect` object that
    represents the rectangular area of the X button in the game. It is used to check if the mouse is
    hovering over the X button.
    event (pygame.event): The `event` parameter is a `pygame.event` object that represents an event
    that occurred in the game. This could be a mouse click, a key press, or any other type of event that
    the game is programmed to handle.
    mouse_pos (tuple[int, int]): The `mouse_pos` parameter is a tuple containing the x and y
    coordinates of the mouse cursor on the screen.
    
    Returns:
    The function `exit_game` returns a boolean value. If the game is not exited (i.e., the user did
    not click the X button, press the ESC key, or exit the app using Alt+F4), it returns `True`.
    Otherwise, if the game is exited, it returns `False`.
    """
    # Check if the mouse is over the button
    is_hovering: int = X_button_rect.collidepoint(mouse_pos)

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
