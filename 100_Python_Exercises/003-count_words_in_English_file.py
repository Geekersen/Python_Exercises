"""

003-count_words_in_English_file.py

描述：统计任意纯英文文件中单词个数

"""

import os
import re


def count_words_in(file_data):
    words = re.compile(r'([a-zA-Z]+)')

    words_and_times_dict = {}
    for word in words.findall(file_data):
        if word not in words_and_times_dict:
            words_and_times_dict[word] = 1
        else:
            words_and_times_dict[word] += 1

    for word in words_and_times_dict.keys():
        print("{:>10s} : {:<10d}".format(word, words_and_times_dict[word]))

if __name__ == '__main__':

    # 修改工作路径，以能够读取到 Test_Data 目录下的测试文件
    os.chdir('../Test_Data')

    with open('relativity', 'r') as english_file:
        file_data = english_file.read()
        count_words_in(file_data)
