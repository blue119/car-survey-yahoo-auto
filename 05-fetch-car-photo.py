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
    _df = None
    _d_dir = None

    for _d in os.listdir(_dir):
        if not os.path.isdir('{}/{}'.format(_dir, _d)):
            continue
        _df = '{}/{}/detail.html'.format(_dir, _d)
        break

    print('Parsing {}'.format(_df))
    with open(_df, 'r+') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    for img in soup.find_all('img', class_='gabtn'):
        if not img.get('src'):
            continue

        fn = '{}/{}'.format(_dir, img['src'].split('/')[-1])
        if os.path.exists(fn):
            continue

        c = requests.get(img['src'])
        assert c.status_code == 200

        print('Download {}'.format(fn))
        with open(fn, 'wb') as f:
            f.write(c.content)

