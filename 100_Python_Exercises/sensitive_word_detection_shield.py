"""

sensitive_word_detection_shield.py

描述：敏感词文本文件 filtered_words.txt ，当用户输入敏感词时，将敏感词用 ** 代替。

"""

import os


def sensitive_word_detection_shield(detected_words, filter_words):
    for word in filter_words:
        detected_words = detected_words.replace(word, len(word) * '*')
    print(detected_words)

if __name__ == '__main__':
    os.chdir('/Users/richardsen/PycharmProjects/Python_Exercises/Test_Data')
    with open('filtered_words') as fileter_file_object:
        fileter_file = fileter_file_object.read()

    filter_words = fileter_file.split('\n')
    while True:
        words_in = input()
        if words_in == '^Z':
            break
        sensitive_word_detection_shield(words_in, filter_words)
