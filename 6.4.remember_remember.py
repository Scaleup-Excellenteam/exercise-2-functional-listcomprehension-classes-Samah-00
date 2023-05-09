# run this command in the terminal in order to be able to use the Image module in the code:
# pip install Pillow

# from the "Python Imaging Library" import the "Image" module
from PIL import Image


def decrypt_message(image_path):
    image = Image.open(image_path)
    # get the width and height of the image using the size attribute of Image
    width, height = image.size
    message = ''
    # iterate over each column of the image
    for x in range(width):
        black_pixel = None
        # for each column, iterate over each row of pixels and check if the pixel is black
        for y in range(height):
            pixel = image.getpixel((x, y))
            if pixel == 1:  # black = 1 in pixels
                black_pixel = y
                break
        # concatenate all the characters together to form the decrypted message
        # use the chr() function to convert the numerical value to its corresponding ASCII character
        if black_pixel is not None:
            message += chr(black_pixel)
    return message


message = decrypt_message('resources/code.png')
print(message)  # the output I received: "Place gunpowder beneath the House of Lords. 11/05/1605"
