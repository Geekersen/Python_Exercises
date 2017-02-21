"""

004-get_picture_from_url.py

描述：将一个网站上的所有的需要的图片全部下载下来，即爬网站的图片。

from url:http://tieba.baidu.com/p/2166231880

"""

import re
import os
import urllib.request


def get_picture_from(url):
    with urllib.request.urlopen(url) as url_obj:
        url_content = url_obj.read()
    pic_name_regular = re.compile(r'src="(.*?\.jpg)" bdwater=')
    pic_list = pic_name_regular.findall(url_content.decode('utf-8'))
    save_picture_from(pic_list)


def save_picture_from(pic_list):
    os.mkdir('/Users/richardsen/PycharmProjects/Python_Exercises/Test_Data/pic_collection')
    os.chdir('/Users/richardsen/PycharmProjects/Python_Exercises/Test_Data/pic_collection')
    for i in range(len(pic_list)):
        pic_name = str(i) + '.jpg'
        urllib.request.urlretrieve(pic_list[i], pic_name)
        print('success : ' + pic_name)

if __name__ == '__main__':
    get_picture_from("http://tieba.baidu.com/p/2166231880")