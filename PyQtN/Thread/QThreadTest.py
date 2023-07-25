import time
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *

form_class = form_class = uic.loadUiType("./Thread/QThreadTest.ui")[0]

class WindowClass(QMainWindow, form_class) : 
   def __init__(self) :
       super().__init__()
       self.setupUi(self)
       
       self.btn_A_start.clicked.connect(self.slot_A_task)
       self.btn_B_start.clicked.connect(self.slot_B_task)
       
   def slot_A_task(self):
        print('A 업무를 시작합니다')
        for i in range(0, 101, 10):
            print('A 업무 진행율 {}%'.format(i))
            time.sleep(2)
        print('A 업무 종료')
        
   def slot_B_task(self): 
        print('B 업무를 시작합니다')
        for i in range(0, 101, 10): 
            print('B 업무 진행율 {}%'.format(i)) 
            time.sleep(2)
        print('B 업무 종료')
            
if __name__ == "__main__" : 
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show() 
    app.exec_()