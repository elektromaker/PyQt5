# -*- coding: utf-8 -*-

"""
Bu projede nodeMCU ve Raspberry pi kullanulmıştır. NodeMCU arduino ide
ile programlanmıştır. Raspberry pi ise python ile programlanmıştır.
Bir odanın sıcaklığını nodeMCU ile ölçüp thingspeak.com sitesindeki
kanalımıza yazdırıyoruz. Raspberry pi üzerinde yazdığımız python kodları
ile de istediğimiz yerden internet üzerinden okuyoruz.
30 Eylül 2017
"""

from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
                             QApplication, QLabel)
import sys

import thingspeak #Thingspeak modülünü önceden python'a yüklemek gerekiyor.
channel_id = 59878 # Kendi kanal ID'nizi yazınız
write_key  = "0C074K0QF9M1NKL1" # Kendi WRITE KEY değerinizi yazınız.
read_key    = "9UDLSXZ2F411ZUP5" # Kendi YOUR API KEY değerinizi yazınız.
channel = thingspeak.Channel(id=channel_id,api_key=read_key)

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        etiket1 = QLabel('Sıcaklığı okumak için butona basınız', self)
        etiket1.move(10, 5)

        etiket2 = QLabel('° C', self)
        etiket2.move(145, 25)

        self.btn = QPushButton('Buton', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.resize(40,20)
        self.le.move(100, 22)


        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Sıcaklık Okuma Programı')
        self.show()

    def showDialog(self):
        oku = channel.get_field_last(field='field1')
        #print("Sıcaklık:", oku[66:71], "*C")
        #deger = QLineEdit(oku[66:71])
        self.le.setText(oku[66:71])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
