import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

class HelloWorldWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializedUI()
        
    def initializedUI(self):
        self.setGeometry(300, 300, 320, 180)
        self.setWindowTitle('Hello World')
        
        Hello_label = QLabel(self)
        Hello_label.setText('Hello World')
        Hello_label.move(200, 40)
        
        button = QPushButton(self)
        button.setText('OK')
        button.move(200, 60)

app = QApplication(sys.argv)
window = HelloWorldWindow()
window.show()
app.exec()


