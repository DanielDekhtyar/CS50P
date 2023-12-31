"""
The `game_logic` function controls the main logic of a hangman game, including rendering the game
screen, handling user input, and updating the screen based on the user's actions.

Args:
screen: The `screen` parameter is the Pygame surface object that represents the game window. It is
used to render and update the game elements on the screen.
level: The `level` parameter represents the difficulty level of the game. It is used to determine
the complexity of the word that the player needs to guess.
all_button_instances: The `all_button_instances` parameter is a list that contains instances of
all the buttons in the hangman game. Each button instance is represented by a `pygame.Rect` object.
"""

import csv
import random
import pygame

from classes.word import Word
from classes.button import Button
from src import game_screen
from src import game_loop
from sounds import play_sound
from utils import util_functions
import project


def game_logic(screen: pygame.Surface, level: str, all_button_instances: list[pygame.Rect]) -> bool:
    """
    The function `game_logic` controls the main logic of a hangman game, including rendering the game
    screen, handling user input, and updating the screen based on the user's actions.
    
    Args:
    screen: The screen parameter is the Pygame surface object that represents the game window. It is
    used to render and update the game elements on the screen.
    level: The level parameter represents the difficulty level of the game. It is used to determine
    the complexity of the word that the player needs to guess.
    all_button_instances: The `all_button_instances` parameter is a list that contains instances of
    all the buttons in the game. These buttons can include the letter buttons, the restart button, the
    exit button, and any other buttons that are present in the game screen.
    """
    # Make all the buttons from the main screen unclickable in the game screen
    # Currently all the buttons in all_button_instances are from the main screen
    project.make_all_main_screen_button_unclickable(all_button_instances)

    # Count how many attempts the user has made
    # Max 7 attempts till the game is over
    hangman_attempts: int = 0
    
    play_sound.game_start()

    # Create the word class
    word: Word = get_word_cls(level)

    # Render all the element on the screen
    exit_button = game_screen.render_game_screen(
        word, all_button_instances, screen, hangman_attempts
    )

    # Game screen Game Loop:
    is_playing: bool = True
    
    # The Game loop. It will run until 'is_playing' is set to False, aka exit the game
    while is_playing:
        mouse_pos: tuple[int, int] = pygame.mouse.get_pos()

        for event in pygame.event.get():
            # Check if the game should exit
            is_playing = game_loop.exit_game(exit_button, event, mouse_pos)

            # If mouse hovers, it will change the cursor to a pointing hand
            game_loop.mouse_when_over_button(all_button_instances, mouse_pos)
        
        # Code that runs when the Restart or Exit buttons are clicked
        is_playing = exit_or_restart(screen, is_playing, all_button_instances)

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
        
        # Make sure that the restart and exit buttons are clickable no matter what
        project.make_restart_and_exit_clickable(all_button_instances)
    
    return is_playing


def get_word_cls(level: str) -> Word:
    """
    The function `get_word_cls` takes a level as input, uses it to get a random word and its topic from
    the `hangman_game` module, and returns an instance of the `Word` class with the word and topic as
    attributes.
    
    Args:
    level: The level parameter is used to specify the difficulty level of the word that you want to
    retrieve. It is passed to the get_random_word() function to get a random word of the specified
    level.
    
    Returns:
    an instance of the Word class.
    """
    # Give the required level of the word to get_random_word() and receives back the word and it's topic
    topic, word = get_random_word(level)
    word: Word = Word(word, topic)
    return word


def get_random_word(level: str) -> tuple[str, str]:
    """
    The function `get_random_word` takes a level as input and returns a random word and its
    corresponding topic from a CSV file.
    
    Args:
    level: The `level` parameter is used to determine which CSV file to read from. It is a string that
    represents the level of difficulty or category of words. The CSV file name is constructed by
    appending the `level` parameter with the file extension ".csv".
    
    Returns:
    The function `get_random_word` returns a tuple containing two strings: the topic and the word.
    """
    
    # Path where all the csv files with the words are located within the project
    csv_path = f"CS50P/Final Project/data/{level}.csv"

    # Open the CSV file
    with open(csv_path, "r") as file:
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
    all_button_instances: list[Button],
    mouse_pos: tuple[int],
    hangman_attempts: int,
) -> tuple[bool, int]:
    """
    The function `guess_letter` takes in various parameters such as the game screen, the word to guess,
    the list of all button instances, the mouse position, and the number of hangman attempts, and it
    handles the logic for guessing a letter in the hangman game.
    
    Args:
    screen (pygame.Surface): The screen parameter is a pygame.Surface object representing the game
    screen where the hangman game is being displayed.
    word (Word): The `word` parameter is an instance of the `Word` class, which represents the word to
    be guessed in the hangman game.
    all_button_instances (list[Button]): A list of instances of the button class. Each instance
    represents a letter button on the screen.
    mouse_pos (tuple[int]): The `mouse_pos` parameter is a tuple of two integers representing the x
    and y coordinates of the mouse cursor on the screen.
    hangman_attempts (int): The `hangman_attempts` parameter represents the number of incorrect
    guesses made by the player in the Hangman game. It keeps track of the number of attempts made to
    guess the word.
    
    Returns:
    a tuple containing two values: `try_guessing` and `hangman_attempts`.
    """
    # Getting the button.name of the button that was clicked. If no button was clicked, it will get None
    button_name: str | None = util_functions.button_clicked(all_button_instances, mouse_pos)

    # Check if any letter was clicked at all
    try_guessing: bool = False

    # Initializing is_guessed that will be used to check if a letter was guessed right or not
    is_guessed: bool = False

    # Get the button instance
    button = util_functions.get_button_instance(button_name, all_button_instances)

    if button is not None and button.letter_button_clicked is False:
        if button_name != "Exit":
            # Goes over all the letters in the word

            # Indicate that the letter button was clicked
            button.letter_button_clicked = True

            # Check if the letter was guessed correctly and returns a boolean value accordingly
            is_letter_guessed: bool = project.is_letter_guessed(word, button)
            
            if is_letter_guessed:
                play_sound.correct_answer()
            
            elif not is_letter_guessed:
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
    all_button_instances: list[Button],
    screen: pygame.Surface,
) -> None:
    """
    The function updates the hangman game based on the number of attempts, the guessed letters, and the
    state of the buttons.
    
    Args:
    hangman_attempts (int): The number of attempts the player has made in the Hangman game.
    word (Word): The `word` parameter is an instance of the `Word` class, which represents the word to
    be guessed in the Hangman game. It contains information about the word itself, such as the actual
    word string and a list of boolean values indicating which letters have been guessed correctly.
    all_button_instances (list[Button]): The `all_button_instances` parameter is a list that contains
    instances of the `Button` class. These instances represent the buttons in the hangman game
    interface.
    screen (pygame.Surface): The `screen` parameter is a `pygame.Surface` object that represents the
    game screen. It is used to render and update the game graphics.
    """
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

        # Make all the buttons, except the exit and restart buttons, are unclickable
        for button in all_button_instances:
            if button.name != "Exit" or button.name != "Restart":
                button.clickable = False


def exit_or_restart(screen, is_playing: bool, all_button_instances: list[Button]) -> bool:
    """
    The function "exit_or_restart" checks if the game should exit or restart based on the button
    clicked and returns a boolean indicating if the game should continue running.
    
    Args:
    screen: The screen parameter is the surface object representing the game window or screen. It is
    used to draw and update the game graphics.
    is_playing (bool): A boolean variable that indicates whether the game is currently
    being played or not.
    all_button_instances (list[Button]): The parameter "all_button_instances" is a list
    that contains instances of the Button class.
    
    Returns:
    a boolean value indicating whether the game should continue running or not.
    """
    
    # Get the name of the button that was clicked
    button_name: str = util_functions.button_clicked(all_button_instances, pygame.mouse.get_pos())
    
    # Check if the game should exit
    if button_name == "Exit":
        is_playing = False
    
    # Check if the game should restart
    if button_name == "Restart":
        # Make all the buttons unclickable
        for button in all_button_instances:
            button.clickable = False
        
        # Restart the level by calling main()
        is_playing = project.main(screen, is_playing)

    # Return if the game should continue to run or not
    return is_playing
