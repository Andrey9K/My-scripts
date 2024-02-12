import pyperclip
import requests
import json
import numpy as np
# Установить 'sudo apt-get install xclip' для Linux
# Установить 'pip install pyperclip' Установить библиотеку

# Впишите category_id и type_id из дерева OZON
category_id=24692739
type_id=97651


url = "https://api-seller.ozon.ru/v1/description-category/attribute"
payload = json.dumps({
"description_category_id": f'{category_id}',
"type_id": f'{type_id}',
"language": "DEFAULT"
})
headers = {
'Client-Id': '77899',
'Api-Key': '67de6a35-eaaf-4b08-ba84-62f525a6e0c8',
'Content-Type': 'text/plain',
'Cookie': '__cf_bm=zBIfnu0fjArVn6K_OsxSXfq.zy8lDVG5tcuIFOkS02w-1698179182-0-AanjbwikPZTpzfRXbf5x4GHbDIuhOSxpqd4Ewr80udCehPwPgvlmMiIREm6xvkoan2HVPZV7J0oOg+exMi1or9U='
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
                    s3=s1['name']
                    s4=s1['type']
                    s5=s1['is_required']
                    if s5 == False:
                              s5='ЛОЖЬ'
                    if s5 == True:
                              s5='ИСТИНА'
                    s6=s1['is_collection']
                    if s6 == False:
                              s6='ЛОЖЬ'
                    if s6 == True:
                              s6='ИСТИНА'                    
                    s7=s1['dictionary_id']
                    js1.append(f'{s2}	{s3}	{s4}	{s5}	{s6}	{s7}')
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