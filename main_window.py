import sys, os
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from yum_window import YumWindow
from login_window import LoginWindow
from user_window import UserWindow
from yum_window import YumWindow
from file_window import FileWindow
from general_commands import GeneralWindow
from network_window import NetworkWindow
from service_window import ServiceWindow

MainWindow = "MainWindow.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(MainWindow)

class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        date = os.popen("date +%A__%d.%m.%Y").read()
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setFixedWidth(555)
        self.setFixedHeight(425)
        qtRectangle = self.frameGeometry()
        centerPoint = QtWidgets.qApp.desktop().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        self.setWindowTitle("Main Window")
        self.date.setText(str(date))
        self.YumRelatedCommands.clicked.connect(self.YumWindow_Enter)
        self.UserRelatedCommands.clicked.connect(self.UserWindow_Enter)
        self.GeneralCommands.clicked.connect(self.GeneralWindow_Enter)
        self.ServiceConfigurationSettings.clicked.connect(self.ServiceWindow_Enter)
        self.FileSystem.clicked.connect(self.FileWindow_Enter)
        self.NetworkSettings.clicked.connect(self.NetworkWindow_Enter)
        self.Exit.clicked.connect(self.Exit_Window)
        self.h = QtWidgets.QLabel()
        
    def Exit_Window(self):
        self.cams = LoginWindow() 
        self.cams.show()
        self.close()
        
    def YumWindow_Enter(self):
        self.cams = YumWindow() 
        self.cams.show()
        self.close()
        
    def UserWindow_Enter(self):
        self.cams = UserWindow() 
        self.cams.show()
        self.close()
        
    def GeneralWindow_Enter(self):
        self.cams = GeneralWindow() 
        self.cams.show()
        self.close()
    
    def FileWindow_Enter(self):
        self.cams = FileWindow() 
        self.cams.show()
        self.close()
    
    def NetworkWindow_Enter(self):
        self.cams = NetworkWindow() 
        self.cams.show()
        self.close()
        
    def ServiceWindow_Enter(self):
        self.cams = ServiceWindow() 
        self.cams.show()
        self.close()
        
    def NameSetter(self,n):
        self.h.setText(n.text())
        self.user.setText(self.h.text())
    
    def login(self,l):
        if l == 0:
            self.LoginType.setText("Local Login")
        else :
            self.LoginType.setText("Remote Login")