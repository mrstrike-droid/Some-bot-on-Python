import requests
from bs4 import BeautifulSoup
r = requests.get('https://www.russianfood.com/recipes/bytype/?fid=216')
soup = BeautifulSoup(r.text, 'lxml')
soup = soup.find_all('div', class_='title_o')
for i in soup:
    url = i.find('div', class_='title').find('a').get('href')
    title = i.find('div', class_='title').find('a').text
    new_page_link = 'https://www.russianfood.com/' + url
    print(title)
    print(new_page_link)


