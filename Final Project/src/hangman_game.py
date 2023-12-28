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
from sounds import play_sound
import project


def game_logic(screen, level, all_button_instances) -> bool:
    # Make all the buttons from the main screen unclickable in the game screen
    change_main_screen_button_clickability(all_button_instances)

    # Count how many attempts the user has made
    # Max 7 attempts till the game is over
    hangman_attempts = 0
    
    play_sound.game_start()

    # Create the word class
    word = get_word_cls(level)

    # Render all the element on the screen
    exit_button = game_screen.render_game_screen(
        word, all_button_instances, screen, hangman_attempts
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
        
        button_clicked = project.button_clicked(all_button_instances, mouse_pos)
        
        # Code that runs when the Restart or Exit buttons are clicked
        is_playing = project.exit_or_restart(screen, is_playing, all_button_instances)

        # When a letter button was clicked, guess_letters will check if the guessed letter is in the word.
        # If it is, word.guessed_letters_index is changed to True in the corresponding index.
        tried_guessing, hangman_attempts = guess_letter(
            screen, word, all_button_instances, mouse_pos, hangman_attempts
        )

        # If a letter was guessed, the game screen will be updated
        if tried_guessing:
            update_the_hangman(hangman_attempts, word, all_button_instances, screen)

        # Update the screen once after processing events
        pygame.display.update()
        for button in all_button_instances:
                    if button.name == "Restart" or button.name == "Exit":
                        button.clickable = True


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
    screen: pygame.Surface,
    word: Word,
    all_button_instances: list[pygame.Rect],
    mouse_pos: tuple[int],
    hangman_attempts: int,
) -> None:
    # Getting the button.name of the button that was clicked. If no button was clicked, it will get None
    button_name: str | None = project.button_clicked(all_button_instances, mouse_pos)

    # Check if any letter was clicked at all
    try_guessing: bool = False

    # Initializing is_guessed that will be used to check if a letter was guessed right or not
    is_guessed: bool = False

    # Get the button instance
    button = project.get_button_instance(button_name, all_button_instances)

    if button is not None and button.letter_button_clicked is False:
        if button_name is not None and button_name != "Exit":
            # Goes over all the letters in the word

            # Indicate that the letter button was clicked
            button.letter_button_clicked = True

            for i, char in enumerate(word.word):
                # If the letter that was guessed is in the word, change the guessed_letters_index to True
                if char == button_name:
                    # Make the letter visible in the masked word
                    word.guessed_letters_index[i] = True
                    is_guessed = True
                    
                    play_sound.correct_answer()

            if is_guessed is False:
                hangman_attempts += 1
                
                # Play only if there are attempts left.
                # This is done, so in the event of GAME OVER, just the game over sound will play and not both.
                if hangman_attempts < 7:
                    play_sound.wrong_answer()

            # Indicates that the letter was guessed
            try_guessing = True

            game_screen.render_v_or_x_image(screen, button, "x")

    return try_guessing, hangman_attempts


def update_the_hangman(
    hangman_attempts: int,
    word: Word,
    all_button_instances: list[pygame.Rect],
    screen: pygame.Surface,
):
    # If there are attempts left
    if hangman_attempts < 7:
        exit_button = game_screen.render_game_screen(
            word, all_button_instances, screen, hangman_attempts
        )
    # If the user has guessed ALL the letters
    if False not in word.guessed_letters_index:
        play_sound.yay()

    # If no more attempts are left, the game is over
    if hangman_attempts >= 7:
        # Make the whole word visible
        for i in range(len(word.word)):
            word.guessed_letters_index[i] = True
        
        play_sound.game_over()
        
        # Rerender the screen
        exit_button = game_screen.render_game_screen(
            word, all_button_instances, screen, hangman_attempts
        )
        # Render the GAME OVER! text on the screen
        game_screen.render_game_over(screen)

        # Make all the buttons, except the exit button, unclickable
        for button in all_button_instances:
            if button.name != "Exit":
                button.clickable = False
