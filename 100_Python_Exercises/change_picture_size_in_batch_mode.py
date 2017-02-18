"""

change_picture_size_in_batch_mode.py

描述：批量修改目录中图片的分辨率，使其不大于规定大小。此例中图片大小为iPhone5分辨率大小。
     其中读取的目录为 get_picture_from_url.py 程序运行后产生的目录中图片。

"""

import os
from PIL import Image

iPhone5_WIDTH = 1136
iPhone5_HIGHT = 640


def change_picture_size_to(from_path, to_path, max_width=iPhone5_WIDTH, max_height=iPhone5_HIGHT):
    from_image = Image.open(from_path)
    width, hight = from_image.size

    if width > max_width:
        hight = max_width * hight // width
        width = max_width
    if hight > max_height:
        width = max_height * width // hight
        hight = max_height

    to_image = from_image.resize((width, hight), Image.ANTIALIAS)
    to_image.save(to_path)


def walk_dir_and_resize(from_path):
    for root, dirs, files in os.walk(from_path):
        for file in files:
            if file.lower().endswith('jpg'):
                path_dst = os.path.join(root, file)
                pic_name = 'iPhone5_' + file
                change_picture_size_to(path_dst, pic_name)

if __name__ == '__main__':
    os.chdir('/Users/richardsen/PycharmProjects/Python_Exercises/Test_Data/pic_collection')
    walk_dir_and_resize('./')
