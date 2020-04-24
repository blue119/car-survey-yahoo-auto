#  https://bit.ly/2UhPgiR

import requests
from bs4 import BeautifulSoup
import re
import time
import random
import os
from glob import glob

DATA_DIR = './data'
car_datum = [p.replace(DATA_DIR + '/', '') for p in glob('{}/*'.format(DATA_DIR))]

for p in car_datum:
    _dir = '{0}/{1}'.format(DATA_DIR, p)
    _detail_files = []

    for _d in os.listdir(_dir):
        if not os.path.isdir('{}/{}'.format(_dir, _d)):
            continue
        _detail_files.append('{}/{}/detail.html'.format(_dir, _d))

    for _df in _detail_files:
        _df_data = _df.replace('detail.html', 'detail.data')
        if os.path.exists(_df_data):
            continue

        print('Parsing {}'.format(_df))
        if not os.path.exists(_df):
            print('{} not found.'.format(_df))
            continue

        with open(_df, 'r+') as f:
            _page = f.read()

        _spec = {}
        soup = BeautifulSoup(_page, 'html.parser')

        # spec-wrapper sector
        _soup = BeautifulSoup(str(soup.find('div', class_='spec-wrapper')), 'html.parser')
        s = _soup.find('div', class_='spec-wrapper').find('div', class_='title')
        _title = s.text.strip()

        _spec[_title] = _sub_title = {}
        while True:
            # find sub item
            s = s.find_next('label', class_='gabtn')
            if not s:
                break
            _title = s.text.strip()

            _items = {}
            for item in s.find_next('ul').find_all('li'):
                k, v = [ i.text.strip() for i in item.find_all('span') ]
                _items[k] = v

            _sub_title[_title] = _items

        # spec-wrapper spec-right sector
        soup = BeautifulSoup(str(soup.find('div', class_='spec-wrapper spec-right')), 'html.parser')
        s = soup.find('div', class_='title')
        _title = s.text.split()[0].strip()

        _spec[_title] = _sub_title = {}
        while True:
            s = s.find_next('label')
            if not s:
                break
            _title = s.text.strip()
            _items = [i.span.text.strip() for i in s.find_next('ul').find_all('li')]
            _sub_title[_title] = _items

        with open(_df_data, 'w+') as f:
            f.write(str(_spec))
