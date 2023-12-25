"""
This file contains all the game functionality 
"""

import csv
import random
import os
import pygame
import string
from PIL import Image, ImageEnhance

from classes.word import Word
from src import hangman_game
from src import game_screen
from src import game_loop
from font import set_font
import project


def game_logic(level, all_button_instances):
    change_main_screen_button_clickability(all_button_instances)

    # Create the word class
    word_cls = get_word_cls(level)
    screen, alphabet_buttons, exit_button = game_screen.render_game_screen(
        word_cls, all_button_instances
    )

    # Game screen Game Loop:
    is_playing = True
    # The Game loop. It will run until 'is_playing' is set to False, aka exit the game
    while is_playing:
        mouse_pos: tuple[int, int] = pygame.mouse.get_pos()

        for event in pygame.event.get():
            # Check if the game should exit
            is_playing = game_loop.exit_game(exit_button, event, mouse_pos)

            # If mouse hovers, it will change the cursor to a pointing hand
            game_loop.mouse_when_over_button(all_button_instances, mouse_pos)

        # Update the screen once after processing events
        pygame.display.update()
    return is_playing


def change_main_screen_button_clickability(
    all_button_instances: list[pygame.Rect],
) -> None:
    # Make all the buttons from the main screen unclickable
    for button in all_button_instances:
        if "Level" in button.name:
            button.clickable = False


def get_word_cls(level):
    topic, word = hangman_game.get_random_word(level)
    word_cls = Word(word, topic)
    return word_cls


def get_random_word(level) -> tuple[str, str]:
    csv_path = r"CS50P/Final Project/data/"
    csv_file = f"{level}.csv"
    path_to_csv = os.path.join(csv_path, csv_file)

    with open(path_to_csv, "r") as file:
        reader = csv.DictReader(file)
        # Convert the CSV rows to a list
        rows = list(reader)

        # Check if there is more than one row (header + data)
        if len(rows) > 1:
            # Get a random line from the file (exclude the header and last line)
            random_line = random.choice(rows[1:-1])
            return random_line["topic"], random_line["word"]
        else:
            # Return None if the CSV file is empty or has only a header
            return None


def guess_letter(letter: chr, word: Word) -> None:
    for index, char in enumerate(word.word):
        if char == letter:
            word.guessed_letters_index[index] = True
            return True
        else:
            return False


def apply_color_filter_to_letter(image, color, intensity):
    # Set the RGB for the requested color
    if color == "red":
        color = (255, 0, 0)
    elif color == "gray":
        color = (128, 128, 128)

    # Open the image
    img = Image.open(image)

    # Convert the image to RGBA (if it's not already)
    img = img.convert("RGBA")

    # Create a solid color image of the same size
    color_img = Image.new("RGBA", img.size, color + (0,))

    # Blend the original image with the color image using intensity
    result_img = Image.blend(img, color_img, intensity)
