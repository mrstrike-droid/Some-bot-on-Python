import requests
from bs4 import BeautifulSoup
from time import sleep
import os
import json
data = []
data2=[]
data3=[]
count=0
count2=0
headers = {'user-agent': 'my-app/0.0.2'}
url = 'https://rezka.ag'
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'lxml')
Text_and_urls = soup.find('div', class_='b-content__inline_sidebar').find_all('div', class_='b-seriesupdate__block')
for i in Text_and_urls:
    count+=1
    data.append(count)
    tech_var= i.find_all('li', class_='b-seriesupdate__block_list_item')
    for x in tech_var:                
        data.append(x.find('div', class_='b-seriesupdate__block_list_item_inner').find('div', class_='cell cell-1').find('a', class_='b-seriesupdate__block_list_link').text)
date = soup.find('div', class_='b-content__inline_sidebar').find_all('div', class_='b-seriesupdate__block')
for z in date:
    tech_var2=z.find_all('div', class_='b-seriesupdate__block_date')
    tech_var3=z.find_all('div', class_='b-seriesupdate__block_date collapsible')
    for y in tech_var2:
        y=y.find('small')
        y=str(y)
        y=y.replace('<small>(','')
        y=y.replace(')</small>','')
        data2.append(y)
    for y in tech_var3:
        y=y.text
        y=str(y)
        y=y.replace(' развернуть','')
        data2.append(y) 
for k in data2:
    if k != 'None':
        data3.append(k)
print(data)


