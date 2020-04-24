import sys

SEP = '\t'
power_key = set()
drive_key = set()
chassis_key = set()
body_key = set()
other_key = set()
exterior_key = set()
interior_key = set()
media_key = set()
convenient_key = set()
safety_key = set()

with open('all_car_detail', 'r+') as f:
    all_car_detail = eval(f.read())

for name, model in all_car_detail.items():
    for model_name, model_detail in model.items():
        power_key = power_key.union(model_detail['規格']['動力'].keys())
        drive_key = drive_key.union(model_detail['規格']['傳動'].keys())
        chassis_key = chassis_key.union(model_detail['規格']['底盤'].keys())
        body_key = body_key.union(model_detail['規格']['車體'].keys())
        other_key = other_key.union(model_detail['規格']['其他'].keys())
        exterior_key = exterior_key.union(model_detail['配備']['外觀'])
        interior_key = interior_key.union(model_detail['配備']['內裝'])
        media_key = media_key.union(model_detail['配備']['影音'])
        convenient_key = convenient_key.union(model_detail['配備']['便利'])
        safety_key = safety_key.union(model_detail['配備']['安全'])

power_key = ['動力型式', '引擎型式', '排氣量', '最大馬力', '最大扭力',
             '壓縮比', '系統總合輸出', '馬達出力']
drive_key = ['驅動型式', '變速系統']
chassis_key = ['前輪懸吊', '後輪懸吊', '煞車型式', '輪胎尺碼']
body_key = ['車身型式', '車門數', '座位數', '車長', '車寬', '車高', '車重',
            '軸距', '標準行李箱容量', '後座傾倒行李箱容量']
other_key = ['市區油耗', '高速油耗', '平均油耗', '燃料費', '牌照稅', '油箱容量']

header = ['car', 'model', 'price'] + power_key + drive_key + chassis_key + body_key
header = header + other_key + list(exterior_key) + list(interior_key)
header = header + list(media_key) + list(convenient_key) + list(safety_key)
print(SEP.join(header))

for name, model in all_car_detail.items():
    with open('data/{0}/{0}.data'.format(name), 'r+') as f:
        model_price = {}
        for n in eval(f.read()):
            # only keep {<model>: <price>, }
            model_price[n[1]] = float(n[-1])
        model_price = sorted(model_price.items(), key=lambda a: a[1])

    first_line = True

    #  for model_name, model_detail in model.items():
    for model_name, price in model_price:
        L = []
        model_detail = model[model_name]
        power = model_detail['規格']['動力']
        drive = model_detail['規格']['傳動']
        chassis = model_detail['規格']['底盤']
        body = model_detail['規格']['車體']
        other = model_detail['規格']['其他']
        exterior = model_detail['配備']['外觀']
        interior = model_detail['配備']['內裝']
        media = model_detail['配備']['影音']
        convenient = model_detail['配備']['便利']
        safety = model_detail['配備']['安全']

        if first_line:
            L += [name, model_name, str(price)]
        else:
            L += ['', model_name, str(price)]
        first_line = False

        for k in power_key:
            L.append(power.get(k, ''))

        for k in drive_key:
            L.append(drive.get(k, ''))

        for k in chassis_key:
            L.append(chassis.get(k, ''))

        for k in body_key:
            L.append(body.get(k, ''))

        for k in other_key:
            L.append(other.get(k, ''))

        for k in exterior_key:
            L.append('O' if k in exterior else 'X')

        for k in interior_key:
            L.append('O' if k in interior else 'X')

        for k in media_key:
            L.append('O' if k in media else 'X')

        for k in convenient_key:
            L.append('O' if k in convenient else 'X')

        for k in safety_key:
            L.append('O' if k in safety else 'X')

        print(SEP.join(L))

