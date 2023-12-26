"""
Here is the code that describes what should be displayed on the screen.
There is no game logic in this file.
The game logic is in the hangman_game.py file.
"""

import pygame
import string

from src import start_screen
from classes.word import Word
from classes.button import Button
from font import set_font


def render_game_screen(word, all_button_instances, screen) -> None:
    # Reuse the code from start_screen.py as the background screen is the same
    # Render the screen surface
    start_screen.render_bg(screen)

    # Render the X exit button at the top right side of the screen
    exit_button = start_screen.render_exit_button(screen)

    # Renders the Topic : <topic> text
    render_topic_text(word.topic, screen)

    # Rended the masked word in the middle of the screen
    render_masked_word(word, screen)

    # Render the alphabet buttons
    render_letter_buttons(screen, all_button_instances)

    put_v_or_x(screen, all_button_instances, word)

    return exit_button


def render_topic_text(topic: str, screen: pygame.Surface) -> pygame.Rect:
    # Set the percentage of the screen that the text will occupy
    font_percentage = 0.11

    # Set the font size of the text according to the percentage of the screen
    font_size = int(screen.get_height() * font_percentage)

    # Choose the font of the text
    font = pygame.font.Font(set_font.topic_font(), font_size)

    # Title text
    text: str = f"Topic : {topic}"

    # Render the text
    render = font.render(text, True, (0, 0, 0))

    # Get the rect of the rendered text
    rect: pygame.Rect = render.get_rect()

    # Position the text at the top center of the screen
    rect.centerx = screen.get_rect().centerx

    # Adjust this value to set the vertical position
    rect.y = int(screen.get_height() * 0.05)

    # Draw the text
    screen.blit(render, rect)


def render_masked_word(word: Word, screen: pygame.Surface) -> pygame.Rect:
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
    rect.centery = screen.get_rect().centery - int(screen.get_height() * 0.045)

    # Draw the text
    screen.blit(render, rect)


# Function to render the letter buttons in rows and columns
def render_letter_buttons(
    screen: pygame.Surface, all_button_instances: list[Button]
) -> None:
    # Load letter images into a dictionary
    letter_images: dict[str, pygame.Surface] = {}
    for letter in string.ascii_uppercase:
        letter_images[letter] = pygame.image.load(
            f"CS50P/Final Project/images/letters/{letter}.png"
        )

    # The dimensions of the buttons
    button_width, button_height = 81, 93

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


def put_v_or_x(
    screen: pygame.Surface, all_button_instances: list[Button], word: Word
) -> None:
    for button in all_button_instances:
        if button.letter_button_clicked:
            if button.name in word.word:
                render_v_or_x_image(screen, button, "v")
            else:
                render_v_or_x_image(screen, button, "x")


def render_v_or_x_image(screen: pygame.Surface, button: Button, image_name) -> None:
    image = pygame.image.load(f"CS50P/Final Project/images/{image_name}.png")

    pos_x = button.x
    pos_y = button.y

    screen.blit(image, (pos_x, pos_y))
