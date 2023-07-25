import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("./CheckBox/checkbox.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #GroupBox밖에 있는 CheckBox에 기능 연결
        self.chkBox3.stateChanged.connect(self.chkFunction)
        self.chkBox4.stateChanged.connect(self.chkFunction)
        #GroupBox안에 있는 CheckBox에 기능 연결
        self.groupChkBox1.stateChanged.connect(self.groupchkFunction)
        self.groupChkBox2.stateChanged.connect(self.groupchkFunction)

    def chkFunction(self):
    #CheckBox는 여러개가 선택될 수 있기 때문에 elif를 사용하지 않습니다.
        if self.chkBox3.isChecked():
            print("checkBox1 is Checked")
        if self.chkBox4.isChecked():
            print("checkBox2 is Checked")

    def groupchkFunction(self):
        if self.groupchkBox1.isChecked():
            print("group checkbox1 is Checked")
        if self.groupchkBox2.isChecked():
            print("group checkbox2 is Checked")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show() 
    app.exec_()