"""

009-get_main_body_from_url.py

描述：找到 URL 中的正文

URL：https://github.com/Yixiaohan/show-me-the-code

"""

from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl


def get_main_body_from(url):
    context = ssl._create_unverified_context()
    with urlopen(url, context=context) as html:
        soup = BeautifulSoup(html.read(), 'lxml')

    print(soup.body.text)

if __name__ == '__main__':
    get_main_body_from('https://github.com/Yixiaohan/show-me-the-code')
