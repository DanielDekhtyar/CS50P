import pygame


class Button:
    def __init__(self, text: str, font: pygame.font.Font, font_size: int):
        self._render = font.render(text, True, (0, 0, 0))
        self._rect: pygame.Rect = self._render.get_rect()
        self._active = True

    def draw(self, screen):
        screen.blit(self._render, self._rect)  # Draw the rendered text onto the screen

    def get_x(self) -> int:
        return self._rect.x

    def set_x(self, x):
        self._rect.x = x

    def get_y(self) -> int:
        return self._rect.y

    def set_y(self, y):  # Fix: Correct method name
        self._rect.y = y

    def get_width(self) -> int:  # Fix: Correct method name
        return self._rect.width

    def set_width(self, width):  # Fix: Correct method name
        self._rect.width = width

    def get_height(self) -> int:
        return self._rect.height

    def set_height(self, height):  # Fix: Correct method name
        self._rect.height = height
