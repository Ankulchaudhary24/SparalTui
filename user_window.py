import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import main_window
from general_commands import Output

UserWindow = "UserCommands.ui"

Ui_UserWindow, QtBaseClass = uic.loadUiType(UserWindow)

class UserWindow(QtWidgets.QMainWindow,Ui_UserWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_UserWindow.__init__(self)
        self.setupUi(self)
        self.setFixedWidth(555)
        self.setFixedHeight(425)
        self.setWindowTitle("User Commands Window")
        qtRectangle = self.frameGeometry()
        centerPoint = QtWidgets.qApp.desktop().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        self.CreateUserAccount.clicked.connect(lambda: self.takeinputs("Enter the name of User:",1))
        self.DeleteUserAccount.clicked.connect(lambda: self.takeinputs("Enter the name of User:",2))
        self.ViewUserAccount.clicked.connect(lambda: self.takeinputs("Enter the name of User:",3))
        self.CreateUserGroup.clicked.connect(lambda: self.takeinputs("Enter the name of Group:",4))
        self.DeleteUserGroup.clicked.connect(lambda: self.takeinputs("Enter the name of Group:",5))
        self.ChangeGroupDetails.clicked.connect(lambda: self.takeinputs("Enter the name of Group:",6))
        self.ChangeUserPassword.clicked.connect(lambda: self.takeinputs("Enter the name of User:",7))
        self.ChangeUserPermission.clicked.connect(lambda: self.takeinputs("Enter the name of User:",8))
        self.ChangeGroupPermisson.clicked.connect(lambda: self.takeinputs("Enter the name of Group:",9))
        self.ViewUserSession.clicked.connect(lambda: self.takeinputs("Enter the name of User:",10))
        self.Exit.clicked.connect(self.Exit_Window)
        
    def takeinputs(self,__str,num): 
        name, done = QtWidgets.QInputDialog.getText( 
            self, 'Input Dialog', __str) 
        if done:
            self.cams = Output()
            stdouterr = ""
            if num == 1:
                stdouterr = os.popen("useradd "+name).read()
            if num == 2:
                stdouterr = os.popen("userdel "+name).read()   
            if num == 3:
                stdouterr = os.popen("id "+name).read()   
            if num == 4:
                stdouterr = os.popen("groupadd "+name).read()
            if num == 5:
                stdouterr = os.popen("groupdel "+name).read() 
            if num == 6:
                stdouterr = os.popen("groupmod "+name).read()  
            if num == 7:
                stdouterr = os.popen("passwd "+name).read()
            if num == 8:
                stdouterr = os.popen("usermod "+name).read()
            if num == 9:
                stdouterr = os.popen("groupmod "+name).read()
            if num == 10:
                stdouterr = os.popen("w "+name).read()    
            self.cams.te.setText(stdouterr)
            self.cams.show()   
        
        
    def Exit_Window(self):
        self.cams = main_window.MainWindow() 
        self.cams.show()
        self.close()