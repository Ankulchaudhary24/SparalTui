import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import main_window
from general_commands import Output

ServiceWindow = "ServiceCommands.ui"

Ui_ServiceWindow, QtBaseClass = uic.loadUiType(ServiceWindow)
_str = ""

class ServiceWindow(QtWidgets.QMainWindow,Ui_ServiceWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_ServiceWindow.__init__(self)
        self.setupUi(self)
        self.setFixedWidth(555)
        self.setFixedHeight(425)
        self.setWindowTitle("Service Commands Window")
        qtRectangle = self.frameGeometry()
        centerPoint = QtWidgets.qApp.desktop().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        self.las.clicked.connect(lambda: Output_("systemctl list-units -at service"))
        self.lrs.clicked.connect(lambda: Output_("systemctl -t service --state=active"))
        self.eas.clicked.connect(lambda: takeinputs("Enter the name of the service",3))
        self.vss.clicked.connect(lambda: takeinputs("Enter the name of the service",4))
        self.ras.clicked.connect(lambda: takeinputs("Enter the name of the service",5))
        self.cise.clicked.connect(lambda: takeinputs("Enter the name of the service",6))
        self.cl.clicked.connect(lambda: Output_("systemd-journald.service"))
        self.vl.clicked.connect(lambda: Output_("journalctl"))
        self.vao.clicked.connect(lambda: Output_("cat /etc/pam.d/system-authtlog"))
        self.sbt.clicked.connect(lambda: Output_("crontab -e"))
        self.ffbn.clicked.connect(lambda: takeinputs("Enter the name of the file",11))
        self.ffbc.clicked.connect(lambda: takeinputs("Enter the name of the file",12))
        self.das.clicked.connect(lambda: takeinputs("Enter the name of the service",13))
        self.vrlt.clicked.connect(lambda: Output_("who -r"))
        self.Exit.clicked.connect(self.Exit_Window)
        
        
    def takeinputs(self,__str,num): 
        name, done = QtWidgets.QInputDialog.getText( 
            self, 'Input Dialog', __str) 
        if done:
            self.cams = Output()
            stdouterr = ""
            if num == 3:
                stdouterr = os.popen("systemctl enable "+name).read()
            if num == 4:
                stdouterr = os.popen("systemctl status "+name).read()
            if num == 5:
                stdouterr = os.popen("systemctl restart "+name).read()
            if num == 6:
                stdouterr = os.popen("systemctl is-enabled "+name).read()
            if num == 11:
                stdouterr = os.popen("locate "+name).read()
            if num == 12:
                stdouterr = os.popen("find "+name).read() 
            if num == 13:
                stdouterr = os.popen("systemctl disable "+name).read()    
            self.cams.te.setText(stdouterr)
            self.cams.show()
            
            
    def Output_(self,__str):
        _str = __str
        self.cams = Output()
        stdouterr = os.popen(_str).read()
        self.cams.te.setText(stdouterr)
        self.cams.show()
            
            
    def Exit_Window(self):
        self.cams = main_window.MainWindow() 
        self.cams.show()
        self.close() 