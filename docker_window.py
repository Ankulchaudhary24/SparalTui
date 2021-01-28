import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import main_window
from general_commands import Output
from subprocess import getstatusoutput as gso

MyDockerWindow = "DockerSetup.ui"

Ui_DockerWindow, QtBaseClass = uic.loadUiType(MyDockerWindow)

class DockerWindow(QtWidgets.QMainWindow,Ui_DockerWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_DockerWindow.__init__(self)
        self.setupUi(self)
        self.setFixedWidth(555)
        self.setFixedHeight(425)
        self.setWindowTitle("Docker Setup Window")
        qtRectangle = self.frameGeometry()
        centerPoint = QtWidgets.qApp.desktop().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        self.Exit.clicked.connect(self.Exit_Window)
        
        
    def Exit_Window(self):
        self.cams = main_window.MainWindow() 
        self.cams.show()
        self.close()