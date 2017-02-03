"""

activation_code_generator.py

描述：随机生成200个20个字符的激活码

"""


import secrets


def activation_code_generator(key_bytes=20, key_nums=1):
    key_list = []
    while len(key_list) < key_nums:
        key_list.append(secrets.token_urlsafe(key_bytes))
    return tuple(key_list)

if __name__ == '__main__':
    key_list = activation_code_generator(key_bytes=20, key_nums=200)
    print(key_list)
