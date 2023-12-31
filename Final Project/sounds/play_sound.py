"""
The code defines several functions that play different sounds using pygame.mixer.
"""

import pygame.mixer


def correct_answer() -> None:
    # Load the sound
    correct_answer_sound = pygame.mixer.Sound("CS50P/Final Project/sounds/correct answer.mp3")

    # Set volume 40%
    correct_answer_sound.set_volume(0.4)
    
    # Play the sound
    correct_answer_sound.play()
    
    return


def wrong_answer() -> None:
    # Load the sound
    wrong_answer_sound = pygame.mixer.Sound("CS50P/Final Project/sounds/wrong answer.mp3")

    # Set volume 50%
    wrong_answer_sound.set_volume(0.5)
    
    # Play the sound
    wrong_answer_sound.play()
    
    return


def yay() -> None:
    # Load the sound
    game_win_sound = pygame.mixer.Sound("CS50P/Final Project/sounds/yay.mp3")
    
    # Set volume 35%
    game_win_sound.set_volume(0.35)

    # Play the sound
    game_win_sound.play()
    
    return


def game_over() -> None:
    # Load the sound
    game_over_sound = pygame.mixer.Sound("CS50P/Final Project/sounds/game over.mp3")
    
    # Set volume 60%
    game_over_sound.set_volume(0.6)

    # Play the sound
    game_over_sound.play()
    
    return


def game_start() -> None:
    # Load the sound
    game_start_sound = pygame.mixer.Sound("CS50P/Final Project/sounds/game start.mp3")
    
    # Set volume 70%
    game_start_sound.set_volume(0.7)

    # Play the sound
    game_start_sound.play()
    
    return
