"""
This file contains all the game functionality 
"""

import csv
import random
import os
import pygame

from classes.word import Word
from src import hangman_game
from src import game_screen
from src import game_loop
from font import set_font
import project


def game_logic(screen, level, all_button_instances):
    # Make all the buttons from the main screen unclickable in the game screen
    change_main_screen_button_clickability(all_button_instances)

    # Create the word class
    word = get_word_cls(level)
    exit_button = game_screen.render_game_screen(word, all_button_instances, screen)

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
        
        # When a letter button was clicked, guess_letters will check if the guessed letter is in the word.
        # If it is, word.guessed_letters_index is changed to True in the corresponding index.
        is_guessed = guess_letter(word, all_button_instances, mouse_pos)

        # If a letter was guessed, the game screen will be updated
        if is_guessed:
            screen.fill((255, 255, 255))
            exit_button = game_screen.render_game_screen(word, all_button_instances, screen)

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
    # Give the required level of the word to get_random_word() and receives back the word and it's topic
    topic, word = hangman_game.get_random_word(level)
    word = Word(word, topic)
    return word


def get_random_word(level) -> tuple[str, str]:
    # Path to where all the csv files with the words are located within the project
    csv_path = r"CS50P/Final Project/data/"
    
    # Get the CSV file name based on the level
    csv_file = f"{level}.csv"
    
    # Join the path to the file
    path_to_csv = os.path.join(csv_path, csv_file)

    # Open the CSV file
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


def guess_letter(
    word: Word, all_button_instances: list[pygame.Rect], mouse_pos: tuple[int]
) -> None:
    # Getting the button.name of the button that was clicked. If no button was clicked, it will get None
    button_clicked: str | None = project.button_clicked(all_button_instances, mouse_pos)
    
    # Initializing is_guessed that will be used to check if a letter was guessed or not
    is_guessed = False
    
    if button_clicked is not None and button_clicked != "Exit":
        # Goes over all the letters in the word
        for i, char in enumerate(word.word):
            # If the letter that was guessed is in the word, change the guessed_letters_index to True
            if char == button_clicked:
                word.guessed_letters_index[i] = True
                # Indicates that the letter was guessed
                is_guessed = True
    
    # It returned to indicate that the game screen needs to be updated
    return is_guessed
