import sys
import numpy as np
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *    # for Qtime
import random
import pyqtgraph as pg 

form_class = uic.loadUiType("./PyQtGraph/rtpQuiz.ui")[0]

class MyMainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btnStart.clicked.connect(self.slot_start)
        self.btnStop.clicked.connect(self.slot_stop)
        
        self.nPoints = 40
        self.ch0dBm = np.zeros(self.nPoints, dtype=float)
        self.ch1dBm = np.zeros(self.nPoints, dtype=float)
        self.x = range(self.nPoints)
        self.pw0 = pg.PlotWidget(title='Ch 0')
        self.pw1 = pg.PlotWidget(title='Ch 1')
        self.verticalLayout.addWidget(self.pw0)
        self.verticalLayout.addWidget(self.pw1)
        self.pw0.setYRange(-50, 0)
        self.pdi0 = self.pw0.plot()         # PlotDataItem obj를 반환
        self.pdi0.setData(self.x, self.ch0dBm, pen='r')        
        self.pw1.setYRange(-50, 0)
        self.pdi1 = self.pw1.plot()         # PlotDataItem obj를 반환
        self.pdi1.setData(self.x, self.ch1dBm, pen='g')        
        
        # --- timer for update the date/time
        self.timer_plot = QTimer()
        self.timer_plot.setInterval(100)
        self.timer_plot.timeout.connect(self.drawPlot)
        
        
    def drawPlot(self):
        self.ch0dBm = self.ch0dBm[1:]
        self.ch0dBm = np.append(self.ch0dBm, -1.0* random.randint(0, 40) )
        self.pdi0.setData(self.x, self.ch0dBm, pen='r')        
        
        self.ch1dBm = self.ch1dBm[1:]
        self.ch1dBm = np.append(self.ch1dBm, -1.0* random.randint(0, 40) )
        self.pdi1.setData(self.x, self.ch1dBm, pen='g')     
        
    
    def slot_start(self):
        self.timer_plot.start()
    
    def slot_stop(self):
        self.timer_plot.stop()
        

if __name__=='__main__':
    app = QApplication(sys.argv)
    mywin = MyMainWindow()
    mywin.show()
    sys.exit(app.exec_())

