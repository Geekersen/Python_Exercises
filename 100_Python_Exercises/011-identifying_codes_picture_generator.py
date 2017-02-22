"""

011-identifying_codes_picture_generator.py

描述：生成验证码图片

"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
from random import choices, randint
from string import ascii_letters

IMAGE_MODE = 'RGB'
IMAGE_BG_COLOR = (255, 255, 255)
IMAGE_FONTS = '../Test_Data/Deng.ttf'
IMAGE_FONTS_SIZE = 80
CODE_LEN = 4


def random_color():
    return randint(0, 256), randint(0, 256), randint(0, 256)


def identifying_code_picture_generatro(width=400, hight=200, chance=10):
    im = Image.new(IMAGE_MODE, (width, hight), IMAGE_BG_COLOR)
    im = print_identifying_codes_to(im)
    im = print_noise_to(im, chance)
    im = im.filter(ImageFilter.BLUR)
    im.show()


def print_identifying_codes_to(im):
    draw = ImageDraw.Draw(im)
    identifying_codes = "".join(choices(ascii_letters, k=CODE_LEN))
    font = ImageFont.truetype(IMAGE_FONTS, IMAGE_FONTS_SIZE)
    font_width, font_hight = font.getsize(identifying_codes)
    x = (im.width - font_width) / 2
    y = (im.height - font_hight) / 2
    for code in identifying_codes:
        draw.text((x, y), code, fill=random_color(), font=font)
        x += font_width / CODE_LEN
    del draw
    return im


def print_noise_to(im, chance):
    draw = ImageDraw.Draw(im)
    for x in range(im.width):
        for y in range(im.height):
            if chance >= randint(0, 100):
                draw.point((x, y), fill=random_color())
    del draw
    return im

if __name__ == '__main__':
    identifying_code_picture_generatro()
