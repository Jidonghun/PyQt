import sys 
from PyQt5.QtWidgets import * 
from PyQt5 import uic

form_class=uic.loadUiType("./temp/click.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Btn.clicked.connect(self.push)
        
    def push(self):
        if self.label.text() != 'Button Clicked':
            self.label.setText('Button Clicked')
        else:
            self.label.setText('아래버튼 클릭')
        # self.label.setText('clicked')


if __name__ == "__main__" : 
   #QApplication : 프로그램을 실행시켜주는 클래스
   app = QApplication(sys.argv)

   #WindowClass의 인스턴스 생성
   myWindow = WindowClass()

   #프로그램 화면을 보여주는 코
   myWindow.show() 

   #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
   app.exec_()