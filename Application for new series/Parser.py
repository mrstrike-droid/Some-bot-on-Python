import requests
from bs4 import BeautifulSoup
from time import sleep
from itertools import chain
import os
import json
list_of_serial_names=[]
tech_var_list=[]
list_of_serial_urls=[]
list_of_lists=[]
dict_with_set_of_date_and_serials = {}
headers = {'user-agent': 'my-app/0.0.2'}
url = 'https://rezka.ag'
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'lxml')
text_and_urls = soup.find('div', class_='b-content__inline_sidebar').find_all('div', class_='b-seriesupdate__block')
for i in text_and_urls:
    tech_var= i.find_all('li', class_='b-seriesupdate__block_list_item') 
    for x in tech_var:
        list_of_serial_names=(x.find('div', class_='b-seriesupdate__block_list_item_inner').find('div', class_='cell cell-1').find('a', class_='b-seriesupdate__block_list_link').text)
        list_of_serial_urls=(x.find('div', class_='b-seriesupdate__block_list_item_inner').find('div', class_='cell cell-1').find('a', class_='b-seriesupdate__block_list_link').get('href'))
        list_of_lists=([list_of_serial_names,list_of_serial_urls])
date_var = soup.find('div', class_='b-content__inline_sidebar').find_all('div', class_='b-seriesupdate__block')
for z in date_var:
    tech_var2=z.find_all('div', class_='b-seriesupdate__block_date')
    tech_var3=z.find_all('div', class_='b-seriesupdate__block_date collapsible')
    for y in tech_var2:
        y=y.find('small')
        y=str(y)
        y=y.replace('<small>(','')
        y=y.replace(')</small>','')
        tech_var_list.append(y)
    for y in tech_var3:
        y=y.text
        y=str(y)
        y=y.replace(' развернуть','')
        tech_var_list.append(y) 
date_list = [k for k in tech_var_list if k != 'None']
for key in date_list:
    for value in list_of_lists:
        dict_with_set_of_date_and_serials[key] = value
        list_of_lists.remove(value)
        break
print(dict_with_set_of_date_and_serials)

