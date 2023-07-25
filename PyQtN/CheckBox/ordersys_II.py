import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType('./CheckBox/ordersys.ui')[0]
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Btn.clicked.connect(self.order)
    
    def order(self):
        Alst=[]; Blst=[]; total_price=0
        if self.chkBox_A0.isChecked():
            Alst.append(self.chkBox_A0.text())
            s_price=self.lbl_price_A0.text().replace('원','').replace(',','')
            total_price+=int(s_price)
        if self.chkBox_A1.isChecked():
            Alst.append(self.chkBox_A1.text())
            s_price=self.lbl_price_A1.text().replace('원','').replace(',','')
            total_price+=int(s_price)
        
        if self.chkBox_B0.isChecked():
            Blst.append(self.chkBox_B0.text())
            s_price=self.lbl_price_B0.text().replace('원','').replace(',','')
            total_price+=int(s_price)
        if self.chkBox_B1.isChecked():
            Blst.append(self.chkBox_B1.text())
            s_price=self.lbl_price_B1.text().replace('원','').replace(',','')
            total_price+=int(s_price)
        if self.chkBox_B2.isChecked():
            Blst.append(self.chkBox_B2.text())
            s_price=self.lbl_price_B2.text().replace('원','').replace(',','')
            total_price+=int(s_price)

        # QMessageBox.information(self, 'Info', '총금액은 {}입니다.'.format(total_price))
        print('식사:', Alst, '요리:', Blst, '\n총 가격:', total_price)


if __name__ == "__main__" : 
   #QApplication : 프로그램을 실행시켜주는 클래스
   app = QApplication(sys.argv)

   #WindowClass의 인스턴스 생성
   myWindow = WindowClass()

   #프로그램 화면을 보여주는 코
   myWindow.show() 

   #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
   app.exec_()

            