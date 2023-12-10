import pygame

from font import set_font


"""
This file contains the code for the start screen of the game.
The functions are called to render different elements of the start screen.
"""


def render_title(screen: pygame) -> pygame.Rect:
    """
    The function `render_title` renders the title "Hangman" on the screen using a specified font and
    returns the rectangle object representing the position of the rendered text.

    :param screen: The `screen` parameter is the surface object representing the game window or
    screen on which the title will be rendered. It is of type `pygame.Surface`
    :type screen: pygame
    :return: a pygame.Rect object that represents the position and size of the rendered title
    text on the screen.
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


def render_buttons(screen: pygame.Surface, title_rect: pygame.Rect) -> tuple[pygame.Rect]:
    """
    The `render_buttons` function renders four level buttons on the screen and returns the rectangle
    objects representing their positions.

    :param screen: The `screen` parameter is a `pygame.Surface` object representing the surface on
    which the buttons will be rendered. This is typically the main display surface of the game window
    :type screen: pygame.Surface
    :param title_rect: The `title_rect` parameter is a `pygame.Rect` object that represents the
    rectangle where the title of the screen is located. It is used to calculate the positions of the
    level buttons relative to the title
    :type title_rect: pygame.Rect
    :return: The function `render_buttons` returns a tuple of `pygame.Rect` objects.
    """
    # Load the level button images
    image_folder_path: int = "CS50P/Final Project/images/level buttons/"
    level_1_img: pygame.Surface = pygame.image.load(f"{image_folder_path}level 1.png")
    level_2_img: pygame.Surface = pygame.image.load(f"{image_folder_path}level 2.png")
    level_3_img: pygame.Surface = pygame.image.load(f"{image_folder_path}level 3.png")
    level_4_img: pygame.Surface = pygame.image.load(f"{image_folder_path}level 4.png")

    # Resize the images if needed
    image_width, image_height = 400, 200
    level_1_img: pygame.Surface = pygame.transform.scale(
        level_1_img, (image_width, image_height)
    )
    level_2_img: pygame.Surface = pygame.transform.scale(
        level_2_img, (image_width, image_height)
    )
    level_3_img: pygame.Surface = pygame.transform.scale(
        level_3_img, (image_width, image_height)
    )
    level_4_img: pygame.Surface = pygame.transform.scale(
        level_4_img, (image_width, image_height)
    )

    # Calculate the horizontal center for the images
    center_x: int = screen.get_rect().centerx

    # Set the positions of the images
    image_margin: int = 80
    image1_rect: pygame.Rect = level_1_img.get_rect()
    image1_rect.x: int = center_x - (2 * image_width + image_margin) // 2
    image1_rect.y: int = title_rect.bottom + image_margin

    image2_rect: pygame.Rect = level_2_img.get_rect()
    image2_rect.x: int = image1_rect.right + image_margin
    image2_rect.y: int = title_rect.bottom + image_margin

    image3_rect: pygame.Rect = level_3_img.get_rect()
    image3_rect.x: int = center_x - (2 * image_width + image_margin) // 2
    image3_rect.y: int = image2_rect.bottom + image_margin

    image4_rect: pygame.Rect = level_4_img.get_rect()
    image4_rect.x: int = image3_rect.right + image_margin
    image4_rect.y: int = image2_rect.bottom + image_margin

    # Draw the images
    screen.blit(level_1_img, image1_rect)
    screen.blit(level_2_img, image2_rect)
    screen.blit(level_3_img, image3_rect)
    screen.blit(level_4_img, image4_rect)

    # Return the rect objects for reference
    return image1_rect, image2_rect, image3_rect, image4_rect


def render_X_button(screen: pygame) -> pygame.Rect:
    """
    The function `render_X_button` renders an "X" button on the screen at the top right corner.

    :param screen: The "screen" parameter is the pygame surface on which the X button will be
    rendered. It represents the window or display where the game or application is being shown
    :type screen: pygame
    :return: a pygame.Rect object.
    """
    # Choose the font of the title
    font = pygame.font.Font(set_font.exit_button_font(), 55)
    # Title text
    text: str = "X"
    # Render the text
    render = font.render(text, True, (0, 0, 0))
    # Get the rect of the rendered text
    rect: pygame.Rect = render.get_rect()
    # Position the text at the top right corner of the screen
    # -65 is the margin from the right side of the screen
    rect.x: int = screen.get_width() - rect.width - 65
    # Adjust this value to set the vertical position
    rect.y: int = 25
    # Draw the text
    screen.blit(render, rect)
    # rect obj returns to later know when the mouse hovers over it
    return rect
