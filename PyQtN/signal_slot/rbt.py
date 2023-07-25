# 파일 이름 : PushButtonTest2.py
import sys 
from PyQt5.QtWidgets import * 
from PyQt5 import uic

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치
form_class = uic.loadUiType("./signal_slot/rbt.ui")[0]

#화면을 띄우는데 사용되는 Class 선언 
class WindowClass(QMainWindow, form_class) : 
    def __init__(self):
       super().__init__()
       self.setupUi(self)
       self.radioBtn1.clicked.connect(self.groupboxRadFunction)
       self.radioBtn2.clicked.connect(self.groupboxRadFunction)
       self.radioBtn3.clicked.connect(self.groupboxRadFunction)
       self.radioBtn4.clicked.connect(self.groupboxRadFunction)
       
    def groupboxRadFunction(self):
       if self.radioBtn1.isChecked():
           print('radioBtn1 Checked')
       elif self.radioBtn2.isChecked():
           print('radioBtn2 Checked')
       elif self.radioBtn3.isChecked():
           print('radioBtn3 Checked')
       elif self.radioBtn4.isChecked():
           print('radioBtn4 Checked')
            
   
if __name__ == "__main__" : 
   #QApplication : 프로그램을 실행시켜주는 클래스
   app = QApplication(sys.argv)

   #WindowClass의 인스턴스 생성
   myWindow = WindowClass()

   #프로그램 화면을 보여주는 코
   myWindow.show() 

   #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
   app.exec_()
