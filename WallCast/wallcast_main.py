from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import pyautogui

import wallcast_functions

class Ui_MainWindow(QMainWindow, object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 720))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 720))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setWindowTitle("WallCast")
        icon = QtGui.QIcon("C:\\Users\\PC\\PycharmProjects\\pythonProject\\WallCast\\logo_wallcast.png")
        icon.addPixmap(QtGui.QPixmap(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(157, 161, 170);")
        MainWindow.setIconSize(QtCore.QSize(24, 24))
        MainWindow.setStyleSheet("background-color: rgb(157, 161, 170);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.box_top_selection = QtWidgets.QFrame(self.centralwidget)
        self.box_top_selection.setGeometry(QtCore.QRect(0, -1, 1280, 71))
        self.box_top_selection.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.box_top_selection.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.box_top_selection.setFrameShadow(QtWidgets.QFrame.Raised)
        self.box_top_selection.setObjectName("box_top_selection")
        self.label_logo = QtWidgets.QLabel(self.box_top_selection)
        self.label_logo.setGeometry(QtCore.QRect(10, 0, 81, 71))
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap("C:\\Users\\PC\\PycharmProjects\\pythonProject\\WallCast\\logo_wallcast.png"))
        self.label_logo.setObjectName("label_logo")
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
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\PC\\PycharmProjects\\pythonProject\\WallCast\\ava_wallcast.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_profil.setIcon(icon)
        self.pushButton_profil.setIconSize(QtCore.QSize(77, 54))
        self.pushButton_profil.setAutoRepeat(False)
        self.pushButton_profil.setObjectName("pushButton_profil")
        self.pushButton = QtWidgets.QPushButton(self.box_top_selection)
        self.pushButton.setGeometry(QtCore.QRect(1160, 16, 41, 41))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"border-color: beige;\n"
"font: bold 16px;\n"
"padding: 6px;")
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:\\Users\\PC\\PycharmProjects\\pythonProject\\WallCast\\kolokol_wallcast.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(28, 28))
        self.pushButton.setObjectName("pushButton")
        self.label_logo.raise_()
        self.pushButton_subscriptions.raise_()
        self.pushButton_messages.raise_()
        self.pushButton_profil.raise_()
        self.pushButton_tape.raise_()
        self.pushButton.raise_()
        self.fon_subscriptions = QtWidgets.QFrame(self.centralwidget)
        self.fon_subscriptions.setVisible(False)
        self.fon_subscriptions.setGeometry(QtCore.QRect(160, 61, 960, 661))
        self.fon_subscriptions.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fon_subscriptions.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fon_subscriptions.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fon_subscriptions.setObjectName("fon_subscriptions")
        self.box_subscriptions_top = QtWidgets.QWidget(self.fon_subscriptions)
        self.box_subscriptions_top.setGeometry(QtCore.QRect(0, 9, 961, 61))
        self.box_subscriptions_top.setStyleSheet("background-color: rgb(66, 70, 70);")
        self.box_subscriptions_top.setObjectName("box_subscriptions_top")
        self.filters_subscriptions = QtWidgets.QLabel(self.box_subscriptions_top)
        self.filters_subscriptions.setGeometry(QtCore.QRect(410, 8, 121, 41))
        self.filters_subscriptions.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 14px;\n"
"font: 18pt \"Bahnschrift SemiLight Condensed\";\n"
"")
        self.filters_subscriptions.setAlignment(QtCore.Qt.AlignCenter)
        self.filters_subscriptions.setObjectName("filters_subscriptions")
        self.lineEdit = QtWidgets.QLineEdit(self.box_subscriptions_top)
        self.lineEdit.setGeometry(QtCore.QRect(30, 10, 361, 41))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 14px;\n"
"font: 18pt \"Bahnschrift SemiLight Condensed\";\n"
"")
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setMaxLength(32767)
        self.lineEdit.setObjectName("lineEdit")
        self.window_box_subscriptions_allinfo = QtWidgets.QFrame(self.fon_subscriptions)
        self.window_box_subscriptions_allinfo.setGeometry(QtCore.QRect(110, 100, 741, 101))
        self.window_box_subscriptions_allinfo.setStyleSheet("border-radius: 16px;\n"
"background-color: rgb(138, 144, 140);")
        self.window_box_subscriptions_allinfo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.window_box_subscriptions_allinfo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.window_box_subscriptions_allinfo.setObjectName("window_box_subscriptions_allinfo")
        self.window_subscriptions_box_ava = QtWidgets.QLabel(self.window_box_subscriptions_allinfo)
        self.window_subscriptions_box_ava.setGeometry(QtCore.QRect(20, 10, 81, 81))
        self.window_subscriptions_box_ava.setStyleSheet("border-radius: 8px;")
        self.window_subscriptions_box_ava.setText("")
        self.window_subscriptions_box_ava.setPixmap(QtGui.QPixmap("C:\\Users\\PC\\PycharmProjects\\pythonProject\\WallCast\\logo_wallcast.png"))
        self.window_subscriptions_box_ava.setObjectName("window_subscriptions_box_ava")
        self.window_subscriptions_box_textinfo = QtWidgets.QLabel(self.window_box_subscriptions_allinfo)
        self.window_subscriptions_box_textinfo.setGeometry(QtCore.QRect(100, 20, 441, 61))
        self.window_subscriptions_box_textinfo.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 0px;\n"
"border-bottom-right-radius: 16px;\n"
"border-top-right-radius: 16px;")
        self.window_subscriptions_box_textinfo.setText("")
        self.window_subscriptions_box_textinfo.setObjectName("window_subscriptions_box_textinfo")
        self.window_subscriptions_box_timesum = QtWidgets.QLabel(self.window_box_subscriptions_allinfo)
        self.window_subscriptions_box_timesum.setGeometry(QtCore.QRect(570, 20, 141, 60))
        self.window_subscriptions_box_timesum.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 12px;\n"
"font: 14pt \"Bahnschrift SemiLight Condensed\";")
        self.window_subscriptions_box_timesum.setObjectName("window_subscriptions_box_timesum")
        self.box_tape_slection = QtWidgets.QFrame(self.centralwidget)
        self.box_tape_slection.setGeometry(QtCore.QRect(80, 60, 201, 111))
        self.box_tape_slection.setStyleSheet("border-style: outset;\n"
"background-color: rgb(0, 0, 0);\n"
"border-width: 2px;\n"
"border-bottom-left-radius: 20px;\n"
"border-bottom-right-radius: 20px;\n"
"font: bold 28px;\n"
"padding: 2px;")
        self.box_tape_slection.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.box_tape_slection.setVisible(False)
        self.box_tape_slection.setFrameShadow(QtWidgets.QFrame.Raised)
        self.box_tape_slection.setObjectName("box_tape_slection")
        self.pushButton_tape_2 = QtWidgets.QPushButton(self.box_tape_slection)
        self.pushButton_tape_2.setGeometry(QtCore.QRect(10, 10, 181, 41))
        self.pushButton_tape_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 26pt \"Bahnschrift SemiLight Condensed\";\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 16px;\n"
"border-color: beige;\n"
"font: bold 24px;\n"
"padding: 2px;")
        self.pushButton_tape_2.setObjectName("pushButton_tape_2")
        self.pushButton_tape_3 = QtWidgets.QPushButton(self.box_tape_slection)
        self.pushButton_tape_3.setGeometry(QtCore.QRect(10, 60, 181, 41))
        self.pushButton_tape_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 26pt \"Bahnschrift SemiLight Condensed\";\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 16px;\n"
"border-color: beige;\n"
"font: bold 24px;\n"
"padding: 2px;")
        self.pushButton_tape_3.setObjectName("pushButton_tape_3")
        self.box_settings = QtWidgets.QFrame(self.centralwidget)
        self.box_settings.setGeometry(QtCore.QRect(1110, 70, 171, 231))
        self.box_settings.setMouseTracking(False)
        self.box_settings.setVisible(False)
        self.box_settings.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-bottom-left-radius: 20px;")
        self.box_settings.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.box_settings.setFrameShadow(QtWidgets.QFrame.Raised)
        self.box_settings.setObjectName("box_settings")
        self.nickname = QtWidgets.QLabel(self.box_settings)
        self.nickname.setGeometry(QtCore.QRect(10, 0, 151, 31))
        self.nickname.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"font: 16pt \"Bahnschrift SemiLight Condensed\";")
        self.nickname.setAlignment(QtCore.Qt.AlignCenter)
        self.nickname.setObjectName("nickname")
        self.support_button_profil = QtWidgets.QLabel(self.box_settings)
        self.support_button_profil.setGeometry(QtCore.QRect(10, 40, 151, 31))
        self.support_button_profil.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"font: 16pt \"Bahnschrift SemiLight Condensed\";")
        self.support_button_profil.setAlignment(QtCore.Qt.AlignCenter)
        self.support_button_profil.setObjectName("support_button_profil")
        self.settings_button_profil = QtWidgets.QLabel(self.box_settings)
        self.settings_button_profil.setGeometry(QtCore.QRect(10, 80, 151, 31))
        self.settings_button_profil.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"font: 16pt \"Bahnschrift SemiLight Condensed\";")
        self.settings_button_profil.setAlignment(QtCore.Qt.AlignCenter)
        self.settings_button_profil.setObjectName("settings_button_profil")
        self.log_off_button_profil = QtWidgets.QLabel(self.box_settings)
        self.log_off_button_profil.setGeometry(QtCore.QRect(10, 180, 151, 31))
        self.log_off_button_profil.setStyleSheet("color: rgb(170, 69, 52);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"font: 16pt \"Bahnschrift SemiLight Condensed\";")
        self.log_off_button_profil.setAlignment(QtCore.Qt.AlignCenter)
        self.log_off_button_profil.setObjectName("log_off_button_profil")
        self.change_account_button_profil = QtWidgets.QLabel(self.box_settings)
        self.change_account_button_profil.setGeometry(QtCore.QRect(10, 140, 151, 31))
        self.change_account_button_profil.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"font: 16pt \"Bahnschrift SemiLight Condensed\";")
        self.change_account_button_profil.setAlignment(QtCore.Qt.AlignCenter)
        self.change_account_button_profil.setObjectName("change_account_button_profil")
        self.pushbutton_hide_window1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushbutton_hide_window1.setGeometry(QtCore.QRect(0, 290, 1281, 431))
        self.pushbutton_hide_window1.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border: none;")
        self.pushbutton_hide_window1.setText("")
        self.pushbutton_hide_window1.setObjectName("pushButton_2")
        self.pushbutton_hide_window2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushbutton_hide_window2.setGeometry(QtCore.QRect(0, 70, 1131, 291))
        self.pushbutton_hide_window2.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border: none;")
        self.pushbutton_hide_window2.setText("")
        self.pushbutton_hide_window2.setObjectName("pushButton_3")
        self.pushbutton_hide_window1.setVisible(False)
        self.pushbutton_hide_window2.setVisible(False)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(160, 60, 960, 661))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.raise_()
        self.fon_subscriptions.raise_()
        self.box_top_selection.raise_()
        self.box_settings.raise_()
        self.box_tape_slection.raise_()
        self.pushbutton_hide_window1.raise_()
        self.pushbutton_hide_window2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.function_wallcast()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton_tape.setText(_translate("MainWindow", "Лента"))
        self.pushButton_subscriptions.setText(_translate("MainWindow", "Подписки"))
        self.pushButton_messages.setText(_translate("MainWindow", "Сообщения"))
        self.filters_subscriptions.setText(_translate("MainWindow", "Фильтры"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Поиск"))
        self.window_subscriptions_box_timesum.setText(_translate("MainWindow", "  Время:\n"
                                                                                   "  Стоимость:"))
        self.pushButton_tape_2.setText(_translate("MainWindow", "Глобальная лента"))
        self.pushButton_tape_3.setText(_translate("MainWindow", "Лента подписок"))
        self.nickname.setText(_translate("MainWindow", "Q1rD"))
        self.support_button_profil.setText(_translate("MainWindow", "Поддержка"))
        self.settings_button_profil.setText(_translate("MainWindow", "Настройки"))
        self.log_off_button_profil.setText(_translate("MainWindow", "Выйти"))
        self.change_account_button_profil.setText(_translate("MainWindow", "Сменить аккаунт"))


    '''Все функции кнопок'''
    def function_wallcast(self):    #отслеживание нажатия на кнопки
        self.pushButton_tape.clicked.connect(self.wallcast_tape_button_click)
        self.pushButton_profil.clicked.connect(self.wallcast_profil_top_button_click)
        self.pushButton_subscriptions.clicked.connect(self.wallcast_subscriptions_button_click)
        self.pushButton_messages.clicked.connect(self.wallcast_messages_button_click)
        self.pushbutton_hide_window1.clicked.connect(self.hide_window_after_clicked)
        self.pushbutton_hide_window2.clicked.connect(self.hide_window_after_clicked)


    def wallcast_tape_button_click(self):    #При нажатии на кнопку 'Лента' происходит
        self.box_tape_slection.setVisible(True)
        self.pushButton_tape_2.clicked.connect(self.wallcast_tape_2_button_click)
    def wallcast_profil_top_button_click(self):    #При нажатии на кнопку 'Профиль' происходит
        self.box_settings.setVisible(True)
        self.pushbutton_hide_window1.setVisible(True)
        self.pushbutton_hide_window2.setVisible(True)
    def wallcast_tape_2_button_click(self):    #При нажатии на кнопку 'Глобальная лента' происходит
        self.fon_subscriptions.setVisible(True)
        self.box_tape_slection.setVisible(False)
    def wallcast_subscriptions_button_click(self):    #При нажатии на кнопку 'Подписки' происходит
        self.fon_subscriptions.setVisible(False)
    def wallcast_messages_button_click(self):    #При нажатии на кнопку 'Сообщения' происходит
        self.fon_subscriptions.setVisible(False)
    def hide_window_after_clicked(self):    #Скрывает окно профиля при нажатии в любое место на экране
        self.box_settings.setVisible(False)
        self.pushbutton_hide_window1.setVisible(False)
        self.pushbutton_hide_window2.setVisible(False)


'''Запуск программы'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
