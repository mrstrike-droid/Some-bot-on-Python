from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLineEdit, QTextEdit, QVBoxLayout
from PyQt6.QtCore import QSize, Qt
import sys
from random import choice
import requests
from time import sleep
from bs4 import BeautifulSoup

app = QApplication(sys.argv)
app.setStyleSheet('''
    QWidget {
        font-size:15px;
    }
    QPushButton {
        font-size:15px;
    }
''')
dict_with_set_of_date_and_serials = {}
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Парсер сериалов')
        self.resize(500, 350)

        layout= QVBoxLayout()
        self.setLayout(layout)

        self.inputField = QLineEdit()
        self.inputField.setPlaceholderText('Введите сериал:')
        self.button = QPushButton('Поиск', clicked=self.search_serial_by_name)
        self.outputField = QTextEdit()


        layout.addWidget(self.inputField)
        layout.addWidget(self.button)
        layout.addWidget(self.outputField)
    
    def search_serial_by_name(self):
        self.outputField.clear()        
        serial = str(self.inputField.text())
        serial = serial.rstrip()  
        for k,v in dict_with_set_of_date_and_serials.items():
            if serial not in v[0]:
                self.outputField.append(f'{k}: В этот день сериал не выходил')
            elif serial in v[0]:
                b=v[0].index(serial)
                self.outputField.append(f'{k}: Вышла новая серия\nСсылка: https://rezka.ag/{dict_with_set_of_date_and_serials[k][1][b]}')
def parcer():
        list_of_serial_names=[]
        tech_var_list=[]
        list_of_serial_urls=[]
        list_of_lists=[]
        headers = {'user-agent': 'my-app/0.0.2'}
        url = 'https://rezka.ag'
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, 'lxml')
        text_and_urls = soup.find('div', class_='b-content__inline_sidebar').find_all('div', class_='b-seriesupdate__block')
        for i in text_and_urls:
            tech_var= i.find_all('li', class_='b-seriesupdate__block_list_item') 
            list_of_serial_names=([x.find('div', class_='b-seriesupdate__block_list_item_inner').find('div', class_='cell cell-1').find('a', class_='b-seriesupdate__block_list_link').text for x in tech_var])
            list_of_serial_urls=([x.find('div', class_='b-seriesupdate__block_list_item_inner').find('div', class_='cell cell-1').find('a', class_='b-seriesupdate__block_list_link').get('href') for x in tech_var])
            list_of_lists.append([list_of_serial_names, list_of_serial_urls])
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

window = MainWindow()
window.show()  # Важно: окно по умолчанию скрыто.

# Запускаем цикл событий.
parcer()
app.exec()
