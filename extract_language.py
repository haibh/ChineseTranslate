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

        if '–' in ','.join(sentence):
            full_string = ','.join(sentence).decode('utf-8')
            meaning_ch_simple = re.findall(ur'[\u4e00-\u9fff]+', full_string)[0]
            print full_string
            # print meaning_ch_simple
            # meaning_vi = ','.join(sentence).split('–')[1].decode(
            #     'utf-8')  # split by '-', get second value, convert to readable
            # first_phase = ','.join(sentence).split('–')[0]
            # pinyin_en = first_phase.split('】')[1].decode('utf-8')
            #
            # meaning_pinyin = pinyin_en.split(' ', 1)[0]
            # meaning_en = pinyin_en.split(' ', 1)[1]
            #
            # meaning_ch_traditional = translate(meaning_ch_traditional, 'zh-TW')
            #
            # print meaning_ch_simple + '\\' + meaning_ch_traditional + '\\' + meaning_pinyin + '\\' + meaning_en + '\\' + meaning_vi


if __name__ == '__main__':
    main()
