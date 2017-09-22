#-*-coding:utf-8-*-
import sys
import RPi.GPIO as GPIO
import time
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QLabel
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)

class Example(QMainWindow, QLabel):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        etiket = QLabel('<font color="black" size="+1">Lamba kontrol butonları</font>', self)
        etiket.resize(etiket.sizeHint())
        etiket.move(10, 10)
        
        btn1 = QPushButton("ON", self)
        btn1.move(30, 50)

        btn2 = QPushButton("OFF", self)
        btn2.move(150, 50)

        btn1.clicked.connect(self.ONClicked)
        btn2.clicked.connect(self.OFFClicked)

        self.statusBar()

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')
        self.show()

    def ONClicked(self):
        GPIO.output(3,1)
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' Led yandı')


    def OFFClicked(self):
        GPIO.output(3,0)
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' Led söndü')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
