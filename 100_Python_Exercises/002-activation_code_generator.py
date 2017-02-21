"""

002-activation_code_generator.py

描述：随机生成200个20个字符的激活码

"""


import secrets
from pprint import pprint


def activation_code_generator(key_bytes=20, key_nums=1):
    key_set = set()
    while len(key_set) < key_nums:
        key_set.add(secrets.token_urlsafe(key_bytes))
    return tuple(key_set)

if __name__ == '__main__':
    key_set = activation_code_generator(key_bytes=20, key_nums=200)
    pprint(key_set)
