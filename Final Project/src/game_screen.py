"""
The `render_game_screen` function renders the game screen with the masked word, hangman, restart
button, alphabet buttons, and green V or red X over letter buttons.

Args:
word: The `word` parameter is an instance of a class that represents the word to be guessed in the
game. It likely has attributes such as `topic` (the topic of the word) and `masked_word` (the word
with hidden letters).
all_button_instances: The `all_button_instances` parameter is a list that contains instances of
all the letter buttons in the game screen. These button instances are used to render the alphabet
buttons on the screen and to check if a button has been clicked by the player.
screen: The `screen` parameter is a `pygame.Surface` object representing the game screen or window
where the elements will be rendered. It is the surface on which the background, buttons, text, and
images will be displayed.
hangman_attempts: The `hangman_attempts` parameter represents the number of incorrect guesses the
player has made in the game. It is used to determine which stage of the hangman drawing to render on
the screen.

Returns:
    The function `render_game_screen` returns the `exit_button` object.
"""


import pygame
import string

from src import start_screen
from classes.word import Word
from classes.button import Button
from font import set_font


def render_game_screen(word: Word, all_button_instances: list[Button], screen: pygame.Surface, hangman_attempts: int) -> Button:
    """
    The function renders the game screen with the hangman, masked word, topic text, alphabet buttons,
    and restart button.
    
    Args:
    word: The word object that contains the topic and the masked word.
    all_button_instances: A list of all the button instances in the game screen.
    screen: The screen parameter is a pygame.Surface object that represents the game screen. It is
    used to render all the elements of the game screen.
    hangman_attempts: The number of attempts the player has made in the hangman game.
    
    Returns:
    the exit button.
    """
    # Reuse the code from start_screen.py as the background screen is the same
    # Render the screen surface
    start_screen.render_bg(screen)

    # Render the X exit button at the top right side of the screen
    exit_button = start_screen.render_exit_button(screen)

    # Renders the Topic : <topic> text
    render_topic_text(word.topic, screen)

    # Rended the masked word in the middle of the screen
    render_masked_word(word, screen)
    
    # Render the hangman
    render_the_hangman(screen, hangman_attempts)
    
    # Render the restart button
    restart_button = render_restart_button(screen)
    
    # Add restart button in to all_button_instances
    all_button_instances.append(restart_button)

    # Render the alphabet buttons
    render_letter_buttons(screen, all_button_instances)

    # Render green V or red X over letter buttons wherever needed
    put_v_or_x(screen, all_button_instances, word)

    # Returns the exit button for later use in the game logic
    return exit_button


def render_restart_button(screen: pygame.Surface) -> Button:
    """
    The function `render_restart_button` renders a restart button on the screen using an image and
    returns the rectangle of the button for later use.
    
    Args:
    screen (pygame.Surface): The `screen` parameter is a `pygame.Surface` object representing the
    surface on which the button will be rendered.
    
    Returns:
    the `rect` attribute of the `button` object.
    """
    # Load the image
    image_folder_path: int = "CS50P/Final Project/images/"
    image: pygame.Surface = pygame.image.load(f"{image_folder_path}restart.png")

    button_width = int(screen.get_width() * 0.035)
    button_height = int(screen.get_height() * 0.055)
    # Create an instance of the exit (big X) button as a Button class instance
    button = Button(image, button_width, button_height, "Restart")

    # Set the X position of the exit button.
    margin_from_right_side = int(screen.get_width() * 0.11)

    # It calculates the position from the right side, leaving a specified margin
    button.x: int = screen.get_width() - button.width - margin_from_right_side

    # Set the Y position of the button
    button.y: int = int(screen.get_height() * 0.03)

    # Draw the button on the screen
    button.draw(screen)

    # Return the rect attribute for later use
    return button


def render_topic_text(topic: str, screen: pygame.Surface) -> None:
    """
    The function `render_topic_text` renders a given topic text on a pygame surface, with the text
    positioned at the top center of the screen.
    
    Args:
    topic (str): The `topic` parameter is a string that represents the topic you want to render on the
    screen. It could be any text that you want to display as the topic.
    screen (pygame.Surface): The `screen` parameter is a `pygame.Surface` object, which represents the
    window or surface where the text will be rendered. It is the surface on which the text will be
    drawn.
    """
    # Set the font size based on a percentage of the screen height
    font_percentage: float = 0.11
    font_size: int = int(screen.get_height() * font_percentage)

    # Choose the font for the text
    font = pygame.font.Font(set_font.topic_font(), font_size)

    # Create the text string by concatenating the topic with the "Topic : " prefix
    text: str = f"Topic : {topic}"

    # Render the text using the chosen font
    render = font.render(text, True, (0, 0, 0))

    # Get the rectangle that encloses the rendered text
    rect: pygame.Rect  = render.get_rect()

    # Position the text at the top center of the screen
    rect.centerx: int = screen.get_rect().centerx
    rect.y: int = int(screen.get_height() * 0.05)

    # Draw the text on the screen
    screen.blit(render, rect)


def render_masked_word(word: Word, screen: pygame.Surface) -> None:
    # Get the masked word. i.e HANGMAN will be for example HAN_M_N
    masked_word = word.get_masked_word()
    # Set the percentage of the screen that the text will occupy
    font_percentage = 0.1

    # Set the font size of the text according to the percentage of the screen
    font_size = int(screen.get_height() * font_percentage)

    # Choose the font of the text
    font = pygame.font.Font(set_font.masked_word_font(), font_size)

    # Title text
    text: str = masked_word

    # Render the text
    render = font.render(text, True, (0, 0, 0))
    # Get the rect of the rendered text
    rect: pygame.Rect = render.get_rect()

    # Position the text at the top center of the screen
    rect.centerx = screen.get_rect().centerx

    # Adjust this value to set the vertical position
    rect.centery = screen.get_rect().centery

    # Draw the text
    screen.blit(render, rect)


# Function to render the letter buttons in rows and columns
def render_letter_buttons(screen: pygame.Surface, all_button_instances: list[Button]) -> None:
    """
    The function `render_letter_buttons` takes a screen surface and a list of button instances as input,
    and renders letter buttons on the screen using the provided button instances.
    
    Args:
    screen (pygame.Surface): The `screen` parameter is a `pygame.Surface` object representing the
    surface on which the buttons will be rendered.
    all_button_instances (list[Button]): `all_button_instances` is a list that contains instances of
    the `Button` class.
    """
    # Load letter images into a dictionary
    letter_images: dict[str, pygame.Surface] = {}
    for letter in string.ascii_uppercase:
        letter_images[letter] = pygame.image.load(
            f"CS50P/Final Project/images/letters/{letter}.png"
        )

    # The dimensions of the buttons
    button_width = screen.get_width() * 0.048
    button_height = screen.get_height() * 0.08

    # The margin between buttons
    button_margin_x, button_margin_y = 10, 10

    # 26 letters in the alphabet / 2 rows = 13 letters per row
    max_buttons_per_row = 13

    # Total number of buttons to be displayed
    total_buttons = len(letter_images)
    rows = (total_buttons + max_buttons_per_row - 1) // max_buttons_per_row

    # The X position of the first button (A)
    start_x = (
        screen.get_width()
        - (max_buttons_per_row * (button_width + button_margin_x) - button_margin_x)
    ) // 2

    # The Y position of the first button (A)
    start_y = (
        (
            screen.get_height()
            - (rows * (button_height + button_margin_y) - button_margin_y)
        )
        // 2
    ) + screen.get_height() * 0.35

    # Counts how many buttons was created
    buttons_count = 0

    # Iterate through each letter and its corresponding image
    for letter, image in letter_images.items():
        # Create a Button instance for the letter
        letter_button = Button(image, button_width, button_height, letter)
        letter_button.x = start_x
        letter_button.y = start_y

        # Draw the letter image onto the button
        letter_button.draw(screen)

        # Append the button instance to the list
        all_button_instances.append(letter_button)
        buttons_count += 1

        start_x += button_width + button_margin_x

        # Move to the next row if the maximum buttons per row is reached
        if buttons_count % max_buttons_per_row == 0:
            start_x = (
                screen.get_width()
                - (
                    max_buttons_per_row * (button_width + button_margin_x)
                    - button_margin_x
                )
            ) // 2
            start_y += button_height + button_margin_y


def put_v_or_x(screen: pygame.Surface, all_button_instances: list[Button], word: Word) -> None:
    """
    The function `put_v_or_x` iterates through a list of button instances and checks if each button's
    name is present in a given word, then renders a "v" or "x" image on the screen accordingly.
    
    Args:
    screen (pygame.Surface): The `screen` parameter is a `pygame.Surface` object representing the game
    screen or window where the buttons and images will be rendered.
    all_button_instances (list[Button]): `all_button_instances` is a list of `Button` instances.
    word (Word): The `word` parameter is an instance of the `Word` class. It represents a word that
    the player is trying to guess.
    """
    for button in all_button_instances:
        if button.letter_button_clicked:
            if button.name in word.word:
                render_v_or_x_image(screen, button, "v")
            else:
                render_v_or_x_image(screen, button, "x")


def render_v_or_x_image(screen: pygame.Surface, button: Button, image_name) -> None:
    """
    The function `render_v_or_x_image` takes a screen, a button, and an image name as input, loads the
    corresponding image, scales it to a specific size, and then blits it onto the screen at the position
    of the button.
    
    Args:
    screen (pygame.Surface): The `screen` parameter is a `pygame.Surface` object representing the game
    screen or window on which the image will be rendered.
    button (Button): The `button` parameter is an instance of the `Button` class. It represents a
    image_name: The `image_name` parameter is a string that represents the name of the image file to
    be loaded. It should not include the file extension (e.g., ".png").
    """
    image = pygame.image.load(f"CS50P/Final Project/images/{image_name}.png")

    pos_x = button.x
    pos_y = button.y
    
    image_height = int(screen.get_height() * 0.08)
    image_width = int(screen.get_width() * 0.048)
    
    image = pygame.transform.scale(image, (image_width, image_height))

    screen.blit(image, (pos_x, pos_y))


def render_the_hangman(screen: pygame.Surface, hangman_image_number: int) -> None:
    """
    The function `render_the_hangman` takes a screen surface and a hangman image number as input, loads
    the corresponding hangman image, scales it to a desired size, and then blits it onto the screen at a
    specified position.
    
    Args:
    screen (pygame.Surface): The `screen` parameter is a `pygame.Surface` object that represents the
    game window or screen on which the hangman image will be rendered.
    hangman_image_number (int): The `hangman_image_number` parameter is an integer that represents the
    number of the hangman image to be displayed. This number is used to load the corresponding image
    file from the "CS50P/Final Project/images/hangman/" directory.
    """
    hangman_image = pygame.image.load(
        f"CS50P/Final Project/images/hangman/{hangman_image_number}.png"
    )

    image_height = int(screen.get_height() * 0.3)

    image_width = int(screen.get_width() * 0.18)

    hangman_image = pygame.transform.scale(hangman_image, (image_width, image_height))

    # Get the desired X position
    pos_x = int(screen.get_width() * 0.04)

    # Adjust this value to set the vertical position
    pos_y = int(screen.get_height() * 0.05)

    # Draw the hangman on the screen
    screen.blit(hangman_image, (pos_x, pos_y))


# Render the GAME OVER! text on the screen
def render_game_over(screen: pygame.Surface) -> None:
    """
    The function `render_game_over` renders the text "GAME OVER!" at the top center of the screen.
    
    Args:
    screen (pygame.Surface): The `screen` parameter is a `pygame.Surface` object that represents the
    game screen on which the "GAME OVER!" text will be rendered.
    """
    # Set the percentage of the screen that the text will occupy
    font_percentage = 0.35

    # Set the font size of the text according to the percentage of the screen
    font_size = int(screen.get_height() * font_percentage)

    # Choose the font of the text
    font = pygame.font.Font(set_font.game_over_font(), font_size)

    # Title text
    text: str = "GAME OVER!"

    # Render the text
    render = font.render(text, True, (0, 0, 0))

    # Get the rect of the rendered text
    rect: pygame.Rect = render.get_rect()

    # Position the text at the top center of the screen
    rect.centerx = int(screen.get_rect().centerx)

    # Adjust this value to set the vertical position
    rect.y = int(screen.get_rect().centery) - int(screen.get_height() * 0.2)
    # Draw the text
    screen.blit(render, rect)
