import requests
from bs4 import BeautifulSoup
from time import sleep
import os
import json
data = []
headers = {'user-agent': 'my-app/0.0.1'}
url = 'https://rezka.ag/+'
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'lxml')
soup = soup.find_all('div', class_='b-content__inline_sidebar')
print(soup)

