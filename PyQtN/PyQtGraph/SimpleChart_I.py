# pip install scipy
# pip install matplotlib

import sys 
from PyQt5.QtWidgets import *
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
from scipy.stats import linregress

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # pg.PlotWidget()을 이용하여 그림 그릴 수 있는 위젯을 생성
        self.plot_widget = pg.PlotWidget()
        self.plot_widget = pg.PlotWidget()
        # 그림을 그릴 수 있는 위젯을 중앙에 배치
        self.setCentralWidget(self.plot_widget)
        
        x = [1, 2, 3, 4, 5]
        y = [1, 4, 9, 16, 25]
        # x = np.random.randint(1, 101, size=15).tolist()
        # y = np.random.randint(1, 101, size=15).tolist()
        # 그림을 기를 수 있는 위젯(self.plot_widget)의 plot() 메서드 호출
        corr, p_vlaue = pearsonr(x, y)
        self.plot_widget.setBackground('w')
        self.plot_widget.plot(x, y, symbol='o', symbolSize=5)
        # self.plot_widget.plot(y, x, symbol='o', symbolSize=5)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    plt.show()
    app.exec_()  
