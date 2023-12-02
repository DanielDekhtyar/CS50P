# Learning Python with CS50
# Final Project !!!
# https://cs50.harvard.edu/python/2022/project/

"""
Author : Daniel Dekhtyar
Email : denik2707@gmail.com
LinkedIn : https://www.linkedin.com/in/daniel-dekhtyar/
GitHub : https://github.com/DanielDekhtyar
"""


import pygame


def main():
    pygame.init()
    # This is like a header in HTMl
    pygame.display.set_caption("Hang man (Daniel's CS50P Final Project)")
    # Set screen dimensions
    screen = pygame.display.set_mode((1500, 1000))

    # Game runs until 'playing' is set to false. aka click the X button
    is_playing: bool = True
    while is_playing:
        screen.fill((255, 255, 255))

        keyboard_key = pygame.key.get_pressed()

        # check all the events and if the red X button is clicked, the game will exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # the next 'while playing' loop would not execute
                is_playing = False
                break

        # updating the screen each time we change something
        pygame.display.flip()

    pygame.quit()


def function_1():
    ...


def function_2():
    ...


def function_n():
    ...


if __name__ == "__main__":
    main()
