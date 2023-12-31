"""
Utility functions to use throughout the code.
"""

from typing import Tuple
import pygame
from classes.button import Button


def button_clicked(all_button_instances: list[Button], mouse_pos: Tuple[int, int]) -> str | None:
    """
    The function `button_clicked` takes a list of button instances and the current mouse position as
    input, filters out non-clickable buttons, checks if the mouse is over any clickable button, and
    returns the name of the button if the left mouse button is clicked, otherwise it returns None.
    
    Args:
    all_button_instances (list[Button]): The parameter `all_button_instances` is a list of `Button`
    instances.
    mouse_pos (Tuple[int, int, int]): The `mouse_pos` parameter is a tuple containing the x and y
    coordinates of the mouse cursor, as well as the state of the mouse buttons. The format of the
    tuple is `(x, y, buttons)`, where `x` and `y` are the coordinates and `buttons` is
    
    Returns:
    The function `button_clicked` returns a string representing the name of the button that was
    clicked, or `None` if no button was clicked.
    """
    # Filter out non-clickable buttons before the loop
    clickable_buttons: list = [button for button in all_button_instances if button.clickable]

    # Get the list of all mouse button pressed.
    # [0] is the left mouse button, [1] is the middle mouse button, [2] is the right mouse button.
    mouse_click: list[int] = pygame.mouse.get_pressed()

    # Iterate over clickable buttons and check if the mouse is over any of them
    for button in clickable_buttons:
        if button.collidepoint(mouse_pos):
            # mouse_click[0] is the left mouse button
            if mouse_click[0] == 1:
                return button.name

    # If no button is clicked, return None
    return None


def get_button_instance(button_name: str, all_button_instances: list[Button]) -> Button:
    """
    The function `get_button_instance` takes a button name and a list of button instances,
    and returns the button instance with the matching name.
    
    Args:
    button_name (str): A string representing the name of the button we want to find.
    all_button_instances (list[Button]): A list of Button instances,
    representing all the buttons available in the program.
    
    Returns:
    an instance of the Button class that matches the given button_name.
    """
    # Goes over all the buttons in the list
    for button in all_button_instances:
        # If the button.name matches the button_name, it will return the button
        if button.name == button_name:
            return button
