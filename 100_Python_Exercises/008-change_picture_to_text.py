"""

008-change_picture_to_text.py

描述：将图片变成字符画

"""

from PIL import Image
from os import chdir

ascii_char = 'qwertyuiopasdfghjklzxcvbnm!@#$%^&*()_+1234567890-={}:,./'


def change_picture_to_text(picture_path):
    picture = Image.open(picture_path)
    picture = picture.resize((200, 200), Image.NEAREST)
    pic_width, pic_hight = picture.size
    text = ''
    for y in range(pic_hight):
        for x in range(pic_width):
            text += get_char_from_pixel(*picture.getpixel((x, y)))
        text += '\n'
    return text


def get_char_from_pixel(r, g, b, alpha=255):
    if alpha == 0:
        return ' '
    gray = int(r * 0.2989 + g * 0.587 + b * 0.114)
    return ascii_char[int(gray * len(ascii_char) / 256)]

if __name__ == '__main__':
    chdir('/Users/richardsen/PycharmProjects/Python_Exercises/Test_Data')
    text = change_picture_to_text('IMG_9129.jpeg')
    with open('IMG_9129', 'wt') as fout:
        fout.write(text)
