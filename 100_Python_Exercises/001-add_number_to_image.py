"""

001-add_number_to_image.py

描述：在图片的右上角添加一个数字

"""

from PIL import Image, ImageDraw, ImageFont


def add_number_to(image):
    draw = ImageDraw.Draw(image)
    number_size = 100
    number_font = ImageFont.truetype("C:\\Windows\\Fonts\\SourceCodePro-Semibold.ttf", size=number_size)
    number_color = "#ff0000"
    width, height = image.size
    draw.text((width - 150, 0), '99', font=number_font, fill=number_color)
    image.save("D:\\Code\\testdata\\result.jpg", "jpeg")

    return 0

if __name__ == '__main__':
    img = Image.open("D:\\Code\\testdata\\test.jpg")
    add_number_to(img)
