import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QLabel, QVBoxLayout
from PyQt5.QtCore import QCoreApplication


class Example(QLabel):
    def __init__(self):
        super().__init__()

        self.initUI()

    def yazdir(self):
        print("Butona basildı")

    def initUI(self):
        etiket = QLabel('<font color="blue" size="+1">Merhaba Dünya</font>', self)
        etiket.resize(etiket.sizeHint())
        etiket.move(10, 10)

        qbtn = QPushButton('Buton', self)
        qbtn.clicked.connect(self.yazdir)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(10, 30)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
