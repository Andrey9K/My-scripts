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
top_players = pd.read_excel('/home/akozlov/Документы/Project/Marvel/pimcore/pimcore/public/excelTemplates/sber/Кондиционер мобильный.xlsx', 'Кондиционер мобильный')
hed = top_players.values[1].tolist ()
result = list(set(js1) - set(hed))
result2 = list(set(hed) - set(js1))
print('Отличие Старого от Нового:')
for i in result:    
    print(f'- {i}')

print('Отличие Нового от Старого:')
for p in result2:    
    print(f'- {p}')
# print(f'Отличие в : {result}')
# for res in result:
#     print(res)
# print(hed)
# print(len(js2))