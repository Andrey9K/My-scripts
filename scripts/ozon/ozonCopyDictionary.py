import pyperclip
import requests
import json
import numpy as np
# Установить 'sudo apt-get install xclip' для Linux
# Установить 'pip install pyperclip' Установить библиотеку

# Впишите category_id , type_id и attribute_id из дерева OZON
category_id=24692739
type_id=97651
attribute_id=21596

url = "https://api-seller.ozon.ru/v1/description-category/attribute/values"

payload = json.dumps({
  "description_category_id": f'{category_id}',
  "type_id": f"{type_id}",
  "attribute_id": f'{attribute_id}',
  "language": "DEFAULT",
  "last_value_id": 0,
  "limit": 5000
})
headers = {
  'Client-Id': '77899',
  'Api-Key': '67de6a35-eaaf-4b08-ba84-62f525a6e0c8',
  'Content-Type': 'application/json',
  'Cookie': '__cf_bm=azFLDMXN_zGBr6jRxduNsyhDCJ9vcZ91ofwDHtbHPFQ-1698668209-0-AfcWPpQInz5rGPisfY7/o7oUi8DGwthvok5Q2L9sCQReOMdrHRaR8wGXOuY5jqD2cmhtChS1SeH8qrb5DGsrmos='
}

response = requests.request("POST", url, headers=headers, data=payload)
# print(response.json())
data=response.json()
templates = data
js1=[]  
if   'result' in templates: 
    if isinstance(templates['result'], list):
                s= templates['result']
                for t in range(0,len(s)):            
                    s1= s[t]
                    s2=s1['id']
                    s3=s1['value']                    
                    js1.append(f'{s3}	{s2}')
    else: 
        print('Не корректный Json')
else:
        print('Не корректный Json')

result=np.array(js1)

result1 = '\n'.join(map(str, result))


# # # Запись результата в буфер обмена
pyperclip.copy(result1)

# # # Проверка, что результат записан в буфер обмена
copied_result = pyperclip.paste()
if copied_result != None and copied_result!= '':
      print('Атрибуты скопированы в буфер обмена')
else:
      print('Ошибка (строка для копирования в буфер обмена Отсутствует)')
# print("Результат: ", copied_result)