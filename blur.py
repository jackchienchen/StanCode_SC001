"""
File: blur.py
Name: Jack Chen
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    Functions to blur the original smile photo.
    """
    # Loop over the picture
    new_img = SimpleImage.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.height):
            img_p = img.get_pixel(x, y)
            b_img_p1 = new_img.get_pixel(x, y)

            # Todo: get pixel of new_img at x,y
            # Belows are 9 conditions of pixel filling, depending on pixels' x,y orientation.
            if x == 0 and y == 0:
                # Get pixel at the top-left corner of the image.
                img_total_red = (img.get_pixel(1, 1).red+img.get_pixel(0, 1).red + img.get_pixel(1, 0).red+ img_p.red)/4
                img_total_green = (img.get_pixel(1, 1).green + img.get_pixel(0, 1).green + img.get_pixel(1, 0).green+img_p.green)/4
                img_total_blue = (img.get_pixel(1, 1).blue + img.get_pixel(0, 1).blue + img.get_pixel(1, 0).blue+img_p.blue) / 4
                b_img_p1.red = img_total_red
                b_img_p1.green = img_total_green
                b_img_p1.blue = img_total_blue
            elif x == img.width-1 and y == 0:
                # Get pixel at the top-right corner of the image.
                img_total_red = (img.get_pixel(img.width-2, 1).red + img.get_pixel(img.width-2, 0).red + img.get_pixel(img.width-1, 1).red + img_p.red) / 4
                img_total_green = (img.get_pixel(img.width-2, 1).green + img.get_pixel(img.width-2, 0).green + img.get_pixel(img.width-1, 1).green + img_p.green) / 4
                img_total_blue = (img.get_pixel(img.width-2, 1).blue + img.get_pixel(img.width-2, 0).blue + img.get_pixel(img.width-1, 1).blue + img_p.blue) / 4
                b_img_p1.red = img_total_red
                b_img_p1.green = img_total_green
                b_img_p1.blue = img_total_blue
            elif x == img.width-1 and y == img.height-1:
                # Get pixel at the bottom-right corner of the image
                img_total_red = (img.get_pixel(img.width - 1, img.height-2).red + img.get_pixel(img.width - 2, img.height-1).red + img.get_pixel(img.width - 2, img.height-2).red + img_p.red) / 4
                img_total_green = (img.get_pixel(img.width - 1, img.height - 2).green + img.get_pixel(img.width - 2, img.height - 1).green + img.get_pixel(img.width - 2, img.height - 2).green + img_p.green) / 4
                img_total_blue = (img.get_pixel(img.width - 1, img.height - 2).blue + img.get_pixel(img.width - 2,img.height - 1).blue + img.get_pixel( img.width - 2, img.height - 2).blue + img_p.blue) / 4
                b_img_p1.red = img_total_red
                b_img_p1.green = img_total_green
                b_img_p1.blue = img_total_blue
            elif x == 0 and y == img.height-1:
                # bottom left
                img_total_red = (img.get_pixel(0, img.height - 2).red + img.get_pixel(1,img.height - 2).red + img.get_pixel(1, img.height - 1).red + img_p.red) / 4
                img_total_green = (img.get_pixel(0, img.height - 2).green + img.get_pixel(1,img.height - 2).green + img.get_pixel(1, img.height - 1).green + img_p.green) / 4
                img_total_blue = (img.get_pixel(0, img.height - 2).blue + img.get_pixel(1,img.height - 2).blue + img.get_pixel(1, img.height - 1).blue + img_p.blue) / 4
                b_img_p1.red = img_total_red
                b_img_p1.green = img_total_green
                b_img_p1.blue = img_total_blue
            elif 0 < x < img.width-1 and y == 0:
                # Get top edge's pixels (without two corners)
                img_total_red = (img.get_pixel(x-1, 0).red + img.get_pixel(x-1, 1).red + img.get_pixel(x, 1).red+ img.get_pixel(x+1, 1).red+ img.get_pixel(x+1, 0).red + img_p.red) / 6
                img_total_green = (img.get_pixel(x - 1, 0).green + img.get_pixel(x - 1, 1).green + img.get_pixel(x,1).green + img.get_pixel(x + 1, 1).green + img.get_pixel(x + 1, 0).green + img_p.green) / 6
                img_total_blue = (img.get_pixel(x - 1, 0).blue + img.get_pixel(x - 1, 1).blue + img.get_pixel(x,1).blue + img.get_pixel(x + 1, 1).blue + img.get_pixel(x + 1, 0).blue + img_p.blue) / 6
                b_img_p1.red = img_total_red
                b_img_p1.green = img_total_green
                b_img_p1.blue = img_total_blue
            elif 0 < x < img.width-1 and y == img.height-1:
                # Get bottom edge's pixels (without two corners)
                img_total_red = (img.get_pixel(x - 1, img.height-1).red + img.get_pixel(x - 1, img.height-2).red + img.get_pixel(x,img.height-2).red + img.get_pixel(x + 1, img.height-2).red + img.get_pixel(x + 1, img.height-1).red + img_p.red) / 6
                img_total_green = (img.get_pixel(x - 1, img.height-1).green + img.get_pixel(x - 1, img.height-2).green+ img.get_pixel(x,img.height-2).green + img.get_pixel(x + 1, img.height-2).green + img.get_pixel(x + 1, img.height-1).green + img_p.green) / 6
                img_total_blue = (img.get_pixel(x - 1, img.height - 1).blue + img.get_pixel(x - 1,img.height - 2).blue + img.get_pixel(x, img.height - 2).blue + img.get_pixel(x + 1, img.height - 2).blue + img.get_pixel(x + 1,img.height - 1).blue + img_p.blue) / 6
                b_img_p1.red = img_total_red
                b_img_p1.green = img_total_green
                b_img_p1.blue = img_total_blue

            elif x == 0:
                # Get left edge's pixels (without two corners)
                img_total_red = (img.get_pixel(0, y-1).red + img.get_pixel(1,y-1).red + img.get_pixel(1, y+1).red + img.get_pixel(0, y+1).red + img.get_pixel(1,y).red + img_p.red) / 6
                img_total_green = (img.get_pixel(0, y - 1).green + img.get_pixel(1, y - 1).green + img.get_pixel(1,y + 1).green + img.get_pixel(0, y + 1).green + img.get_pixel(1, y).green + img_p.green) / 6
                img_total_blue = (img.get_pixel(0, y - 1).blue + img.get_pixel(1, y - 1).blue + img.get_pixel(1,y + 1).blue + img.get_pixel(0, y + 1).blue+ img.get_pixel(1, y).blue + img_p.blue) / 6
                b_img_p1.red = img_total_red
                b_img_p1.green = img_total_green
                b_img_p1.blue = img_total_blue
            elif x == img.width-1:
                # Get right edge's pixels (without two corners)
                img_total_red = (img.get_pixel(img.width-1, y-1).red + img.get_pixel(img.width-2, y - 1).red + img.get_pixel(img.width-2,y).red + img.get_pixel(img.width-2, y + 1).red + img.get_pixel(img.width-1, y+1).red + img_p.red) / 6
                img_total_green = (img.get_pixel(img.width - 1, y - 1).green + img.get_pixel(img.width - 2,y - 1).green + img.get_pixel(img.width - 2, y).green + img.get_pixel(img.width - 2, y + 1).green + img.get_pixel(img.width - 1,y + 1).green + img_p.green) / 6
                img_total_blue = (img.get_pixel(img.width-1, y-1).blue + img.get_pixel(img.width-2, y - 1).blue + img.get_pixel(img.width-2,y).blue + img.get_pixel(img.width-2, y + 1).blue + img.get_pixel(img.width-1, y+1).blue + img_p.blue) / 6
                b_img_p1.red = img_total_red
                b_img_p1.green = img_total_green
                b_img_p1.blue = img_total_blue
            else:
                # Inner pix
                img_total_red = (img.get_pixel(x-1, y).red + img.get_pixel(x+1, y).red + img.get_pixel(x-1, y-1).red + img.get_pixel(x, y - 1).red + img.get_pixel(x + 1,y - 1).red + img.get_pixel(x - 1,y + 1).red+img.get_pixel(x,y + 1).red +img.get_pixel(x + 1,y + 1).red + img_p.red) / 9
                img_total_green = (img.get_pixel(x-1, y).green + img.get_pixel(x+1, y).green + img.get_pixel(x - 1,y - 1).green + img.get_pixel(x, y - 1).green + img.get_pixel(x + 1, y - 1).green + img.get_pixel(x - 1, y + 1).green + img.get_pixel(x, y + 1).green + img.get_pixel(x + 1, y + 1).green + img_p.green) / 9
                img_total_blue = (img.get_pixel(x-1, y).blue + img.get_pixel(x+1, y).blue + img.get_pixel(x-1, y-1).blue + img.get_pixel(x, y - 1).blue + img.get_pixel(x + 1,y - 1).blue + img.get_pixel(x - 1,y + 1).blue+img.get_pixel(x,y + 1).blue +img.get_pixel(x + 1,y + 1).blue + img_p.blue) / 9
                b_img_p1.red = img_total_red
                b_img_p1.green = img_total_green
                b_img_p1.blue = img_total_blue
    return new_img


def main():
    """
    blur the picture
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
