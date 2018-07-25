import sys
from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication(sys.argv)
login = uic.loadUi('untitled.ui')
login.show()
app.exec()
