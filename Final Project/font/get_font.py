import os


def font(font_file):
    """
    The function "font" takes a font file name as input and returns the full path to the font file.

    :param font_file: The `font_file` parameter is a string that represents the name of the font file
    (including the file extension) that you want to use
    :return: the full path to the font file by joining the font folder path and the font filename.
    """
    # The path to the folder containing the font file
    font_folder = r"CS50P\Final Project\font\fonts"

    # The name of the TTF file
    font_filename = font_file

    # Construct the full path to the font file
    return os.path.join(font_folder, font_filename)


if __name__ == "__main__":
    font()
