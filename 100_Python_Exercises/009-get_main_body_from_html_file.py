"""

009-get_main_body_from_html_file.py

描述：找到 URL 中的正文

URL：https://github.com/Yixiaohan/show-me-the-code

"""

from bs4 import BeautifulSoup
from os import chdir


def get_main_body_from(html_file):
    with open(html_file) as html:
        soup = BeautifulSoup(html, 'lxml')

    print(soup.body.text)

if __name__ == '__main__':
    chdir('../Test_Data')
    get_main_body_from('show-me-the-code.html')
