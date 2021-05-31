# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'second.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(784, 605)
        LoginWindow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        LoginWindow.setStyleSheet("QMainWindow {\n"
"        background-color: \'#8bbdd9\';\n"
"}")
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setStyleSheet("QWidget {\n"
"        background-color: \'#8bbdd9\';\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 0, 361, 301))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("logo2.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 320, 121, 31))
        self.label_2.setStyleSheet("QLabel{\n"
"        font-size: 25px;\n"
"        color: \'white\';\n"
"}")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 410, 111, 20))
        self.label_3.setStyleSheet("QLabel{\n"
"        font-size: 25px;\n"
"        color: \'white\';\n"
"}")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(350, 320, 191, 51))
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"        border: 4px solid \'white\';\n"
"        font-size: 20px;\n"
"        color: \'white\';\n"
"        background-color: \'#298fca\';\n"
"        padding: 10px;\n"
"\n"
"}\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(350, 390, 191, 51))
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
"        border: 4px solid \'white\';\n"
"        font-size: 20px;\n"
"        color: \'white\';\n"
"        background-color: \'#298fca\';\n"
"        padding: 10px;\n"
"\n"
"}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(110, 270, 71, 91))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("user.png"))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(110, 360, 81, 81))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("password.png"))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(450, 450, 101, 20))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.backbutton = QtWidgets.QPushButton(self.centralwidget)
        self.backbutton.setGeometry(QtCore.QRect(250, 480, 151, 71))
        self.backbutton.setStyleSheet("QPushButton{\n"
"        border-radius : 30;\n"
"        border: 6px solid \'#0079bf\';\n"
"        border-style: double;\n"
"        font-size: 20px;\n"
"        color: \'white\';\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backbutton.setIcon(icon)
        self.backbutton.setIconSize(QtCore.QSize(40, 40))
        self.backbutton.setObjectName("backbutton")
        self.loginbutton = QtWidgets.QPushButton(self.centralwidget)
        self.loginbutton.setGeometry(QtCore.QRect(440, 480, 151, 71))
        self.loginbutton.setStyleSheet("QPushButton{\n"
"        border-radius : 30;\n"
"        border: 6px solid \'#0079bf\';\n"
"        border-style: double;\n"
"        font-size: 20px;\n"
"        color: \'white\';\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.loginbutton.setIcon(icon1)
        self.loginbutton.setIconSize(QtCore.QSize(40, 40))
        self.loginbutton.setObjectName("loginbutton")
        LoginWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LoginWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 784, 21))
        self.menubar.setObjectName("menubar")
        LoginWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LoginWindow)
        self.statusbar.setObjectName("statusbar")
        LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "MainWindow"))
        self.label_2.setText(_translate("LoginWindow", "Username"))
        self.label_3.setText(_translate("LoginWindow", "Password"))
        self.lineEdit.setPlaceholderText(_translate("LoginWindow", "enter username"))
        self.lineEdit_2.setPlaceholderText(_translate("LoginWindow", "enter password"))
        self.label_6.setText(_translate("LoginWindow", "Forgot password?"))
        self.backbutton.setText(_translate("LoginWindow", "Back"))
        self.loginbutton.setText(_translate("LoginWindow", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())
