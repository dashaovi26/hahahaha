import requests
import json 
headers={"Authorization": "Token 48896f6969457d187ac01be24e91de66e53af2be"}
url="https://classif.gov.spb.ru/api/v2/datasets/?page=1&per_page=100"



response=requests.get(url,headers=headers)
print(response.json())
if response.status_code ==requests.codes.ok:
    print(response.json())
else:
    print(response.status_code)
    print(response.text)
data=response.json()['results']
s=input()
while s!='no':

    for i in data:
        if int(s)==i['id']:
            print(i['name'])
    s=input()








