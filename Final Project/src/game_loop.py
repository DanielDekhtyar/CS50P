import pygame


# Making pointing hand cursor when hovering over a button
def mouse_when_over_button(X_button_rect, level_buttons_rect):
    """
    This function checks if the mouse is hovering over a button and changes the cursor accordingly.

    :param X_button_rect: The X_button_rect is a rectangle that represents the position and size of the
    X button on the screen. It is used to check if the mouse is hovering over the X button
    :param level_buttons_rect: level_buttons_rect is a list of rectangles representing the bounding
    boxes of the level buttons on the screen. Each rectangle is defined by its top-left corner
    coordinates (x, y) and its width and height
    """
    # Get the mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()
    # Check if the mouse is over the button
    is_hovering = X_button_rect.collidepoint(mouse_x, mouse_y)

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


def exit_game(X_button_rect, event):
    """
    The function `exit_game` checks if the mouse is hovering over the X button and left mouse button
    is clicked, and returns a boolean value indicating whether the game should continue playing or not.

    :param X_button_rect: X_button_rect is a rectangle object that represents the position and size of
    the X button on the screen
    :param event: The `event` parameter is an object that represents an event that has occurred in the
    game. It could be a keyboard event, mouse event, or any other type of event that the game is
    listening for
    :return: the value of the variable "is_playing".
    """
    mouse_x, mouse_y = pygame.mouse.get_pos()
    # Check if the mouse is over the button
    is_hovering = X_button_rect.collidepoint(mouse_x, mouse_y)
    # Get the state of the mouse buttons (left, middle, right)
    mouse_click = pygame.mouse.get_pressed()
    # mouse_click[0] is the left mouse button
    if event.type == pygame.QUIT or (is_hovering and mouse_click[0] == 1):
        # the next 'while is_playing' loop would not execute
        is_playing = False
        return is_playing
    else:
        is_playing = True
        return is_playing
