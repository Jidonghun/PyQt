import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType('./CheckBox/ordersys.ui')[0]
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Btn.clicked.connect(self.order)
        self.total = 0
        self.chkBox_A0.stateChanged.connect(self.tp)
        self.chkBox_A1.stateChanged.connect(self.tp)
        self.chkBox_B0.stateChanged.connect(self.tp)
        self.chkBox_B1.stateChanged.connect(self.tp)
        self.chkBox_B2.stateChanged.connect(self.tp)
        self.Btn.clicked.connect(self.orpi)

    def order(self):
        Alst = []; Blst = []; total_price=0
        if self.chkBox_A0.isChecked():
            Alst.append(self.chkBox_A0.text())
            s_price = self.lbl_price_A0.text().replace('원','').replace(',','')
            total_price += int(s_price)
        if self.chkBox_A1.isChecked():
            Alst.append(self.chkBox_A1.text())
            s_price = self.lbl_price_A1.text().replace('원','').replace(',','')
            total_price += int(s_price)
        
        if self.chkBox_B0.isChecked():
            Blst.append(self.chkBox_B0.text())
            s_price = self.lbl_price_B0.text().replace('원','').replace(',','')
            total_price += int(s_price)
        if self.chkBox_B1.isChecked():
            Blst.append(self.chkBox_B1.text())
            s_price = self.lbl_price_B1.text().replace('원','').replace(',','')
            total_price += int(s_price)
        if self.chkBox_B2.isChecked():
            Blst.append(self.chkBox_B2.text())
            s_price = self.lbl_price_B2.text().replace('원','').replace(',','')
            total_price += int(s_price)

        # QMessageBox.information(self, 'Info', '총금액은 {}입니다.'.format(total_price))
        print('식사:', Alst, '요리:', Blst, '\n총 가격:', total_price)

    def tp(self):
        chkBoxs = [self.chkBox_A0, self.chkBox_A1, self.chkBox_B0, self.chkBox_B1, self.chkBox_B2]
        lbls = [self.lbl_price_A0, self.lbl_price_A1, self.lbl_price_B0, self.lbl_price_B1, self.lbl_price_B2]
        total = 0
        for i, chkBox in enumerate(chkBoxs):
            if chkBox.isChecked():
                total += int(lbls[i].text().replace('원', '').replace(',', ''))
                
        self.lbl_price.setText(str(total))
    
    def orpi(self):
        chkBoxs = [self.chkBox_A0, self.chkBox_A1, self.chkBox_B0, self.chkBox_B1, self.chkBox_B2]
        order_lst = []
        for chkBox in chkBoxs:
            if chkBox.isChecked():
                order_lst.append(chkBox.text())
                
        print(order_lst, '주문')
        print('총 금액은 {}이다.'.format(self.lbl_price.text()))


if __name__ == "__main__" : 
   #QApplication : 프로그램을 실행시켜주는 클래스
   app = QApplication(sys.argv)

   #WindowClass의 인스턴스 생성
   myWindow = WindowClass()

   #프로그램 화면을 보여주는 코
   myWindow.show() 

   #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
   app.exec_()

            