#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mtranslate import translate
from xpinyin import Pinyin
import csv


def main():
    with open('input.csv', 'r') as f:
        reader = csv.reader(f, skipinitialspace=True)
        sentences_list = list(reader)
    # print sentences_list

    translate_list = []  # Create list

    for sentence in sentences_list:
        # key = sentence[0].decode('utf-8')
        full_string = ','.join(sentence)
        key = full_string.decode('utf-8')

        p = Pinyin()
        pinyin_word = p.get_pinyin(key, ' ', show_tone_marks=True)

        traditional_word = translate(full_string, 'zh-TW')
        if traditional_word == key:
            traditional_word = ''

        english_word = translate(full_string, 'en')
        vietnamese_word = translate(full_string, 'vi')

        # print type(key), type(traditional_word), type(pinyin_word), type(english_word), type(vietnamese_word)
        print key
        if traditional_word:
            print traditional_word
        print pinyin_word
        print english_word
        print vietnamese_word
        temp_list = [key,
                     traditional_word,
                     pinyin_word,
                     english_word,
                     vietnamese_word]
        translate_list.append(temp_list)


if __name__ == '__main__':
    main()
