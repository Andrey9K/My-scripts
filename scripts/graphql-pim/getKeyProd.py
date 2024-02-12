import pyperclip
import requests
import json
import numpy as np

className= 'BatteryType'

url = 'http://pim.marvel.ru/pimcore-graphql-webservices/getKey'
proxies = {'http': 'socks5h://localhost:6060'}
headers = {
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Connection': 'keep-alive',
    'DNT': '1',
    'Origin': 'http://pim.marvel.ru',
    'X-API-Key': '226a8a53959cd42e3d002e573cb497c6'
}
data = json.dumps({
  "query": "{{ get{}Listing {{ edges {{ node {{ key }} }} }}}}".format(className)
})

# data = {
#     'query': '''
#         # Write your query or mutation here
#         {
#           getDisplayTypeListing {
#             edges {
#               node {       
#                 key
#               }
#             }
#           }
#         }
#     '''
# }
response = requests.request("POST", url, proxies=proxies, headers=headers, data=data)
# response = requests.post(url, proxies=proxies, headers=headers, json=data)
# print(response.json())
data=response.json()
template1 = data
js1=[]  
if   'data' in template1: 
    template2= template1['data']
    templates= template2[f'get{className}Listing']
    if isinstance(templates['edges'], list):
                s= templates['edges']
                for t in range(0,len(s)):            
                    s1= s[t]
                    s2=s1['node']
                    s3=s2['key']                    
                    js1.append(f'{s3}')
    else: 
        print('Не корректный Json')
else:
        print('Не корректный Json')
# print(js1)
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