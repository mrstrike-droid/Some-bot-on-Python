from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLineEdit, QTextEdit, QVBoxLayout
from PyQt6.QtCore import QSize, Qt
import sys

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
        self.setWindowTitle('Актуализатор файлов')
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
    
    def save_to_file(self):
        pass
        

window = MainWindow()
window.show()  # Важно: окно по умолчанию скрыто.

# Запускаем цикл событий.

app.exec()