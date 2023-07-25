import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

class HelloWorldWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializedUI()
        
    def initializedUI(self):
        self.setGeometry(300, 300, 320, 180)
        self.setWindowTitle('Hello World')

app = QApplication(sys.argv)
window = HelloWorldWindow()
window.show()
app.exec()
