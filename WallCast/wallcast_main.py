from PyQt5 import QtCore, QtGui, QtWidgets

import WallCast.wallcast_functions
import wallcast_functions

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 720))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 720))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setWindowTitle("WallCast")
        MainWindow.setStyleSheet("background-color: rgb(157, 161, 170);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1280, 60))
        self.frame.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_logo = QtWidgets.QLabel(self.frame)
        self.label_logo.setGeometry(QtCore.QRect(10, 0, 81, 61))
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap("C:\\Users\\PC\\PycharmProjects\\pythonProject\\WallCast\\logo wallcast.png"))
        self.label_logo.setObjectName("label_logo")
        self.pushButton_tape = QtWidgets.QPushButton(self.frame)
        self.pushButton_tape.setGeometry(QtCore.QRect(110, 10, 141, 41))
        self.pushButton_tape.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 26pt \"Bahnschrift SemiLight Condensed\";\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"border-color: beige;\n"
"font: bold 28px;\n"
"padding: 2px;")
        self.pushButton_tape.setObjectName("pushButton_tape")
        self.pushButton_subscriptions = QtWidgets.QPushButton(self.frame)
        self.pushButton_subscriptions.setGeometry(QtCore.QRect(270, 10, 141, 41))
        self.pushButton_subscriptions.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 26pt \"Bahnschrift SemiLight Condensed\";\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"border-color: beige;\n"
"font: bold 28px;\n"
"padding: 2px;")
        self.pushButton_subscriptions.setObjectName("pushButton_subscriptions")
        self.pushButton_messages = QtWidgets.QPushButton(self.frame)
        self.pushButton_messages.setGeometry(QtCore.QRect(430, 10, 141, 41))
        self.pushButton_messages.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 26pt \"Bahnschrift SemiLight Condensed\";\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"border-color: beige;\n"
"font: bold 28px;\n"
"padding: 2px;")
        self.pushButton_messages.setObjectName("pushButton_messages")
        self.pushButton_profil = QtWidgets.QPushButton(self.frame)
        self.pushButton_profil.setGeometry(QtCore.QRect(1220, 5, 51, 51))
        self.pushButton_profil.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"border-color: beige;\n"
"font: bold 16px;\n"
"padding: 6px;")
        self.pushButton_profil.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\PC\\PycharmProjects\\pythonProject\\WallCast\\ava_wallcast.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_profil.setIcon(icon)
        self.pushButton_profil.setIconSize(QtCore.QSize(77, 54))
        self.pushButton_profil.setAutoRepeat(False)
        self.pushButton_profil.setObjectName("pushButton_profil")
        self.label_logo.raise_()
        self.pushButton_subscriptions.raise_()
        self.pushButton_messages.raise_()
        self.pushButton_profil.raise_()
        self.pushButton_tape.raise_()
        self.fon = QtWidgets.QFrame(self.centralwidget)
        self.fon.setGeometry(QtCore.QRect(160, 60, 960, 662))
        self.fon.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fon.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fon.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fon.setObjectName("fon")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(80, 40, 201, 121))
        self.frame_2.setVisible(False)
        self.frame_2.setStyleSheet("border-style: outset;\n"
"background-color: rgb(0, 0, 0);\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"font: bold 28px;\n"
"padding: 2px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton_tape_global = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_tape_global.setGeometry(QtCore.QRect(5, 20, 191, 41))
        self.pushButton_tape_global.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 26pt \"Bahnschrift SemiLight Condensed\";\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"border-color: beige;\n"
"font: bold 28px;\n"
"padding: 2px;")
        self.pushButton_tape_global.setObjectName("pushButton_tape_2")
        self.pushButton_tape_subscriptions = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_tape_subscriptions.setGeometry(QtCore.QRect(5, 70, 191, 41))
        self.pushButton_tape_subscriptions.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 26pt \"Bahnschrift SemiLight Condensed\";\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"border-color: beige;\n"
"font: bold 28px;\n"
"padding: 2px;")
        self.pushButton_tape_subscriptions.setObjectName("pushButton_tape_3")
        self.fon.raise_()
        self.frame_2.raise_()
        self.frame.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.function_wallcast()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton_tape.setText(_translate("MainWindow", "Лента"))
        self.pushButton_subscriptions.setText(_translate("MainWindow", "Подписки"))
        self.pushButton_messages.setText(_translate("MainWindow", "Сообщения"))
        self.pushButton_tape_global.setText(_translate("MainWindow", "Глобальная лента"))
        self.pushButton_tape_subscriptions.setText(_translate("MainWindow", "Лента подписок"))

    def function_wallcast(self):
        self.pushButton_tape.clicked.connect(self.wallcast_tape_but_click)

    def wallcast_tape_but_click(self):
        self.frame_2.setVisible(True)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())