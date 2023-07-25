import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My First PyQt Window')
        self.setGeometry(0, 0, 320, 180)
        
app = QApplication(sys.argv)
mywindow = MyWindow()
mywindow.show()
app.exec_()
