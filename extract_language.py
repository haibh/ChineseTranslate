#!/usr/bin/env python
# -*- encoding: utf8 -*-

import re
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
        meaning_ch_simple = ''
        meaning_ch_traditional = ''
        meaning_vi = ''
        meaning_pinyin = ''
        meaning_en = ''

        if '-' in ''.join(sentence):
            full_string = ','.join(sentence).decode('utf-8')
            print full_string

            meaning_ch_simple = re.findall(ur'[\u4e00-\u9fff]+', full_string)[0]  # get first CHINA word

            meaning_ch_traditional = translate(meaning_ch_simple.encode('utf-8'), 'zh-TW')
            if meaning_ch_simple == meaning_ch_traditional:
                meaning_ch_simple_check = translate(meaning_ch_simple.encode('utf-8'),
                                                    'zh-CN')  # If traditional, swap simple & traditional
                if meaning_ch_simple_check != meaning_ch_simple:
                    meaning_ch_traditional = meaning_ch_simple
                    meaning_ch_simple = meaning_ch_simple_check
            else:
                meaning_ch_traditional = ''

            # pinyin_and_en = ','.join(sentence).split('-')[0].decode('utf-8')
            # pinyin_and_en = pinyin_and_en.split(' ', 2)[2]
            first_word = ','.join(sentence).split(' ')[0]
            meaning_pinyin = first_word.split('．')[1].decode('utf-8')
            meaning_en = translate(meaning_ch_simple.encode('utf-8'), 'en')

            meaning_vi = ','.join(sentence).split('-')[2].lstrip(' ').decode(
                'utf-8')
            meaning_han = ','.join(sentence).split('-')[1].lstrip(' ').decode(
                'utf-8')

            print meaning_ch_simple \
                  + '\\' + meaning_ch_traditional \
                  + '\\' + meaning_pinyin \
                  + '\\' + meaning_han \
                  + '\\' + meaning_vi \
                  + '\\' + meaning_en


if __name__ == '__main__':
    main()
