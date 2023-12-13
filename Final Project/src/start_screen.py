"""
This file contains the code for the start screen of the game.
The functions are called to render different elements of the start screen.
"""


import pygame

from font import set_font
from classes.button import Button


def render_title(screen: pygame) -> pygame.Rect:
    """
    The function `render_title` renders the title "Hangman" on the screen using a specified font and
    returns the rectangle object representing the position of the rendered text.

    Args:
    screen (pygame): The `screen` parameter is the surface object representing the game window or
    screen on which the title will be rendered. It is of type `pygame.Surface`.

    Returns:
    a pygame.Rect object that represents the position and size of the rendered title text on the
    screen.
    """
    # Choose the font of the title
    title_font = pygame.font.Font(set_font.title_font(), 120)
    # Title text
    title_text: str = "Hangman"
    # Render the text
    title_render = title_font.render(title_text, True, (0, 0, 0))
    # Get the rect of the rendered text
    title_rect: pygame.Rect = title_render.get_rect()
    # Position the text at the top center of the screen
    title_rect.centerx = screen.get_rect().centerx
    # Adjust this value to set the vertical position
    title_rect.y = 50
    # Draw the text
    screen.blit(title_render, title_rect)
    # Return the rect object for reference
    return title_rect


def render_buttons(screen: pygame.Surface, title_rect: pygame.Rect) -> tuple[Button]:
    """
    The function `render_buttons` loads and positions level buttons on a screen surface in a pygame
    application.

    Args:
    screen (pygame.Surface): The `screen` parameter is a `pygame.Surface` object representing
    the game window or screen on which the buttons will be rendered.
    title_rect (pygame.Rect): The `title_rect` parameter is a `pygame.Rect` object that represents
    the rectangle area where the title of the screen is displayed. It is used to calculate
    the position of the buttons relative to the title.

    Returns:
    a tuple containing the Button objects for level 1, level 2, level 3, and level 4.
    """
    # Load the level button images
    image_folder_path: str = "CS50P/Final Project/images/level buttons/"
    level_1_img: pygame.Surface = pygame.image.load(f"{image_folder_path}level 1.png")
    level_2_img: pygame.Surface = pygame.image.load(f"{image_folder_path}level 2.png")
    level_3_img: pygame.Surface = pygame.image.load(f"{image_folder_path}level 3.png")
    level_4_img: pygame.Surface = pygame.image.load(f"{image_folder_path}level 4.png")

    # Size the images
    image_width, image_height = 450, 225

    # Instantiate the buttons as Button class instances
    level_1_button = Button(level_1_img, image_width, image_height)
    level_2_button = Button(level_2_img, image_width, image_height)
    level_3_button = Button(level_3_img, image_width, image_height)
    level_4_button = Button(level_4_img, image_width, image_height)

    # Calculate the horizontal center of the screen
    center_x: int = screen.get_rect().centerx

    # Set the margin between the title and the buttons, and between each button
    image_margin: int = 60

    """
    Set the buttons' position
    
    Sets the x-coordinate (x attribute) of the level_1_button so that it 
    is horizontally centered on the screen, considering the total width of two buttons 
    plus the margin between them, and using floor division to find the center position.
    """
    # Formula explained above
    level_1_button.x = (center_x - (2 * image_width + image_margin) // 2)
    level_1_button.y = title_rect.bottom + image_margin

    level_2_button.x = level_1_button.right + image_margin
    level_2_button.y = title_rect.bottom + image_margin

    # Formula explained above
    level_3_button.x = (center_x - (2 * image_width + image_margin) // 2)
    level_3_button.y = level_2_button.bottom + image_margin

    level_4_button.x = level_3_button.right + image_margin
    level_4_button.y = level_2_button.bottom + image_margin

    # Draw the images
    level_1_button.draw(screen)
    level_2_button.draw(screen)
    level_3_button.draw(screen)
    level_4_button.draw(screen)

    # Return the button objects for reference
    return level_1_button, level_2_button, level_3_button, level_4_button


def render_X_button(screen: pygame.Surface) -> pygame.Rect:
    """
    The function `render_X_button` renders an exit button on the screen using an image
    and returns the rectangle of the button for later use.

    Args:
    screen (pygame.Surface): The `screen` parameter is a `pygame.Surface` object representing the
    surface on which the button will be rendered.

    Returns:
    the rect attribute of the exit button, which is obtained using the get_rect() method
    of the Button class.
    """
    # Load the image
    image_folder_path: int = "CS50P/Final Project/images/"
    image: pygame.Surface = pygame.image.load(f"{image_folder_path}exit button.png")

    # Create an instance of the exit (big X) button as a Button class instance
    button = Button(image, 55, 60)

    # Set the X position of the exit button.
    margin_from_right_side = 63
    # It calculates the position from the right side, leaving a specified margin
    button.x = screen.get_width() - button.width - margin_from_right_side

    # Set the Y position of the exit button
    button.y = 30

    # Draw the button on the screen
    button.draw(screen)

    # Return the rect attribute for later use
    return button
