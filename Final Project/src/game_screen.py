import pygame
from src import start_screen


def render_game_screen() -> pygame.Surface:
    # Reuse the code from start_screen.py as the background screen is the same
    screen = start_screen.render_screen()
    exit_button = start_screen.render_exit_button()