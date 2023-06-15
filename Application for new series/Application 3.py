from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLineEdit, QTextEdit, QVBoxLayout, QTextBrowser
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QTextCursor
import sys
import os
import requests
from time import sleep
from bs4 import BeautifulSoup
import threading


app = QApplication(sys.argv)
app.setStyleSheet('''
    QWidget {
        font-size:15px;
    }
    QPushButton {
        font-size:15px;
    }
''')

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
        self.button_delete = QPushButton('Удалить', clicked=self.delete_file)
        self.button_search = QPushButton('Поискать сериалы по списку', clicked=self.search_serials_by_list)
        self.outputField = QTextBrowser()
        self.outputField.setOpenExternalLinks(True)


        layout.addWidget(self.inputField_serial)
        layout.addWidget(self.button_save)
        layout.addWidget(self.button_delete)
        layout.addWidget(self.button_search)
        layout.addWidget(self.outputField)
    
    def save_to_file(self):
        with open(f'{path}\my_file.txt', 'a', encoding="utf-8") as my_file:
            write_serial='\n'+str(self.inputField_serial.text())          
            my_file.write(write_serial)
            my_file.close()
        self.inputField_serial.clear()
    def delete_file(self):
        my_file = open(f'{path}\my_file.txt', 'r', encoding="utf-8")
        delete_line = str(self.inputField_serial.text())
        delete_line = delete_line.strip()
        lst = []
        for line in my_file:
            if delete_line == line.rstrip():
                line = line.replace(delete_line,'')
            lst.append(line)
        my_file.close()
        my_file = open(f'{path}\my_file.txt', 'w', encoding="utf-8")
        for line in lst:
            my_file.write(line)
        my_file.close()
        self.inputField_serial.clear()
    def search_serials_by_list(self):        
        my_file = open(f'{path}\my_file.txt', "r", encoding="utf-8") 
        self.outputField.clear()       
        for serial in my_file:            
            if serial.isspace():
                continue
            else:                
                serial = serial.rstrip()  
                serial = serial.lower()                               
                for k,v in dict_with_set_of_date_and_serials.items():                    
                    if serial in v[0]:                        
                        b=v[0].index(serial)
                        number_of_series = dict_with_set_of_date_and_serials[k][1][b]
                        self.outputField.append(f'{k}: Вышла {number_of_series} {serial.capitalize()}')
                        self.outputField.append(f'<a href=https://rezka.ag/{dict_with_set_of_date_and_serials[k][1][b]}>Ссылка</a> ')
class Parcer():
    def __init__(self):
        global list_of_serial_names, tech_var_list, list_of_serial_urls, list_of_lists, dict_with_set_of_date_and_serials, list_of_numbseries
        dict_with_set_of_date_and_serials = {}         
        list_of_serial_names=[]
        tech_var_list=[]
        list_of_serial_urls=[]
        list_of_lists=[]
        list_of_numbseries = []
    def request_get(self):
        global soup
        headers = {'user-agent': 'my-app/0.0.2'}
        url = 'https://rezka.ag'
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, 'lxml')
    def find_text_and_urls(self):
        text_and_urls = soup.find('div', class_='b-content__inline_sidebar').find_all('div', class_='b-seriesupdate__block')
        for i in text_and_urls:
            tech_var= i.find_all('li', class_='b-seriesupdate__block_list_item') 
            list_of_serial_names=([x.find('div', class_='b-seriesupdate__block_list_item_inner').find('div', class_='cell cell-1').find('a', class_='b-seriesupdate__block_list_link').text.lower() for x in tech_var])
            list_of_serial_urls=([x.find('div', class_='b-seriesupdate__block_list_item_inner').find('div', class_='cell cell-1').find('a', class_='b-seriesupdate__block_list_link').get('href') for x in tech_var])
            list_of_numbseries = ([x.find('div', class_='b-seriesupdate__block_list_item_inner').find('span', class_='cell cell-2').text for x in tech_var])            
            list_of_lists.append([list_of_serial_names, list_of_numbseries, list_of_serial_urls])
    def find_date(self):
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
    def create_dict(self):
        date_list = [k for k in tech_var_list if k != 'None']
        for key in date_list:
            for value in list_of_lists:
                dict_with_set_of_date_and_serials[key] = value
                list_of_lists.remove(value)
                break
    def run(self):
        while True:
            self.request_get()
            self.find_text_and_urls()
            self.find_date()
            self.create_dict()
            sleep(3600)
def main():
    parcer=Parcer()
    window = MainWindow()
    thread_parcer = threading.Thread(target=parcer.run)
    thread_parcer.start()
    window.show()  
    app.exec()
    thread_parcer.join()
     
if __name__ == "__main__":
    main()