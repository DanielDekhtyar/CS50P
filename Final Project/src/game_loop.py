import pygame


"""
game_loop.py contains the functions for the main game loop of the game.
"""


# Making pointing hand cursor when hovering over a button
def mouse_when_over_button(
    X_button_rect: pygame.Rect, level_buttons_rect: list[pygame.Rect]
):
    """
    The function `mouse_when_over_button` changes the cursor to a pointing hand when the mouse is
    hovering over a button, and changes it back to an arrow when not hovering over a button.

    :param X_button_rect: The X_button_rect parameter is a pygame.Rect object that represents the
    rectangular area of the X button. It is used to check if the mouse is hovering over the X button
    :type X_button_rect: pygame.Rect
    :param level_buttons_rect: The parameter `level_buttons_rect` is a list of `pygame.Rect` objects
    representing the rectangles of the level buttons on the screen.
    Each `pygame.Rect` object contains the position and size of a level button
    :type level_buttons_rect: list[pygame.Rect]
    """
    # Get the mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()
    # Check if the mouse is over the button
    is_hovering: bool = X_button_rect.collidepoint(mouse_x, mouse_y)

    # Iterate over all the level buttons and check if the mouse is over any of the buttons
    for button in range(len(level_buttons_rect)):
        # Check if the mouse is over the button
        if level_buttons_rect[button].collidepoint(mouse_x, mouse_y):
            is_hovering = True
    if is_hovering:
        # Change cursor to pointing hand when hovering over a button
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        # Change cursor to arrow when not hovering over a button
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)


def exit_game(X_button_rect: pygame.Rect, event: pygame.event) -> bool:
    """
    The function `exit_game` checks if the X button is clicked or if the mouse is hovering over the
    X button and left mouse button is clicked, and returns a boolean value indicating whether
    the game should continue playing or not.

    :param X_button_rect: The X_button_rect parameter is a pygame.Rect object that represents the
    rectangular area of the X button in the game
    :type X_button_rect: pygame.Rect
    :param event: The `event` parameter is a pygame event object that represents a user action or
    system event. It can be used to check for specific events such as mouse clicks or window close.
    :type event: pygame.event
    :return: a boolean value indicating whether the game is still playing or not. If the X button is
    clicked or the pygame.QUIT event is triggered, the function returns False, indicating that the
    game should exit. Otherwise, it returns True, indicating that the game should continue playing.
    """
    mouse_x, mouse_y = pygame.mouse.get_pos()
    # Check if the mouse is over the button
    is_hovering: int = X_button_rect.collidepoint(mouse_x, mouse_y)
    # Get the state of the mouse buttons (left, middle, right)
    mouse_click: list[int] = pygame.mouse.get_pressed()
    # mouse_click[0] is the left mouse button
    if event.type == pygame.QUIT or (is_hovering and mouse_click[0] == 1):
        # the next 'while is_playing' loop would not execute
        is_playing: bool = False
        return is_playing
    else:
        is_playing = True
        return is_playing
