import pyperclip
import requests
import json
import yaml
import numpy as np
# Укажите путь до json файла
with open('/home/akozlov/Загрузки/JSON CATEGORY.json') as f:
    templates = json.load(f)

# Укажите subjectID категории из файла Аналитики
subjectID= 1976

#Укажите список Шаблонов для сбора id 
template=['wbReaderAttributes', 'wbReaderNonArray']


dimensionsmm=[6032538, 6032540, 6032541]
dimensionscm=[90745, 90846, 90849]
base=[14177446, 14177451, 14177452, 14177453, 15000000, 15001135, 15001136, 15001137, 15001138, 15001405, 15001650, 9623, 5023, 6032538, 6032540, 6032541, 90745, 90846, 90849]
basename= ['Код упаковки', 'Бренд', 'Страна производства', 'Описание', 'SKU', 'Наименование', 'Номер декларации соответствия', 'Номер сертификата соответствия', 'Дата регистрации сертификата/декларации', 'Дата окончания действия сертификата/декларации', 'Ставка НДС', 'ИКПУ', 'Гарантийный срок', 'Модель', 'Высота упаковки (мм)', 'Ширина упаковки (мм)', 'Длина упаковки (мм)', 'Ширина упаковки', 'Высота упаковки', 'Длина упаковки', 'Предмет']
basename2= {'Код упаковки':15001706, 'Бренд':14177446, 'Страна производства':14177451, 'Описание':14177452, 'SKU':14177453, 'Наименование':15000000, 'Номер декларации соответствия':15001135, 'Номер сертификата соответствия':15001136, 'Дата регистрации сертификата/декларации':15001137, 'Дата окончания действия сертификата/декларации':15001138, 'Ставка НДС': 15001405, 'ИКПУ':15001650, 'Гарантийный срок':9623, 'Модель':5023}
status=[]
jscat=[]
dicttemplate={}
for o in template:    
    s= templates[o]
    if 'of' not in s:
        print (f'Ошибка') 
    else:        
        lo=s['of']        
        if isinstance(lo, list):
            for t in range(0,len(lo)):                
                atr=lo[t]
                for key, value in atr.items():                    
                    dicttemplate[key]= ''
                    status.append('Array')                    
        else:            
            atr=lo
            if 'of' in atr:
                atr2=atr['of']
                if isinstance(atr2, list):
                    for t in range(0,len(atr2)):                
                        atr1=atr2[t]
                        for key, value in atr1.items():
                            dicttemplate[key]= ''
                            status.append('Array')
                else: 
                    for key, value in atr2.items():
                        dicttemplate[key]= ''
                        if 'id' not in value:
                            status.append('NonArray')
            else:
                for key, value in atr.items():
                    dicttemplate[key]= ''                
                    if 'id' not in value:
                        status.append('NonArray')
# print(status)                   
if status !=[]:
    if 'Array' in status and 'NonArray' in status:
         print('Происходит преобразование Array и NonArray')
    else:
        if 'Array' in status:
            print('Происходит преобразование Array')
        else: 
            if 'NonArray' in status:
                print('Происходит преобразование NonArray')
else:
    print('Запуск Проверки')        
             
# print(dicttemplate)
nameCategory= ''
nameTempalte=[]
dimensionsAPIcm=[]
dimensionsAPImm=[]
fullnameAPI={}
js1=[]
for key, value in dicttemplate.items():    
    nameAPI={}   
    # print(key)              
    url = f"https://suppliers-api.wildberries.ru/content/v2/object/charcs/{subjectID}"

    payload = ""
    headers = {
    'Authorization': 'Bearer eyJhbGciOiJFUzI1NiIsImtpZCI6IjIwMjMxMDI1djEiLCJ0eXAiOiJKV1QifQ.eyJlbnQiOjEsImV4cCI6MTcxODMxMDQ5OCwiaWQiOiI0NjcwMGY2MS04ODdjLTQwMTYtYTExNy04MDM3MTE4Nzk3YWQiLCJpaWQiOjY0NDk5NDEsIm9pZCI6OTA3MDUwLCJzIjoyLCJzYW5kYm94IjpmYWxzZSwic2lkIjoiYTA2MTFhYWQtZTQyZC00NmVkLTllZWYtNzYzOTM2YjgzZGYyIiwidWlkIjo2NDQ5OTQxfQ.sG6cJHF4h8NDnNuHo8YmZtTfshmRUFNvBSis3gGYBVNZ9DggrDegHMOnQv4xm-dOeKQyyPS41zPhqV8ZPs11Qg'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    # print(response.text)
    data=response.json()
    templates2 = data
    
    
    if   templates2['data'] != None: 
        if isinstance(templates2['data'], list):
                    s= templates2['data']
                    for t in range(0,len(s)):            
                        s1= s[t]
                        s2=s1['charcID']
                        s4=s1['charcType']
                        s3=s1['name']
                        if nameCategory == '':
                            nameCategory=f"{s1['subjectName']} ({s1['subjectID']})"                          
                        fullnameAPI[s3]=s2
                        if s2 in dimensionscm:                            
                            dimensionsAPIcm.append(s2)
                        else:
                            if s2 in dimensionsmm:                                
                                dimensionsAPImm.append(s2)                                                                           
                        if s2 not in base:            
                            nameAPI[s3]=s2
                            if s3 == key:                                
                                # print(s4)
                                if s4 != 4:                           
                                                js1.append(f"""'{s3}':    
    'id': !const    
        value: '{s2}'
        type: int
    'value': 
    """
    )
                                else: 
                                    js1.append(f"""#'{s3}':    
'id': !const    
    value: '{s2}'
    type: int
'value': 
"""
)
                                                           
        else: 
            print(f' Не корректный Json')
    else:
          print(f' Не корректный Json')
    if key not in basename:        
        nameTempalte.append(key)
# print(js1)
print(f'Категория: {nameCategory}\n')       
absent = list(set(nameAPI.keys()) - set(nameTempalte))
extra = list(set(nameTempalte) - set(nameAPI.keys()))
# print(f'Отсутствует: {result}')
# print(f'Лишние: {result1}')
if absent != []:
    print('Отсутствуют:\n')
    for key, value in nameAPI.items():        
        if key in absent:                           
            print(f'{key}: {value}')    
else: 
    print('\nОтсутствующих: Нет')
if extra != []:
    print('\nЛишние из Template:\n')
    for id in extra:        
        print(id)
else:
    print('\nЛишних из Template: Нет')

NotinAPI = list(set(basename2.keys()) - set(fullnameAPI.keys()))

if NotinAPI != []:
    print('\nЛишиний из Base (Добавьте атрибут в wbIgnoredAttributes):')
    NotinAPI=list(set(NotinAPI))    
    for key, value in basename2.items():        
        if key in NotinAPI:                           
            print(f'{key}: {value}')
if dimensionsAPIcm !=[]:
    print(f'\nГАБАРИТЫ: в см  {len(set(dimensionsAPIcm))}шт.\n')
else:
    if dimensionsAPImm !=[]:
        print(f'\nГАБАРИТЫ: в мм  {len(set(dimensionsAPImm))}шт.\n')
    else:
        print('\nГАБАРИТЫ: Ошибка Габаритов упаковки\n')         
result=np.array(js1)

result1 = '\n'.join(map(str, result))

# # # Запись результата в буфер обмена
pyperclip.copy(result1)

# # # Проверка, что результат записан в буфер обмена
copied_result = pyperclip.paste()
if copied_result != None and copied_result!= '':
      print('Атрибуты скопированы в буфер обмена')
else:
      print('Ошибка (строка для копирования пустая)')
# print("Результат: ", copied_result)