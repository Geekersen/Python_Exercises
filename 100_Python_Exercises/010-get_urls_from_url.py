"""

010-get_urls_from_url.py

描述：得到网站上的所有网络链接

"""
from pprint import pprint
from bs4 import BeautifulSoup
import urllib.request


def get_urls_from(url):
    with urllib.request.urlopen(url) as html:
        page = html.read()

    links = []
    soup = BeautifulSoup(page, 'lxml')
    for link in soup.find_all('a'):
        links.append(link.get('href'))
    return links

if __name__ == '__main__':
    pprint(get_urls_from('http://stackoverflow.com/questions/24075855/python-and-collective-intelligence-keyerror-href'))
