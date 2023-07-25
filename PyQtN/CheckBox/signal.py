import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MySignal(QObject):
    signalx = pyqtSignal()
    signaly = pyqtSignal(int, int)
    
    def run(self):
        self.signalx.emit()
        self.signaly.emit(1, 2)
        
        
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        mysignal = MySignal()
        mysignal.signalx.connect(self.signalx_emitted)
        mysignal.signaly.connect(self.signaly_emitted)
        mysignal.run()
        
    @pyqtSlot()
    def signalx_emitted(self):
        print('signalx emiited')
        
    @pyqtSlot(int, int)
    def signaly_emitted(self, arg1, arg2):
        print('signalx emiited', arg1, arg2)


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_
    
    
    