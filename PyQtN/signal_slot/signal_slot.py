# 파일 이름 : PushButtonTest2.py
import sys 
from PyQt5.QtWidgets import * 
from PyQt5 import uic

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치
form_class = uic.loadUiType("./signal_slot/signal_slot.ui")[0]

#화면을 띄우는데 사용되는 Class 선언 
class WindowClass(QMainWindow, form_class) : 
   def __init__(self) :
       super().__init__()
       self.setupUi(self)
       self.Button1.clicked.connect(self.button1Function)
       self.Button2.clicked.connect(self.button2Function)
    
   def button1Function(self):
        print('Button1 Clicked!')
        self.label.setText('Button A Clicked!')
        print(self.Button1.text() + '눌렸네')
        
   def button2Function(self):
        print('Button2 Clicked!')
        self.label.setText('Button B Clicked!')
        print(self.Button2.text() + '눌렸네')

if __name__ == "__main__" : 
   #QApplication : 프로그램을 실행시켜주는 클래스
   app = QApplication(sys.argv)

   #WindowClass의 인스턴스 생성
   myWindow = WindowClass()

   #프로그램 화면을 보여주는 코
   myWindow.show() 

   #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
   app.exec_()
