from PyQt5 import QtCore, QtGui, QtWidgets

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
        '''Верхняя чёрная полоса'''
        self.box_top_selection = QtWidgets.QFrame(self.centralwidget)
        self.box_top_selection.setGeometry(QtCore.QRect(0, -1, 1280, 71))
        self.box_top_selection.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.box_top_selection.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.box_top_selection.setFrameShadow(QtWidgets.QFrame.Raised)
        self.box_top_selection.setObjectName("box_top_selection")
        '''Логотип wallcast'''
        self.label_logo = QtWidgets.QLabel(self.box_top_selection)
        self.label_logo.setGeometry(QtCore.QRect(10, 0, 81, 71))
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap("C:\\Users\\PC\\PycharmProjects\\pythonProject\\WallCast\\logo_wallcast.png"))
        self.label_logo.setObjectName("label_logo")
        '''Кнопка "Лента"'''
        self.pushButton_tape = QtWidgets.QPushButton(self.box_top_selection)
        self.pushButton_tape.setGeometry(QtCore.QRect(110, 16, 141, 41))
        self.pushButton_tape.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 26pt \"Bahnschrift SemiLight Condensed\";\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"border-color: beige;\n"
"font: bold 28px;\n"
"padding: 2px;")
        self.pushButton_tape.setObjectName("pushButton_tape")
        '''Кнопка "Подписки"'''
        self.pushButton_subscriptions = QtWidgets.QPushButton(self.box_top_selection)
        self.pushButton_subscriptions.setGeometry(QtCore.QRect(280, 16, 141, 41))
        self.pushButton_subscriptions.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 26pt \"Bahnschrift SemiLight Condensed\";\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"border-color: beige;\n"
"font: bold 28px;\n"
"padding: 2px;")
        self.pushButton_subscriptions.setObjectName("pushButton_subscriptions")
        '''кнопка "Сообщения"'''
        self.pushButton_messages = QtWidgets.QPushButton(self.box_top_selection)
        self.pushButton_messages.setGeometry(QtCore.QRect(450, 16, 141, 41))
        self.pushButton_messages.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 26pt \"Bahnschrift SemiLight Condensed\";\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"border-color: beige;\n"
"font: bold 28px;\n"
"padding: 2px;")
        self.pushButton_messages.setObjectName("pushButton_messages")
        '''кнопка "Профиль"'''
        self.pushButton_profil = QtWidgets.QPushButton(self.box_top_selection)
        self.pushButton_profil.setGeometry(QtCore.QRect(1220, 11, 51, 51))
        self.pushButton_profil.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"border-color: beige;\n"
"font: bold 16px;\n"
"padding: 6px;")
        self.pushButton_profil.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\PC\\PycharmProjects\\pythonProject\\WallCast\\ava_wallcast.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)    # импорт фотографии аватарки
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
        self.fon.setGeometry(QtCore.QRect(160, 71, 960, 651))
        self.fon.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fon.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fon.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fon.setObjectName("fon")
        self.box_tape_slection = QtWidgets.QFrame(self.centralwidget)
        self.box_tape_slection.setVisible(False)
        self.box_tape_slection.setGeometry(QtCore.QRect(80, 60, 201, 111))
        self.box_tape_slection.setStyleSheet("border-style: outset;\n"
"background-color: rgb(0, 0, 0);\n"
"border-width: 2px;\n"
"border-bottom-left-radius: 20px;\n"
"border-bottom-right-radius: 20px;\n"
"font: bold 28px;\n"
"padding: 2px;")
        self.box_tape_slection.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.box_tape_slection.setFrameShadow(QtWidgets.QFrame.Raised)
        self.box_tape_slection.setObjectName("box_tape_slection")
        self.pushButton_tape_2 = QtWidgets.QPushButton(self.box_tape_slection)
        self.pushButton_tape_2.setGeometry(QtCore.QRect(5, 10, 191, 41))
        self.pushButton_tape_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 26pt \"Bahnschrift SemiLight Condensed\";\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"border-color: beige;\n"
"font: bold 24px;\n"
"padding: 2px;")
        self.pushButton_tape_2.setObjectName("pushButton_tape_2")
        self.pushButton_tape_3 = QtWidgets.QPushButton(self.box_tape_slection)
        self.pushButton_tape_3.setGeometry(QtCore.QRect(5, 60, 191, 41))
        self.pushButton_tape_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 26pt \"Bahnschrift SemiLight Condensed\";\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"border-color: beige;\n"
"font: bold 24px;\n"
"padding: 2px;")
        self.pushButton_tape_3.setObjectName("pushButton_tape_3")
        self.box_settings = QtWidgets.QFrame(self.centralwidget)
        self.box_settings.setGeometry(QtCore.QRect(1130, 70, 151, 221))
        self.box_settings.setMouseTracking(False)
        self.box_settings.setVisible(False)
        self.box_settings.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-bottom-left-radius: 20px;")
        self.box_settings.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.box_settings.setFrameShadow(QtWidgets.QFrame.Raised)
        self.box_settings.setObjectName("box_settings")
        self.label = QtWidgets.QLabel(self.box_settings)
        self.label.setGeometry(QtCore.QRect(10, 0, 131, 31))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"font: 16pt \"Bahnschrift SemiLight Condensed\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.box_settings)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 131, 31))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"font: 16pt \"Bahnschrift SemiLight Condensed\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.box_settings)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 131, 31))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"font: 16pt \"Bahnschrift SemiLight Condensed\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.box_settings)
        self.label_4.setGeometry(QtCore.QRect(10, 180, 131, 31))
        self.label_4.setStyleSheet("color: rgb(170, 69, 52);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"font: 16pt \"Bahnschrift SemiLight Condensed\";")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.box_settings)
        self.label_5.setGeometry(QtCore.QRect(10, 140, 131, 31))
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"font: 16pt \"Bahnschrift SemiLight Condensed\";")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.fon.raise_()
        self.box_top_selection.raise_()
        self.box_settings.raise_()
        self.box_tape_slection.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.function_wallcast()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton_tape.setText(_translate("MainWindow", "Лента"))
        self.pushButton_subscriptions.setText(_translate("MainWindow", "Подписки"))
        self.pushButton_messages.setText(_translate("MainWindow", "Сообщения"))
        self.pushButton_tape_2.setText(_translate("MainWindow", "Глобальная лента"))
        self.pushButton_tape_3.setText(_translate("MainWindow", "Лента подписок"))
        self.label.setText(_translate("MainWindow", "Q1rD"))
        self.label_2.setText(_translate("MainWindow", "Поддержка"))
        self.label_3.setText(_translate("MainWindow", "Настройки"))
        self.label_4.setText(_translate("MainWindow", "Выйти"))
        self.label_5.setText(_translate("MainWindow", "Сменить аккаунт"))
    '''Все функции кнопок'''
    def function_wallcast(self):
        self.pushButton_tape.clicked.connect(self.wallcast_tape_button_click)
        self.pushButton_profil.clicked.connect(self.wallcast_profil_top_butt_click)

    def wallcast_tape_button_click(self):
        self.box_tape_slection.setVisible(True)
    def wallcast_profil_top_butt_click(self):
        self.box_settings.setVisible(True)
'''Запуск программы'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
