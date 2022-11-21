"""
File: fire.py
Author: Jack Chen
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    :param filename: SimpleImage, input of the original image.
    :return: SimpleImage, turns the original image into grey scale except the fire parts.
    Aimed to point out the fire in the forest, and grey scaled the other
    parts with no fire.
    """
    img = SimpleImage(filename)
    for pixel in img:
        avg = (pixel.red+pixel.blue+pixel.green)/3
        if pixel.red > avg * HURDLE_FACTOR:
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
        else:
            pixel.red = avg
            pixel.blue = avg
            pixel.green = avg
    return img


def main():
    """
    Display the original image and points out the fire in the forest
    with the second image.
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


if __name__ == '__main__':
    main()
