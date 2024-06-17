import pyperclip
import requests
import json
import numpy as np

# Впишите subjectID из WB
subjectID=6462


url = f"https://suppliers-api.wildberries.ru/content/v2/object/charcs/{subjectID}"

payload = ""
headers = {
  'Authorization': 'Bearer eyJhbGciOiJFUzI1NiIsImtpZCI6IjIwMjQwNTA2djEiLCJ0eXAiOiJKV1QifQ.eyJlbnQiOjEsImV4cCI6MTczMTQ2MzQwNCwiaWQiOiJhZjk2Yzg4NS0wNTlkLTQ5MzEtYTcxYy1iZjY1OGQwMmNkMmIiLCJpaWQiOjY0NDk5NDEsIm9pZCI6MjUwMDAwMDg5LCJzIjoyLCJzaWQiOiI2YzI3OGVlYS1mMmNiLTQ1YzktYWQwZC1lYWJmZDgwMjIwZjQiLCJ0IjpmYWxzZSwidWlkIjo2NDQ5OTQxfQ.FfFZ2sBhvzQ7mSnscCbH5s74yEgSyG15X7y7JMFkQnoJ7a7tbUwd8OLXD4BinKZKWcgtqkOLw2NlHizgEhnEYw'
}

response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)
data=response.json()
templates = data
js1=[]  
if   templates['data'] != None: 
    if isinstance(templates['data'], list):
                s= templates['data']
                for t in range(0,len(s)):            
                    s1= s[t]
                    s2=s1['charcID']
                    s3=s1['name']
                    s4=s1['charcType']
                    s5=s1['unitName']
                    s6=s1['maxCount']
                    s7=s1['required']
                    if s7 == False:
                              s7='ЛОЖЬ'
                    if s7 == True:
                              s7='ИСТИНА'
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
      print('Ошибка (строка для копирования пустая)')
# print("Результат: ", copied_result)