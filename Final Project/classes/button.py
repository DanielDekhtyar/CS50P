import pygame


# The Button class represents a button with text that can be rendered and displayed on a screen.
class Button:
    def __init__(self, text: str, font: pygame.font.Font, font_size: int):
        # Render the text using the given font and font size
        self._render: pygame.Surface = font.render(text, True, (0, 0, 0))
        # Create a rectangle for the button using the rendered text
        self._rect: pygame.Rect = self._render.get_rect()
        # Initially the button is active and clickable
        self._active: bool = True

    # This function draws the button on the screen
    def draw(self, screen: pygame.Surface):
        screen.blit(self._render, self._rect)  # Draw the rendered text onto the screen

    def get_x(self) -> int:
        return self._rect.x

    def set_x(self, x: int):
        self._rect.x = x

    def get_y(self) -> int:
        return self._rect.y

    def set_y(self, y: int):
        self._rect.y = y

    def get_width(self) -> int:
        return self._rect.width

    def set_width(self, width: int):
        self._rect.width = width

    def get_height(self) -> int:
        return self._rect.height

    def set_height(self, height: int):
        self._rect.height = height
