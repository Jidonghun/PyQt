# import sys
# from PyQt5.QtWidgets import *

# app = QApplication(sys.argv)
# myWindow = QWidget()
# myWindow.show()

# app.exec_()

import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    pass

app = QApplication(sys.argv)
myWindow = MyWindow()
myWindow.show()

app.exec_()

