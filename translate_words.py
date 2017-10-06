#!/usr/bin/env python
# -*- coding: utf-8 -*-


import csv
import requests
import re
from mtranslate import translate
from xpinyin import Pinyin
from bs4 import BeautifulSoup as BS


def get_hanvi(word):
    # word = '%E8%BF%98'
    # # word = 'aaaaa'
    link = 'http://hvdic.thivien.net/whv/' + word

    response = requests.get(link)
    soup = BS(response.content, "lxml")
    # print(soup.prettify())

    hanvi_list = []
    count = 0

    no_result = soup.body.findAll(text=re.compile(u'Không có kết quả phù hợp'))

    if len(no_result) == 0:
        hanvi_word_count_string = soup.body.findAll(text=re.compile(u'kết quả'))[0]
        count = re.findall('\d+', hanvi_word_count_string)[0]
        # print count
        # for itemText in soup.find_all('div', attrs={'class': 'info'}):
        #     # hanvi_word = itemText.text
        #     # print itemText.text

        for item in soup.findAll('span', attrs={'class': 'hvres-goto-link'}):
            hanvi_list.append(item.string)

    if len(hanvi_list) >= 2:  # IF 2 words get errors
        hanvi_list = hanvi_list[:len(hanvi_list) / 2]
    # hanvi_list.insert(0, str(count))  # insert to count to first of list
    hanvi_word = ",".join(hanvi_list)
    return hanvi_word



def main():
    with open('input.csv', 'r') as f:
        reader = csv.reader(f)
        word_list = list(reader)
    # print word_list

    translate_list = []  # Create list

    for word in word_list:
        key = word[0].decode('utf-8')
        hanvi_word = ''

        p = Pinyin()
        pinyin_word = p.get_pinyin(key, ' ', show_tone_marks=True)

        traditional_word = translate(word[0], 'zh-TW')
        if traditional_word == key:
            simple_word_check = translate(word[0], 'zh-CN')
            if simple_word_check != traditional_word:
                traditional_word = key
                key = simple_word_check
            else:
                traditional_word = ''

        english_word = translate(word[0], 'en')
        vietnamese_word = translate(word[0], 'vi')

        hanvi_word = get_hanvi(word[0])
        hanvi_list = []

        if not hanvi_word:
            for each in key:
                hanvi_list.append(get_hanvi(each))
            hanvi_word = '-'.join(hanvi_list)

        # print type(key), type(traditional_word), type(pinyin_word), type(english_word), type(vietnamese_word)
        print key + "\\" + traditional_word + "\\" + pinyin_word + "\\" + hanvi_word + "\\" + english_word + "\\" + vietnamese_word
        temp_list = [key,
                     traditional_word,
                     pinyin_word,
                     english_word,
                     hanvi_word,
                     vietnamese_word]
        # print temp_listkh
        translate_list.append(temp_list)


if __name__ == '__main__':
    main()
