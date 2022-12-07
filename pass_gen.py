import string
import secrets
from PyQt5.QtWidgets import QInputDialog
import sys
from PyQt5.QtWidgets import *#(QApplication, QWidget, QPushButton, QLineEdit, QInputDialog)
import random

class Example(QWidget):
    ss =None
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btn = QPushButton('Генерувати', self)
        self.btn.move(145, 100)
        self.btn.clicked.connect(self.showDialog)
        self.t_btn = QPushButton('Змінити', self)
        self.t_btn.move(20, 100)
        self.t_btn.clicked.connect(self.re_generate)
        # self.le = QLineEdit(self)
        self.le = QTextEdit(self)
        self.le.setFixedWidth(200)
        self.le.setFixedHeight(70)
        self.le.move(20, 20)
        self.setGeometry(300, 300, 240, 160)
        self.setWindowTitle('Генератор паролю')
        self.show()

    def re_generate(self):
        if self.ss:
            text = self.generate()
            self.le.setText(str(text))
        else:
            self.le.setText('Спочатку згенеруйте')

    def generate(self):
        print(self.ss)
        if self.ss:
            num = int(self.ss)
            print(num)
            res = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(num))
            res = ''.join(secrets.choice(string.ascii_letters) for x in range(num))
            res = ''.join(secrets.choice(string.ascii_uppercase) for x in range(num))
            res = ''.join(secrets.choice(string.ascii_lowercase) for x in range(num))
            res = ''.join(secrets.choice(string.ascii_letters + string.punctuation) for x in range(num))
            res = ''.join(secrets.choice(string.digits) for x in range(num))
            res = ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for x in range(num))
            return res
        else:
            return 'Спочатку згенеуйте'

    def showDialog(self):
        self.ss, ok = QInputDialog.getInt(self, 'Кількість символів у паролі', 'Is this ok?')
        print('dsjkaal', self.ss, ok)
        if ok:
            text = self.generate()
        if text:
            self.le.setText(str(text))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())