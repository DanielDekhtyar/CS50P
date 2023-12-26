"""
    The Button class represents a clickable button with an image.

    Attributes:
    - img (pygame.Surface): The image surface of the button.
    - img_width (int): The width of the button image.
    - img_height (int): The height of the button image.
    - _rect (pygame.Rect): The rectangular area occupied by the button on the screen.
    - _active (bool): A flag indicating whether the button is clickable or not.
    - _letter_button_clicked (bool): A flag indicating if it is not a letter button then it will remain False for the whole duration

    Methods:
    - draw(screen: pygame.Surface): Draws the button on the specified surface.
    - is_active() -> bool: Returns True if the button is currently active (clickable).
    - position() -> tuple[int, int]: Returns the (x, y) position of the top-left corner of the button.
    - x() -> int: Returns the x-coordinate of the top-left corner of the button.
    - y() -> int: Returns the y-coordinate of the top-left corner of the button.
    - width() -> int: Returns the width of the button.
    - get_rect() -> pygame.Rect: Returns the rectangular area occupied by the button.

    Properties (with setters):
    - top: Gets or sets the top y-coordinate of the button.
    - left: Gets or sets the left x-coordinate of the button.
    - bottom: Gets or sets the bottom y-coordinate of the button.
    - right: Gets or sets the right x-coordinate of the button.
    - collidepoint: Gets or sets the collidepoint function of the button's rectangle.
    - position: Gets or sets the (x, y) position of the top-left corner of the button.
    - x: Gets or sets the x-coordinate of the top-left corner of the button.
    - y: Gets or sets the y-coordinate of the top-left corner of the button.
    - width: Gets or sets the width of the button.
    """

import pygame


class Button:
    def __init__(self, img: pygame.Surface, img_width, img_hight, button_name):
        # Render the text using the given font and font size
        self._img: pygame.Surface = pygame.transform.scale(img, (img_width, img_hight))
        # Create a rectangle for the button using the rendered text
        self._rect: pygame.Rect = self._img.get_rect()
        # Initially the button is clickable
        self._clickable: bool = True
        self._hovering: bool = False
        self._button_name: str = button_name
        # Indicates if it is a letter button and if it was clicked
        # If it is not a letter button then it will remain False for the whole duration
        self._letter_button_clicked: bool = False

    # This function draws the button on the screen
    def draw(self, screen: pygame.Surface):
        screen.blit(self._img, self._rect)  # Draw the rendered text onto the screen
        pygame.display.flip()

    def check_hovering(self, mouse_pos):
        # Check if the mouse is hovering over the button
        self._hovering = self._rect.collidepoint(mouse_pos)

    @property
    def letter_button_clicked(self) -> bool:
        return self._letter_button_clicked

    @letter_button_clicked.setter
    def letter_button_clicked(self, value: bool):
        self._letter_button_clicked = value

    @property
    def position(self) -> tuple[int, int]:
        return self._rect.x, self._rect.y

    @position.setter
    def position(self, value: tuple[int, int]):
        self._rect.x, self._rect.y = value

    @property
    def clickable(self) -> bool:
        return self._clickable

    @clickable.setter
    def clickable(self, value: bool):
        self._clickable = value

    @property
    def name(self) -> str:
        return self._button_name

    @property
    def top(self):
        return self._rect.top

    @top.setter
    def top(self, value):
        self._rect.top = value

    @property
    def left(self):
        return self._rect.left

    @left.setter
    def left(self, value):
        self._rect.left = value

    @property
    def bottom(self):
        return self._rect.bottom

    @bottom.setter
    def bottom(self, value):
        self._rect.bottom = value

    @property
    def right(self):
        return self._rect.right

    @right.setter
    def right(self, value):
        self._rect.right = value

    @property
    def collidepoint(self):
        return self._rect.collidepoint

    @collidepoint.setter
    def collidepoint(self, value):
        self._rect.collidepoint = value

    # You can get and set the position by getting or providing a simple (X,Y) tuple
    @property
    def position(self) -> tuple[int, int]:
        pos = (self._rect.x, self._rect.y)
        return pos

    @position.setter
    def position(self, pos: tuple[int, int]):
        self._rect.x = pos[0]
        self._rect.y = pos[1]

    @property
    def x(self) -> int:
        return self._rect.x

    @x.setter
    def x(self, x: int):
        self._rect.x = x

    @property
    def y(self) -> int:
        return self._rect.y

    @y.setter
    def y(self, y: int):
        self._rect.y = y

    @property
    def width(self) -> int:
        return self._rect.width

    @width.setter
    def width(self, width: int):
        self._rect.width = width

    @property
    def hight(self) -> int:
        return self._rect.hight

    @hight.setter
    def hight(self, hight: int):
        self._rect.hight = hight

    def get_rect(self) -> pygame.Rect:
        return self._rect
