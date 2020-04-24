#  https://bit.ly/2UhPgiR

from pprint import pformat
import os
from glob import glob

DATA_DIR = './data'
car_datum = [p.replace(DATA_DIR + '/', '') for p in glob('{}/*'.format(DATA_DIR))]

_all_car_detail = {}
for p in car_datum:
    _dir = '{0}/{1}'.format(DATA_DIR, p)
    #  _brief_f = '{0}/{1}/{1}.data'.format(DATA_DIR, p)
    _detail_datum = []

    #  with open('{}'.format(_brief_f)) as f:
        #  _brief = f.read()

    for _d in os.listdir(_dir):
        if not os.path.isdir('{}/{}'.format(_dir, _d)):
            continue
        _detail_datum.append('{}/{}/detail.data'.format(_dir, _d))

    _all_car_detail[p] = _model = {}
    for _dd in _detail_datum:
        #  print('Parsing {}'.format(_df))
        if not os.path.exists(_dd):
            print('{} not found.'.format(_dd))
            continue

        with open(_dd, 'r+') as f:
            _d = eval(f.read())

        _model[_dd.split('/')[-2]] = _d

with open('./all_car_detail', 'w+') as f:
    f.write(str(_all_car_detail))

#  with open('./all_car_detail', 'w+') as f:
    #  f.write(pformat(_all_car_detail, indent=4))
