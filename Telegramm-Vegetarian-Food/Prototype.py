import requests
from bs4 import BeautifulSoup
from time import sleep
import os
from threading import Thread
data = []
os.makedirs('Картинки')
def one():
    global identificator
    soup_id = BeautifulSoup(r.text, 'lxml')
    soup_identificator = soup_id.find_all('div', class_='recipe_l in_seen v2')
    for i in soup_identificator:
        identificator = i.get('data-in_view_el')
        print(identificator)
        continue
def two():
    soup = BeautifulSoup(r.text, 'lxml')
    soup = soup.find_all('div', class_='title_o')
    for i in soup:
        url = i.find('div', class_='title').find('a').get('href')
        title = i.find('div', class_='title').find('a').text
        new_page_link = 'https://www.russianfood.com/' + url
        data.append([identificator,title, new_page_link])
        #print(data)
        continue
def three():
    soup_F = BeautifulSoup(r.text, 'lxml')
    soup_foto = soup_F.find_all('div', class_='foto_o')
    for i in soup_foto:
        foto = i.find('div', class_='foto').find('a').find('img', class_='round shadow').get('src')
        print(foto)
        r1 = requests.get('https:' + foto)
        extimg = r1.headers["content-type"][6:]
        pathimg = os.path.join('Картинки', f'{identificator}.{extimg}')
        with open (pathimg, 'wb') as f:
            for chunk in r1:
                f.write(chunk)
        continue 
for p in range(1,3):
    url = f'https://www.russianfood.com/recipes/bytype/?fid=216&page={p}'
    r = requests.get(url)
    sleep(6)
    one()
    two()
    three()
with open ('Recepies.txt', 'w') as f:
    f.write(str(data))


