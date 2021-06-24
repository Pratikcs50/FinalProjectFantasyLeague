


from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_openWindow(object):
    def setupUi(self, openWindow):
        openWindow.setObjectName("Window")
        openWindow.resize(535, 389)
        self.centralwidget = QtWidgets.QWidget(openWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.OpenTeam = QtWidgets.QLabel(self.centralwidget)
        self.OpenTeam.setGeometry(QtCore.QRect(150, 120, 231, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.OpenTeam.setFont(font)
        self.OpenTeam.setObjectName("OpenTeam")
        self.OpenTheTeam = QtWidgets.QLineEdit(self.centralwidget)
        self.OpenTheTeam.setGeometry(QtCore.QRect(180, 160, 151, 22))
        self.OpenTheTeam.setObjectName("OpenTheTeam")
        self.openButton = QtWidgets.QPushButton(self.centralwidget)
        self.openButton.setGeometry(QtCore.QRect(210, 210, 93, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.openButton.setFont(font)
        self.openButton.setObjectName("openButton")
        openWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(openWindow)
        self.statusbar.setObjectName("statusbar")
        openWindow.setStatusBar(self.statusbar)

        self.retranslateUi(openWindow)
        QtCore.QMetaObject.connectSlotsByName(openWindow)

    def retranslateUi(self, openWindow):
        _translate = QtCore.QCoreApplication.translate
        openWindow.setWindowTitle(_translate("Window", "Fan Page"))
        self.OpenTeam.setText(_translate("Window", "Enter Team Name"))
        self.openButton.setText(_translate("openWindow", "OK"))


if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    openWindow = QtWidgets.QMainWindow()
    ui = Ui_openWindow()
    ui.setupUi(openWindow)
    openWindow.show()
    sys.exit(app.exec_())
