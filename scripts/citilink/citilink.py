import pandas as pd
import numpy as np
import json
with open('/home/akozlov/Загрузки/citi.json') as f:
    templates = json.load(f)
js1=[]
js2 = []
ids = templates[0].keys()
for i in ids:
    js1.append(i)
# ids = templates[1].keys()
# for i in ids:
#     js2.append(i)
# js = list(set(js1 + js2))
top_players = pd.read_excel('/home/akozlov/Загрузки/Шаблоны для тест проверки/Citi/Материнские платы.xlsx', 'Items')
# top_players1 = pd.read_excel('/home/akozlov/Загрузки/Шаблоны для тест проверки/Citi/Карты памяти и флешки.xlsx', 'Items')
# top_players2 = pd.read_excel('/home/akozlov/Загрузки/Шаблоны для тест проверки/Citi/Шаблон Флеш-диски USB.xlsx', 'Items')
hed = top_players.values[0].tolist ()
# hed1 = top_players1.values[0].tolist ()
# hed2= top_players2.values[0].tolist ()
result = list(set(js1) - set(hed))
result2 = list(set(hed) - set(js1))
# result = list(set(hed1) - set(hed2))
print(f'Отличие в: {result}')
# print(result2)
# print(len(js2))