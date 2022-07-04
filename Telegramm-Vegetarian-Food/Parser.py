import requests
from bs4 import BeautifulSoup
from time import sleep
import os
import json
data = []
os.makedirs('Картинки')
def parsing():
    global identificator
    soup = BeautifulSoup(r.text, 'lxml')
    soup = soup.find_all('div', class_='recipe_l in_seen v2')
    for i in soup:
        url = i.find('div', class_='title_o').find('div', class_='title').find('a').get('href')
        title = i.find('div', class_='title_o').find('div', class_='title').find('a').text
        identificator = i.find('div', class_='title_o').find('div', class_='title').find('a').get('name')
        foto = i.find('div', class_='foto_o').find('div', class_='foto').find('a').find('img', class_='round shadow').get('src')
        information = i.find('div', class_='announce_o').find('div', class_='announce').find('p').text
        try:
            recipe = i.find('div', class_='announce_o').find('div', class_='ingr_str').find('span').text
        except:
            recipe = '-'
        new_page_link = 'https://www.russianfood.com/' + url
        data.append([identificator,title,information,recipe, new_page_link])
        r1 = requests.get('https:' + foto)
        extimg = r1.headers["content-type"][6:]
        pathimg = os.path.join('Картинки', f'{identificator}.{extimg}')
        with open (pathimg, 'wb') as f:
            for chunk in r1:
                f.write(chunk)
for p in range(1,2):
    url = f'https://www.russianfood.com/recipes/bytype/?fid=216&page={p}'
    r = requests.get(url)
    sleep(6)
    parsing()
    print(p)
with open ('Recepies.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)


