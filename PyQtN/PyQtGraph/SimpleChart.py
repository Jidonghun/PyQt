import sys
from PyQt5.QtWidgets import *
import pyqtgraph as pg

class WindowClass(QMainWindow):
    def __init__(self) :
        super().__init__()
        self.plot_widget = pg.PlotWidget(title = 'Basic PyQtGraph Plot')          # 위젯 생성
        self.setCentralWidget(self.plot_widget)     # 위젯 중앙배치
        
        x = [1, 2, 3, 4]
        y = [1, 4, 9, 16]
        self.plot_widget.setBackground('w')
        self.plot_widget.showGrid(x=False, y=True)
        self.plot_widget.plot(x, y, symbol='t')                 # 위젯의 plot() 매서드 호출
        
if __name__ == "__main__" : 
      app = QApplication(sys.argv) 
      myWindow = WindowClass() 
      myWindow.show() 
      app.exec_()