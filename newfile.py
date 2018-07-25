import sys
from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication(sys.argv)
SignUp = uic.loadUi('untitled2.ui')
SignUp.show()
app.exec()
