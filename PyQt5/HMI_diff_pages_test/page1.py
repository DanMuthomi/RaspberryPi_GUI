import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.uic import loadUi

class HMI2(first):
    def __init__(self):
        super(HMI2, self).__init__()
        loadUi('page1.ui',self)
        
        self.setWindowTitle('HMI2 System')
        self.btn2.clicked.connect(self.on)
        self.btn3.clicked.connect(self.off)
        
    @pyqtSlot()
    def on(self):
        self.status.setText('Button 1 pressed')

    def off(self):
        self.status.setText('Button 2 pressed')

app=QApplication(sys.argv)
widget=HMI2()
widget.show()
sys.exit(app.exec_())
