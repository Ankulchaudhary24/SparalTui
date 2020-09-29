import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import getpass
import main_window

LoginWindow = "LoginWindow.ui"
Ui_LoginWindow, QtBaseClass = uic.loadUiType(LoginWindow)

class Dialog(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(
            QtWidgets.QStyle.alignedRect(
                QtCore.Qt.LeftToRight,
                QtCore.Qt.AlignCenter,
                self.size(),
                QtWidgets.qApp.desktop().availableGeometry(),
        ))

        QtWidgets.QMessageBox.question(self, 'Alert Message!!', "Please Enter the Correct Credentials!",QtWidgets.QMessageBox.Ok)
        self.show()


class LoginWindow(QtWidgets.QMainWindow, Ui_LoginWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_LoginWindow.__init__(self)
        self.setupUi(self)
        self.setFixedWidth(555)
        self.setFixedHeight(425)
        self.textEdit.setDisabled(True)
        self.textEdit_2.setDisabled(True)
        self.setWindowTitle("Login Window")
        qtRectangle = self.frameGeometry()
        centerPoint = QtWidgets.qApp.desktop().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.returnPressed.connect(self.MainWindow_Enter)
        self.choice1.clicked.connect(self.MainWindow_Enter)
        
    def takeinputs(self): 
        name, done1 = QtWidgets.QInputDialog.getText( 
             self, 'Input Dialog', 'Enter the Ip Address for remote access:')  
            
    def MainWindow_Enter(self):
        if self.password.text() == 'sparal' and self.name.text():
#             if self.choice.value() == 1:
#                 self.takeinputs()
#             else:
            self.cams = main_window.MainWindow()
            self.cams.NameSetter(self.name)
            self.cams.login(self.choice.value())
            self.cams.show()
            self.close()
        else:
            Dialog()
   

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
    


