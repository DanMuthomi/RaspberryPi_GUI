import sys
from PyQt5.QtCore import pyqtSlot
from Pyqt5.Qtwidgets import QApplication,QDialog
from PyQt5.uic import loadUi
import Rpi.GPIO as gpio

led=26

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
gpio.setup(led,gpio.OUT)

class HMI(QDialog):
    def __init__(self):
        super(HMI, self).__init__()
        loadUi('basic_text.ui',self)
        
        self.setWindowTitle('HMI System')
        self.btn1.clicke.connect(self.on_off)
    @pyqtSlot
    def on_off(self):
        if gpio.input(led):
            gpio.output(led,gpio.LOW)
            self.btn1.setText('OFF')
            self.status.setText('LED is OFF')
        else:
            gpio.output(led, gpio.HIGH)
            self.btn.settext('ON')
            self.status.setText('LED is On')
            
app=QApplication(sys.argv)
widget=HMI()
widget.show()
sys.exit(app.exec ())