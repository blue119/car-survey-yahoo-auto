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
    _df = '{0}/{1}.data'.format(_dir, p)
    _ds = []
    if not os.path.exists(_df):
        print('{} is not existed.'.format(_df))
        continue

    with open(_df, 'r+') as f:
        _ds = eval(f.read())
        # ds format:
        #   [[<url>, <model>, <brief>, <price>], ]
        #   [<url>, '典藏型', '5門 5人座|2359cc|168hp@6000rpm|汽油', '88.5']

    for _d in _ds:
        # put the detail to <model> dir
        _detail_url = '{}/spec'.format(_d[0])
        _model_dir = '{}/{}'.format(_dir, _d[1])
        _detail_file = '{}/detail.html'.format(_model_dir)

        if not os.path.exists(_model_dir):
            os.mkdir(_model_dir)

        if not os.path.exists(_detail_file):
            ctx = requests.get(_detail_url)
            assert ctx.status_code == 200

            with open(_detail_file, 'w+') as f:
                f.write(ctx.text)

        print(_d)

    time.sleep(random.randint(1, 5))
