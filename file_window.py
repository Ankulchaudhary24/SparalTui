import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import main_window
from general_commands import Output

FileWindow = "FileSystemCommands.ui"

Ui_FileWindow, QtBaseClass = uic.loadUiType(FileWindow)

class FileWindow(QtWidgets.QMainWindow,Ui_FileWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_FileWindow.__init__(self)
        self.setupUi(self)
        self.setFixedWidth(555)
        self.setFixedHeight(425)
        self.setWindowTitle("File System Commands Window")
        qtRectangle = self.frameGeometry()
        centerPoint = QtWidgets.qApp.desktop().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        self.cdp.clicked.connect(lambda: self.takeinputs("Enter the number of partion You want to make:",1))
        self.Exit.clicked.connect(self.Exit_Window)
        
    def takeinputs(self,__str,num): 
        name, done = QtWidgets.QInputDialog.getText( 
            self, 'Input Dialog', __str) 
        if done:
            self.cams = Output()
            stdouterr = ""
            if num == 1:
                stdouterr = os.popen("fdisk "+name).read()
            self.cams.te.setText(stdouterr)
            self.cams.show()
            
        
    def Exit_Window(self):
        self.cams = main_window.MainWindow() 
        self.cams.show()
        self.close()