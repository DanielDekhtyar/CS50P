from font import get_font

"""
    The above code defines functions that return different fonts for different purposes in a
    graphical user interface.
    :return: The functions are returning different fonts.
"""


def title_font():
    return get_font.font("Fine College.ttf")


def topic_font():
    return get_font.font("Architex.ttf")


def exit_button_font():
    return get_font.font("Crosshatcher D.otf")


def level_button_font():
    return get_font.font("Light And Airy.ttf")