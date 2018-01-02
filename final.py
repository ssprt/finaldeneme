from PyQt5.QtWidgets import *
import sys

class YeniPencere(QWidget):
    def __init__(self):
        super().__init__()

uygulama = QApplication(sys.argv)
pencere = YeniPencere()
pencere.show()
uygulama.exec_()