import cv2
import numpy as np
from PIL import Image



def create_pixels(file_name):
    # reading image pixels
    pixels = cv2.imread(file_name)
    return pixels


# to create an image from pixels array
def create_image_pixels(pixels, file_name):
    img = Image.new('RGB', (len(pixels[0]), len(pixels)))
    height = len(pixels)
    width = len(pixels[0])

    for i in range(width):
        for j in range(height):
            # pixels[i][j][0] = 123
            img.putpixel((i, j), tuple(pixels[j][i][::-1]))
    img.save('2' + file_name)


def encode2(img, content):
    file = open(img, "rb")

    imgC = file.read()
    file.close()

    file2 = open(img, "wb")
    file2.write(imgC)
    file2.write(bytes((content + "?").encode()))
    file2.write(bytes((str(len(content))).encode()))
    file.close()
    file2.close()

def decode2(img):
    file = open(img, "rb")
    content = file.read()

    size = ""
    for i in content[::-1]:
        if i == 63:
            break
        else:
            size = chr(i) + size
    size = int(size)

    data = ""
    for i in range(size):
        data = (chr(content[len(content) - 1 - i - 1 - (size//10 + 1)])) + data

    return data

def encode(pixels, content):
    print(pixels)
    pixels[-1][-1][-1] = len(content)  # storing len of hidden data into first pixel
    i_content = 0
    for row in pixels:
        if i_content == len(content):
            break
        for pixel in row:
            if i_content == len(content):
                break
            pixel[-1] = ord(content[i_content])
            i_content += 1

def decode(image_file):
    pixels = create_pixels(image_file)
    size = pixels[-1][-1][-1]

    print("----------------------------")
    print(pixels)
    i_content = 0
    data = ""
    for row in pixels:
        if i_content == size:
            break
        for pixel in row:
            if i_content == size:
                break
            data += chr(pixel[-1])
            i_content += 1
    return data

# main work

# 1 - create pixels array from image file
def menu():
    option = input("Press 1 for encode, 2 for decode, 3 for exit:").strip()

    while not(option == "1" or option == "2" or option == "3"):
        option = input("Press 1 for encode, 2 for decode, 3 for exit:")

    if option == "1":

        # file name from user
        file_name = input("Enter image file name:").strip()

        # data to hide should be in a text file
        data_to_hide = input("Enter file-name containing data to hide:").strip()

        # contents of data-to-hide input file
        i_file = open(data_to_hide, "r")
        content = i_file.read()
        i_file.close()

        encode2(file_name, content)

    elif option == "2":
        # file name from user
        file_name = input("Enter image file name:").strip()

        print(decode2(file_name))

    return option


while menu() != "3":
    pass