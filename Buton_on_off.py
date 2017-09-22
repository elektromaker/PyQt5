import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
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
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' Led yandı')


    def OFFClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' Led söndü')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
