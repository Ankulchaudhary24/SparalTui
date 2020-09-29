import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import main_window
from general_commands import Output

YumWindow = "YumCommands.ui"

Ui_YumWindow, QtBaseClass = uic.loadUiType(YumWindow)

__str =""

class EmbTerminal(QtWidgets.QWidget):
    def __init__(self, *args):
        QtWidgets.QWidget.__init__(self, *args)
        self.process = QtCore.QProcess(self)
        self.terminal = QtWidgets.QWidget(self)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.terminal)
        self.setFixedSize(555,425)
        self.process.start('urxvt',['-embed', str(int(self.winId()))])
      
        
class YumWindow(QtWidgets.QMainWindow,Ui_YumWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_YumWindow.__init__(self)
        self.setupUi(self)
        self.setFixedWidth(555)
        self.setFixedHeight(425)
        self.setWindowTitle("Yum Commands Window")
        qtRectangle = self.frameGeometry()
        centerPoint = QtWidgets.qApp.desktop().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        self.yrc.clicked.connect(lambda: self.Output_("dnf -y install https://download1.rpmfusion.org/free/el/rpmfusion-free-release-8.noarch.rpm"))
        self.yrc.clicked.connect(lambda: self.Output_("dnf -y install https://fedoraproject.org/pub/epel-release-latest-8.noarch.rpm"))
        self.wtis.clicked.connect(lambda: self.takeinputs("Enter the name of package:",2))
        self.wtds.clicked.connect(lambda: self.takeinputs("Enter the name of package:",3))
        self.uap.clicked.connect(lambda: self.takeinputs("Enter the name of package:",4))
        self.lap.clicked.connect(lambda: self.takeinputs("Enter the name of package:",5))
        self.sap.clicked.connect(lambda: self.takeinputs("Enter the name of package:",6))
        self.gioap.clicked.connect(lambda: self.takeinputs("Enter the name of package:",7))
        self.laip.clicked.connect(lambda: self.Output_("yum list installed"))
        self.ypf.clicked.connect(lambda: self.takeinputs("Enter the name of function:",9))
        self.us.clicked.connect(lambda: self.Output_("yum update"))
        self.cfau.clicked.connect(lambda: self.Output_("yum check-update"))
        self.YumShell.clicked.connect(lambda: self.yum_shell())
        self.Exit.clicked.connect(self.Exit_Window)
        
    def takeinputs(self,__str,num): 
        name, done = QtWidgets.QInputDialog.getText( 
            self, 'Input Dialog', __str) 
        if done:
            self.cams = Output()
            stdouterr = ""
            if num == 2:
                stdouterr = os.popen("yum install "+name).read()
            if num == 3:
                stdouterr = os.popen("yum remove "+name).read()
            if num == 4:
                stdouterr = os.popen("yum update "+name).read()
            if num == 5:
                stdouterr = os.popen("yum list "+name).read()
            if num == 6:
                stdouterr = os.popen("yum search "+name).read()
            if num == 7:
                stdouterr = os.popen("yum info "+name).read()
            if num == 9:
                stdouterr = os.popen("yum provides "+name).read()
            self.cams.te.setText(stdouterr)
            self.cams.show()
            
    def yum_shell(self):
        self.cams = EmbTerminal()
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