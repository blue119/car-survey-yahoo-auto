#  https://bit.ly/2UhPgiR

import requests
from bs4 import BeautifulSoup
import re
import time
import random
import os

car_pages = set(['https://autos.yahoo.com.tw/new-cars/model/ford-focus-4d-2020',
                'https://autos.yahoo.com.tw/new-cars/model/hyundai-elantra-2020',
                'https://autos.yahoo.com.tw/new-cars/model/mazda-3-4d-2020',
                'https://autos.yahoo.com.tw/new-cars/model/toyota-corolla-altis-2020',
                'https://autos.yahoo.com.tw/new-cars/model/ford-focus-5d-2020',
                'https://autos.yahoo.com.tw/new-cars/model/mazda-3-5d-2020',
                'https://autos.yahoo.com.tw/new-cars/model/toyota-auris-2020',
                'https://autos.yahoo.com.tw/new-cars/model/volkswagen-golf-2020',
                'https://autos.yahoo.com.tw/new-cars/model/toyota-camry-2020',
                'https://autos.yahoo.com.tw/new-cars/model/mazda-6-2020',
                'https://autos.yahoo.com.tw/new-cars/model/subaru-levorg-2020',
                'https://autos.yahoo.com.tw/new-cars/model/mazda-6-wagon-2020',
                'https://autos.yahoo.com.tw/new-cars/model/toyota-rav4-2020',
                'https://autos.yahoo.com.tw/new-cars/model/skoda-karoq-2020',
                'https://autos.yahoo.com.tw/new-cars/model/ford-kuga-2020',
                'https://autos.yahoo.com.tw/new-cars/model/honda-cr-v-2020',
                'https://autos.yahoo.com.tw/new-cars/model/mazda-cx-5-2020',
                'https://autos.yahoo.com.tw/new-cars/model/mitsubishi-outlander-2020',
                'https://autos.yahoo.com.tw/new-cars/model/mitsubishi-eclipse-cross-2020',
                'https://autos.yahoo.com.tw/new-cars/model/nissan-x-trail-2020',
                'https://autos.yahoo.com.tw/new-cars/model/volkswagen-tiguan-2020',
                'https://autos.yahoo.com.tw/new-cars/model/subaru-xv-2020',
                'https://autos.yahoo.com.tw/new-cars/model/subaru-forester-2020',
                'https://autos.yahoo.com.tw/new-cars/model/subaru-outback-2020',
                'https://autos.yahoo.com.tw/new-cars/model/peugeot-308-sw-2020',
                'https://autos.yahoo.com.tw/new-cars/model/peugeot-308-2020',
                'https://autos.yahoo.com.tw/new-cars/model/peugeot-3008-suv-2020',
                'https://autos.yahoo.com.tw/new-cars/model/hyundai-tucson-2020',
                'https://autos.yahoo.com.tw/new-cars/model/kia-sportage-2020',
                'https://autos.yahoo.com.tw/new-cars/model/kia-sorento-2020',
                'https://autos.yahoo.com.tw/new-cars/model/hyundai-santa-fe-2020',
                'https://autos.yahoo.com.tw/new-cars/model/peugeot-5008-suv-2020',
                'https://autos.yahoo.com.tw/new-cars/model/skoda-kodiaq-2020',
                'https://autos.yahoo.com.tw/new-cars/model/volkswagen-tiguan-allspace-2020',
                'https://autos.yahoo.com.tw/new-cars/model/luxgen-urx-2020',
                'https://autos.yahoo.com.tw/new-cars/model/citroen-c5-aircross-2020',
                'https://autos.yahoo.com.tw/new-cars/model/mazda-cx-9-2020',
                'https://autos.yahoo.com.tw/new-cars/model/honda-odyssey-2020',
                'https://autos.yahoo.com.tw/new-cars/model/toyota-sienta-2020',
                'https://autos.yahoo.com.tw/new-cars/model/toyota-prius-alpha-2020',
                'https://autos.yahoo.com.tw/new-cars/model/kia-carens-2020',
                'https://autos.yahoo.com.tw/new-cars/model/volkswagen-sharan-2020',
                'https://autos.yahoo.com.tw/new-cars/model/volkswagen-touran-2020',
                'https://autos.yahoo.com.tw/new-cars/model/citroen-grand-c4-spacetourer-2020',
                'https://autos.yahoo.com.tw/new-cars/model/citroen-berlingo-2020'])

for p in car_pages:
    model_type = p.split('/')[-1]
    dst_file = '{}/{}.data'.format(model_type, model_type)

    if not os.path.exists(model_type):
        os.mkdir(model_type)
    if os.path.exists(dst_file):
        continue

    print('Parsing {}'.format(p))

    ctx = requests.get(p)
    assert ctx.status_code == 200

    soup = BeautifulSoup(ctx.text, 'html.parser')
    model = soup.find('div', class_='model-wrapper')
    m = []
    for sub in model.find_all('a', class_='gabtn', href=re.compile("trim")):
        d = []
        d.append(str(sub).split('href="')[1].split('"')[0])
        d.append(sub.find('div', class_='model-title').text)
        d.append(''.join([b.text for b in sub.find('ul').find_all('li')]))
        d.append(sub.find_all('span')[1].text)
        m.append(d)
    #  print(m)

    with open(dst_file, 'w+') as f:
        f.write(str(m))

    time.sleep(random.randint(1, 5))

