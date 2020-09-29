import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import main_window

NetworkWindow = "NetworkCommands.ui"

Ui_NetworkWindow, QtBaseClass = uic.loadUiType(NetworkWindow)

class NetworkWindow(QtWidgets.QMainWindow,Ui_NetworkWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_NetworkWindow.__init__(self)
        self.setupUi(self)
        self.setFixedWidth(555)
        self.setFixedHeight(425)
        self.setWindowTitle("Network And Security Window")
        qtRectangle = self.frameGeometry()
        centerPoint = QtWidgets.qApp.desktop().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        self.Exit.clicked.connect(self.Exit_Window)
        
    def Exit_Window(self):
        self.cams = main_window.MainWindow() 
        self.cams.show()
        self.close()