import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType('./CheckBox/ordersys.ui')[0]
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.chkBox_A0.stateChanged.connect(self.AFunction)
        self.chkBox_A1.stateChanged.connect(self.AFunction)
        
        self.chkBox_B0.stateChanged.connect(self.BFunction)
        self.chkBox_B1.stateChanged.connect(self.BFunction)
        self.chkBox_B2.stateChanged.connect(self.BFunction)
        
    def AFunction(self):
        if self.chkBox_A0.isChecked():
            print(self.chkBox_A0.text())
        if self.chkBox_A1.isChecked():
            print(self.chkBox_A1.text())
    
    def BFunction(self):
        if self.chkBox_B0.isChecked():
            print(self.chkBox_B0.text())
        if self.chkBox_B1.isChecked():
            print(self.chkBox_B1.text())
        if self.chkBox_B2.isChecked():
            print(self.chkBox_B2.text())
    

if __name__ == "__main__" : 
   #QApplication : 프로그램을 실행시켜주는 클래스
   app = QApplication(sys.argv)

   #WindowClass의 인스턴스 생성
   myWindow = WindowClass()

   #프로그램 화면을 보여주는 코
   myWindow.show() 

   #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
   app.exec_()

            