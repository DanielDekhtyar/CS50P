"""
The `render_start_screen` function renders the start screen of a game, including the background
image, title, level buttons, and exit button, and returns the list of all button instances and the
exit button for later use in the game loop.

Args:
screen: The `screen` parameter is a `pygame.Surface` object that represents the game window or
screen where the elements will be rendered.

Returns:
The function `render_start_screen` returns a tuple containing two elements:
1. `all_button_instances`: a list of all the buttons (Button class instances) in the game.
2. `exit_button`: a pygame.Rect object representing the exit button on the top right corner of the
screen.
"""

import pygame

from utils.resource_path import resource_path
from font import set_font
from classes.button import Button


def render_start_screen(screen: pygame.Surface) -> tuple[list[Button], Button]:
    """
    The function `render_start_screen` renders the start screen of a game, including the background
    image, title, level buttons, and exit button, and returns the list of all button instances and the
    exit button for later use in the game loop.
    
    Args:
    screen: The screen parameter is the surface object representing the game window or screen where
    the elements will be rendered.
    
    Returns:
    The function `render_start_screen` returns a tuple containing two elements:
    1. `all_button_instances`: a list of all the buttons (Button class instances) in the game.
    2. `exit_button`: a pygame.Rect object representing the exit button on the top right corner of the
    screen.
    """
    # A list of all the buttons (Button class instances) in the game
    all_button_instances: list[Button] = []

    # Render the screen and the background image
    render_bg(screen)

    # Render the title "Hangman"
    title_rect: pygame.Rect = render_title(screen)

    # Render the buttons "Level 1", "Level 2", "Level 3", "Level 4"
    level_buttons_rect: pygame.Rect = render_buttons(screen, title_rect)
    # Add the newly created level buttons in to all_button_instances list
    all_button_instances.extend(level_buttons_rect)

    # Render the X button on the top right corner
    exit_button: pygame.Rect = render_exit_button(screen)
    # Add the newly created exit button in to all_button_instances list
    all_button_instances.append(exit_button)

    # Returns the buttons for later use in the game loop
    """
    exit_button returned both in the all_button_instances list and in the exit_button variable because the
    exit_button is used to detect when the button was clicked in the game loop.
    """
    return all_button_instances, exit_button


def render_bg(screen: pygame.Surface) -> None:
    """
    The `render_bg` function sets up the screen size, loads a background image, and renders it on the
    screen.
    
    Args:
    screen: The `screen` parameter is a pygame.Surface object that represents the screen on which the
    background image will be rendered.
    
    Returns:
    a pygame.Surface object, which represents the screen that has been rendered.
    """

    # Clean the screen. Make it completely white
    screen.fill((255, 255, 255))

    # Get the screen width and height to be letter set to the background image
    screen_width, screen_height = screen.get_width(), screen.get_height()

    # Select the background image
    bg_image_path: str = resource_path("Hangman-with-Pygame/images/background_image.png")

    # Load the background image
    bg_image: pygame.Surface = pygame.image.load(bg_image_path)

    # Scale the background image to the size of the screen
    bg_image: pygame.Surface = pygame.transform.scale(
        bg_image, (screen_width, screen_height)
    )

    # Draw the background image.(0, 0) the image will render at the top left corner of the screen
    screen.blit(bg_image, (0, 0))


def render_title(screen: pygame.Surface) -> pygame.Rect:
    """
    The function `render_title` renders and positions a title text on the screen using the Pygame
    library.
    
    Args:
    screen (pygame): The `screen` parameter is a pygame surface object that represents the screen or
    window on which the title will be rendered.
    
    Returns:
    a pygame.Rect object, which represents the rectangular area occupied by the rendered title text on
    the screen.
    """

    # Set the percentage of the screen that the title will occupy
    title_font_percentage = 0.13

    # Set the font size of the title according to the percentage of the screen
    title_font_size = int(screen.get_height() * title_font_percentage)

    # Choose the font of the title
    title_font = pygame.font.Font(set_font.title_font(), title_font_size)

    # Title text
    title_text: str = "Hangman"

    # Render the text
    title_render = title_font.render(title_text, True, (0, 0, 0))

    # Get the rect of the rendered text
    title_rect: pygame.Rect = title_render.get_rect()

    # Position the text at the top center of the screen
    title_rect.centerx = screen.get_rect().centerx

    # Adjust this value to set the vertical position
    title_rect.y = int(screen.get_height() * 0.05)

    # Draw the text
    screen.blit(title_render, title_rect)

    # Return the rect object for reference
    return title_rect


def render_buttons(screen: pygame.Surface, title_rect: pygame.Rect) -> tuple[Button]:
    """
    The `render_buttons` function takes a screen surface and a title rectangle as input, loads and sizes
    level button images, instantiates button objects, sets their positions, draws them on the screen,
    and returns the button objects.
    
    Args:
    screen (pygame.Surface): The `screen` parameter is a `pygame.Surface` object representing the game
    window or screen on which the buttons will be rendered.
    title_rect (pygame.Rect): The `title_rect` parameter is a `pygame.Rect` object that represents the
    rectangle area where the title of the screen is rendered. It is used to calculate the position of
    the buttons relative to the title.
    
    Returns:
    The function `render_buttons` returns a tuple containing the four `Button` objects:
    `level_1_button`, `level_2_button`, `level_3_button`, and `level_4_button`.
    """
    # Load the level button images
    image_folder_path: str = resource_path("Hangman-with-Pygame/images/level buttons/")
    level_1_img: pygame.Surface = pygame.image.load(resource_path(f"{image_folder_path}easy.png"))
    level_2_img: pygame.Surface = pygame.image.load(resource_path(f"{image_folder_path}medium.png"))
    level_3_img: pygame.Surface = pygame.image.load(resource_path(f"{image_folder_path}hard.png"))
    level_4_img: pygame.Surface = pygame.image.load(resource_path(f"{image_folder_path}very hard.png"))

    # Size the images
    image_width, image_height = int(screen.get_width() * 0.25), int(
        screen.get_height() * 0.25
    )

    # Instantiate the buttons as Button class instances
    level_1_button = Button(level_1_img, image_width, image_height, "Level 1")
    level_2_button = Button(level_2_img, image_width, image_height, "Level 2")
    level_3_button = Button(level_3_img, image_width, image_height, "Level 3")
    level_4_button = Button(level_4_img, image_width, image_height, "Level 4")

    # Calculate the horizontal center of the screen
    center_x: int = screen.get_rect().centerx

    # Set the margin between the title and the buttons, and between each button
    image_margin: int = int(screen.get_width() * 0.05)

    """
    Set the buttons' position
    
    Sets the x-coordinate (x attribute) of the level_1_button so that it 
    is horizontally centered on the screen, considering the total width of two buttons 
    plus the margin between them, and using floor division to find the center position.
    """
    # Formula explained above
    level_1_button.x = center_x - (2 * image_width + image_margin) // 2
    level_1_button.y = title_rect.bottom + image_margin

    level_2_button.x = level_1_button.right + image_margin
    level_2_button.y = title_rect.bottom + image_margin

    # Formula explained above
    level_3_button.x = center_x - (2 * image_width + image_margin) // 2
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


def render_exit_button(screen: pygame.Surface) -> Button:
    """
    The function `render_X_button` renders an exit button on the screen using an image and returns the
    rectangle of the button for later use.

    Args:
    screen (pygame.Surface): The `screen` parameter is a `pygame.Surface` object representing the
    surface on which the button will be rendered.

    Returns:
    the `rect` attribute of the `button` object.
    """
    # Load the image
    image_folder_path: int = resource_path("Hangman-with-Pygame/images/")
    image: pygame.Surface = pygame.image.load(resource_path(f"{image_folder_path}exit button.png"))

    button_width = int(screen.get_width() * 0.03)
    button_height = int(screen.get_height() * 0.055)
    # Create an instance of the exit (big X) button as a Button class instance
    button = Button(image, button_width, button_height, "Exit")

    # Set the X position of the exit button.
    margin_from_right_side = int(screen.get_width() * 0.045)

    # It calculates the position from the right side, leaving a specified margin
    button.x: int = screen.get_width() - button.width - margin_from_right_side

    # Set the Y position of the exit button
    button.y: int = int(screen.get_height() * 0.03)

    # Draw the button on the screen
    button.draw(screen)

    # Return the rect attribute for later use
    return button
