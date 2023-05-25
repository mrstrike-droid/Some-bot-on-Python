from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLineEdit, QTextEdit, QVBoxLayout
from PyQt6.QtCore import QSize, Qt
import sys
import os
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
path=os.path.dirname(os.path.abspath(__file__))
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Актуализатор файлов')
        self.resize(500, 350)

        layout= QVBoxLayout()
        self.setLayout(layout)

        self.inputField_serial = QLineEdit()
        self.inputField_serial.setPlaceholderText('Введите название сериала:')
        self.button_save = QPushButton('Сохранить', clicked=self.save_to_file)
        self.button_search = QPushButton('Поискать сериалы по списку', clicked=self.search_serials_by_list)
        self.outputField = QTextEdit()


        layout.addWidget(self.inputField_serial)
        layout.addWidget(self.button_save)
        layout.addWidget(self.button_search)
        layout.addWidget(self.outputField)
    
    def save_to_file(self):
        with open(f'{path}\my_file.txt', 'a') as my_file:
            write_serial='\n'+str(self.inputField_serial.text())          
            my_file.write(write_serial)
            my_file.close()
        self.inputField_serial.clear()
    def search_serials_by_list(self):
        my_file = open(f'{path}\my_file.txt', "r")        
        for serial in my_file:            
            if serial.isspace():
                continue
            else:              
                print('done')
                serial = serial.rstrip()  
                serial = serial.lower()                
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
            list_of_serial_names=([x.find('div', class_='b-seriesupdate__block_list_item_inner').find('div', class_='cell cell-1').find('a', class_='b-seriesupdate__block_list_link').text.lower() for x in tech_var])
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
parcer()
window.show()  # Важно: окно по умолчанию скрыто.

# Запускаем цикл событий.

app.exec()