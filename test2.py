#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup as BS
import re


def get_hanvi(word):
    # word = '%E8%BF%98'
    # # word = 'aaaaa'
    link = 'http://hvdic.thivien.net/whv/' + word
    response = requests.get(link)
    soup = BS(response.content, "lxml")
    print(soup.prettify())

    hanvi_list = []
    count = 0

    no_result = soup.body.findAll(text=re.compile(u'Không có kết quả phù hợp'))

    if len(no_result) == 0:
        hanvi_word_count_string = soup.body.findAll(text=re.compile(u'kết quả'))[0]
        count = re.findall('\d+', hanvi_word_count_string)[0]
        # print count
        # for itemText in soup.find_all('div', attrs={'class': 'info'}):
        #     # hanvi_word = itemText.text
            # print itemText.text

        for item in soup.findAll('span', attrs={'class': 'hvres-goto-link'}):
            hanvi_list.append(item.string)
    else:
        pass
    if len(hanvi_list) >= 2:  # IF 2 words get errors
        hanvi_list = hanvi_list[:len(hanvi_list) / 2]
    hanvi_list.insert(0, str(count))  # insert to count to first of list
    hanvi_word = ",".join(hanvi_list)
    return hanvi_word

# x = get_hanvi('%E8%BF%98')
x = get_hanvi('难')

print x
