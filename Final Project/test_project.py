# Learning Python with CS50
# Final Project !!!
# https://cs50.harvard.edu/python/2022/project/

import pygame
import project

from classes.word import Word
from classes.button import Button


def test_is_letter_guessed():
    # Initialize the Word class with a word and a topic
    word = Word("This is CS50", "CS courses")
    
    # Path to the image folder
    image_path = "images/letters/"
    
    # Initialize the letter button
    letter_button_A = Button(pygame.image.load(f"{image_path}A.png"), 50, 50, "A")
    letter_button_C = Button(pygame.image.load(f"{image_path}C.png"), 50, 50, "C")
    letter_button_T = Button(pygame.image.load(f"{image_path}T.png"), 50, 50, "T")
    
    assert project.is_letter_guessed(word, letter_button_A) == False
    assert project.is_letter_guessed(word, letter_button_C) == True
    assert project.is_letter_guessed(word, letter_button_T) == True


def test_make_restart_and_exit_clickable():
    # Contains all the Button instances
    all_button_instances: list[Button] = []
    
    # Initialize buttons
    mock_button1 = Button(pygame.image.load("images/V.png"), 0, 0, "V")
    all_button_instances.append(mock_button1)
    
    mock_button2 = Button(pygame.image.load("images/X.png"), 0, 0, "X")
    all_button_instances.append(mock_button2)
    
    restart_button = Button(pygame.image.load("images/restart.png"), 0, 0, "Restart")
    all_button_instances.append(restart_button)
    
    exit_button =  Button(pygame.image.load("images/exit button.png"), 0, 0, "Exit")
    all_button_instances.append(exit_button)
    
    # Make sure all buttons are unclickable at the start of the test
    for button in all_button_instances:
        button.clickable = False
        # Make sure the button is unclickable (i.e button.clickable = False)
        assert button.clickable == False
    
    # Run the list of all the buttons through the function.
    # This should make Exit and Restart button clickable again.
    project.make_restart_and_exit_clickable(all_button_instances)
    
    # Check that the Exit and restart buttons are clickable
    assert mock_button1.clickable == False
    assert mock_button2.clickable == False
    assert restart_button.clickable == True
    assert exit_button.clickable == True


def test_make_all_main_screen_button_unclickable():
    # Contains all the Button instances
    all_button_instances: list[Button] = []
    
    # Initialize buttons
    mock_button1 = Button(pygame.image.load("images/level buttons/easy.png"), 0, 0, "Easy")
    all_button_instances.append(mock_button1)
    
    mock_button2 = Button(pygame.image.load("images/level buttons/hard.png"), 0, 0, "Hard")
    all_button_instances.append(mock_button2)
    
    mock_button3 = Button(pygame.image.load("images/level buttons/medium.png"), 0, 0, "Medium")
    all_button_instances.append(mock_button3)
    
    mock_button4 =  Button(pygame.image.load("images/exit button.png"), 0, 0, "Exit")
    all_button_instances.append(mock_button4)
    
    # Make sure the all the buttons are clickable (i.e button.clickable = True)
    for button in all_button_instances:
        assert button.clickable == True
    
    
    project.make_all_main_screen_button_unclickable(all_button_instances)
    
    # Make sure all buttons are unclickable (i.e button.clickable = False)
    for button in all_button_instances:
        assert button.clickable == False
    
    
