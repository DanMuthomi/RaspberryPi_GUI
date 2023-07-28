from PyQt5 import QtCore, QtGui, QtWidgets
from page1_2 import Ui_first

class Ui_main(object):
    def openTwo(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_first()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def setupUi(self, main):
        main.setObjectName("main")
        main.resize(655, 419)
        self.btn1 = QtWidgets.QPushButton(main)
        self.btn1.setGeometry(QtCore.QRect(20, 80, 611, 321))
        self.btn1.setObjectName("btn1")
        self.btn1.clicked.connect(self.openTwo)

        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "Dialog"))
        self.btn1.setText(_translate("main", "Push to activate system"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main = QtWidgets.QDialog()
    ui = Ui_main()
    ui.setupUi(main)
    main.show()
    sys.exit(app.exec_())
