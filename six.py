goods = []
# properties = {'название': '', 'цена': '', 'количество': '', 'ед': ''}
analytics = {'название': [], 'цена': [], 'количество': [], 'ед': []}
n = 1
while True:
    name = str(input("Введите наименование товара: "))
    cost = float(input("Введите стоимость товара: "))
    value = int(input("Введите количество товара: "))
    metric = str(input("Введите единицу измерения товара: "))
    goods.append((n, {'название': name, 'цена': cost, 'количество': value, 'ед': metric}))
    analytics['название'].append(name)
    analytics['цена'].append(cost)
    analytics['количество'].append(value)
    analytics['ед'].append(metric)
    if input("Для завершения нажмите 'Q', для ввода следующей позиции нажмите любую клавишу.") == 'Q':
        break
    else:
        n += 1

print(analytics)
