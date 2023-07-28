from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_first(object):
    def setupUi(self, first):
        first.setObjectName("first")
        first.resize(797, 473)
        self.btn2 = QtWidgets.QPushButton(first)
        self.btn2.setGeometry(QtCore.QRect(90, 180, 231, 211))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.btn2.setFont(font)
        self.btn2.setObjectName("btn2")
        self.btn3 = QtWidgets.QPushButton(first)
        self.btn3.setGeometry(QtCore.QRect(440, 180, 241, 211))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.btn3.setFont(font)
        self.btn3.setObjectName("btn3")
        self.status = QtWidgets.QLabel(first)
        self.status.setGeometry(QtCore.QRect(130, 60, 511, 81))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.status.setFont(font)
        self.status.setText("")
        self.status.setObjectName("status")

        self.retranslateUi(first)
        QtCore.QMetaObject.connectSlotsByName(first)
        
        self.btn2.clicked.connect(self.on)
        self.btn3.clicked.connect(self.off)
        
    def on(self):
        self.status.setText('Button 1 pressed')

    def off(self):
        self.status.setText('Button 2 pressed')

    def retranslateUi(self, first):
        _translate = QtCore.QCoreApplication.translate
        first.setWindowTitle(_translate("first", "Dialog"))
        self.btn2.setText(_translate("first", "Button 1"))
        self.btn3.setText(_translate("first", "Button 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    first = QtWidgets.QDialog()
    ui = Ui_first()
    ui.setupUi(first)
    first.show()
    sys.exit(app.exec_())
