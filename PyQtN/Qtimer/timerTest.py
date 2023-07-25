import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import datetime


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        # self.timer.setInterval(200)
        # print(self.timer.interval())
        self.timer.start()
        self.timer.timeout.connect(self.slot_timeout)
        
        self.label = QLabel(self)
        self.label.setGeometry(10, 10, 150, 16)
        
    def slot_timeout(self):
        now = datetime.datetime.now()
        self.label.setText(str(now))
        # print(now)
    

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_
    
    