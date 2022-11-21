"""
File: shrink.py
Author: Jack Chen
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    """
    :param filename: str,
    :return img: SimpleImage,
    """
    img = SimpleImage(filename)
    img_blank = SimpleImage.blank(img.width//2, img.height//2)

    for y in range(img.height-2):
        for x in range(img.width-2):
            p1 = img.get_pixel(x, y)
            p2 = img.get_pixel(x+1, y+1)
            p3 = img.get_pixel(x, y+1)
            p4 = img.get_pixel(x+1, y+1)
            for i in range(img_blank.height):
                for j in range(img_blank.height):
                    new_pixel = img_blank.get_pixel(i, j)
                    new_pixel.red = (p1.red + p2.red + p3.red + p4.red) / 4
                    new_pixel.blue = (p1.blue + p2.blue + p3.blue + p4.blue) / 4
                    new_pixel.red = (p1.green + p2.green + p3.green + p4.green) / 4
            x += 2
        y += 2
    return img_blank


def main():
    """
    TODO:
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


if __name__ == '__main__':
    main()
