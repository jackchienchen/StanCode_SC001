"""
File: mirror_lake.py
Author: Jack Chen
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing the inverse image of
mt-rainier.jpg below the original one
"""

from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename:
    :return:
    """
    lake = SimpleImage('images/mt-rainier.jpg')
    blank = SimpleImage.blank(lake.width, lake.height * 2)
    for x in range(lake.width):
        for y in range(lake.height):
            img_p = lake.get_pixel(x, y)
            b_img_p1 = blank.get_pixel(x, y)
            b_img_p1.red = img_p.red
            b_img_p1.green = img_p.green
            b_img_p1.blue = img_p.blue

            b_img_p2 = blank.get_pixel(x, blank.height-1-y)
            b_img_p2.red = img_p.red
            b_img_p2.green = img_p.green
            b_img_p2.blue = img_p.blue
    return blank


def main():
    """
    TODO: Mirror the image
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
