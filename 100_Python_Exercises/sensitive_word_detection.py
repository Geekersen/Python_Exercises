"""

sensitive_word_detection.py

描述：敏感词文本文件 filtered_words.txt ，当用户输入敏感词时，输出 freedom ，否则输出 human rights

"""

import os


def sensitive_word_detection(detected_word, filter_words):
    for word in filter_words:
        if word in detected_word:
            break
    else:
        print('human rights')
        return False
    print('freedom')
    return True


if __name__ == '__main__':
    os.chdir('/Users/richardsen/PycharmProjects/Python_Exercises/Test_Data')
    with open('filtered_words') as fileter_file_object:
        fileter_file = fileter_file_object.read()

    filter_words = fileter_file.split('\n')
    while True:
        word_in = input()
        if word_in == '^z':
            break
        sensitive_word_detection(word_in, filter_words)
