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

UserName = " "
logintype = 0
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
        self.YumRelatedCommands.clicked.connect(lambda: self.Window_Enter(lambda: YumWindow()))
        self.UserRelatedCommands.clicked.connect(lambda: self.Window_Enter(lambda: UserWindow()))
        self.GeneralCommands.clicked.connect(lambda: self.Window_Enter(lambda: GeneralWindow()))
        self.ServiceConfigurationSettings.clicked.connect(lambda: self.Window_Enter(lambda:ServiceWindow()))
        self.FileSystem.clicked.connect(lambda: self.Window_Enter(lambda:FileWindow()))
        self.NetworkSettings.clicked.connect(lambda: self.Window_Enter(lambda:NetworkWindow()))
        self.Exit.clicked.connect(lambda: self.Window_Enter(lambda: LoginWindow()))
        self.h = QtWidgets.QLabel()
        
    def Window_Enter(self,s):
        self.cams=s()
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