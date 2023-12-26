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


def masked_word_font():
    return get_font.font("phitradesign Handwritten Thin.ttf")


def game_over_font():
    return get_font.font("Strenght To Strenght.otf")
