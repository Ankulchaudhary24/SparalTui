import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import main_window

GeneralWindow = "GeneralCommands.ui"
Ui_GeneralWindow, QtBaseClass = uic.loadUiType(GeneralWindow)

_str = ""

class Output(QtWidgets.QWidget):
    def __init__(self, *args):
        QtWidgets.QWidget.__init__(self, *args)

        label = QtWidgets.QLabel("Output Of The Command: ")
        self.te = QtWidgets.QTextEdit()
        qbtn = QtWidgets.QPushButton('Quit', self)
        qbtn.clicked.connect(self.Quit)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(qbtn)
        layout.addWidget(label)
        layout.addWidget(self.te)
        self.setLayout(layout)
        self.setWindowTitle("Output Window")
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint,False)
        qtRectangle = self.frameGeometry()
        centerPoint = QtWidgets.qApp.desktop().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        self.te.setTextColor(QtGui.QColor(200,100,0))
        self.te.setReadOnly(True)
    
    def Quit(self):
        self.close()
        

class GeneralWindow(QtWidgets.QMainWindow,Ui_GeneralWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_GeneralWindow.__init__(self)
        self.setupUi(self)
        self.setFixedWidth(555)
        self.setFixedHeight(425)
        self.setWindowTitle("General Commands Window")
        qtRectangle = self.frameGeometry()
        centerPoint = QtWidgets.qApp.desktop().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        self.Exit.clicked.connect(self.Exit_Window)
        self.Date.clicked.connect(lambda: self.Output_("date"))
        self.kcu.clicked.connect(lambda: self.Output_("whoami"))
        self.Calender.clicked.connect(lambda: self.Output_("cal"))
        self.CurrentLocation.clicked.connect(lambda: self.Output_("pwd"))
        self.CopyFile.clicked.connect(lambda: self.takeinputs("Enter the present address:",1))
        self.MoveFile.clicked.connect(lambda: self.takeinputs("Enter the present address:",2))
        self.StartService.clicked.connect(lambda:self.takeinputs("Enter the name of service:",3))
        self.StopService.clicked.connect(lambda:self.takeinputs("Enter the name of service:",4))
        self.RemoveFile.clicked.connect(lambda: self.takeinputs("Enter the address of file:",9))
        
    def takeinputs(self,__str,num): 
        name, done = QtWidgets.QInputDialog.getText( 
            self, 'Input Dialog', __str)  
        if done:
            self.cams = Output()
            stdouterr = ""
            if num == 1:
                name1, done1 = QtWidgets.QInputDialog.getText( 
                    self, 'Input Dialog',"Enter the destination address")
                stdouterr = os.popen("cp "+name+" "+name1).read()
                
            if num == 2:
                name1, done1 = QtWidgets.QInputDialog.getText( 
                    self, 'Input Dialog',"Enter the destination address")
                stdouterr = os.popen("mv "+name+" "+name1).read()
            
            if num == 3:
                stdouterr = os.popen("systemctl start "+name).read()
               
            if num == 4:
                stdouterr = os.popen("systemctl stop "+name).read()

            if num == 9:
                stdouterr = os.popen("rm -f "+name).read()

            if len(stdouterr) == 0:
                stdouterr = "Your Work Is Completed!!"
                
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