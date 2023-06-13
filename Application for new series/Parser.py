import requests
from time import sleep
from bs4 import BeautifulSoup
import threading
class Parcer():
    def __init__(self):
        global soup, list_of_serial_names, tech_var_list, list_of_serial_urls, list_of_lists, dict_with_set_of_date_and_serials
        dict_with_set_of_date_and_serials = {}
        list_of_serial_names=[]
        tech_var_list=[]
        list_of_serial_urls=[]
        list_of_lists=[]
        headers = {'user-agent': 'my-app/0.0.2'}
        url = 'https://rezka.ag'
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, 'lxml')
    def find_text_and_urls(self):
        global date_var
        text_and_urls = soup.find('div', class_='b-content__inline_sidebar').find_all('div', class_='b-seriesupdate__block')
        for i in text_and_urls:
            tech_var= i.find_all('li', class_='b-seriesupdate__block_list_item') 
            list_of_serial_names=([x.find('div', class_='b-seriesupdate__block_list_item_inner').find('div', class_='cell cell-1').find('a', class_='b-seriesupdate__block_list_link').text for x in tech_var])
            list_of_serial_urls=([x.find('div', class_='b-seriesupdate__block_list_item_inner').find('div', class_='cell cell-1').find('a', class_='b-seriesupdate__block_list_link').get('href') for x in tech_var])
            list_of_lists.append([list_of_serial_names, list_of_serial_urls])
        date_var = soup.find('div', class_='b-content__inline_sidebar').find_all('div', class_='b-seriesupdate__block')
    def find_date(self):
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
    def create_dict(self):
        date_list = [k for k in tech_var_list if k != 'None']
        for key in date_list:
            for value in list_of_lists:
                dict_with_set_of_date_and_serials[key] = value
                list_of_lists.remove(value)
                break
    def search_serial_by_name(self):
        while True:
            serial = str(input('Напишите название сериала: '))
            for k,v in dict_with_set_of_date_and_serials.items():
                if serial not in v[0]:
                    print(f'{k}: В этот день сериал не выходил')
                if serial in v[0]:
                    b=v[0].index(serial)
                    print(f'{k}: {dict_with_set_of_date_and_serials[k][0][b]}\n Ссылка: https://rezka.ag/{dict_with_set_of_date_and_serials[k][1][b]}')
            choice = str(input('Если хотите еще поискать сериалы напишите да, если не хотите, то напишите нет: '))
            if choice.lower() == 'нет':
                break
            elif choice.lower() == 'да':
                continue
    def run(self):
        self.find_text_and_urls()
        self.find_date()
        self.create_dict()
        self.search_serial_by_name()
def main():
    parcer=Parcer()
    parcer.run()
if __name__ == "__main__":
    main()

        
        



