import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout, QGraphicsScene, QGraphicsView, \
    QGraphicsBlurEffect
from wallcast_functions import *


class Ui_MainWindow(QMainWindow, object):
    def __init__(self):
        super().__init__()
        self.password = None

        self.title = "Эффекты"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 400

        self.setWindowTitle(self.title)
        # Задание местоположения и размера окна
        self.setGeometry(self.left, self.top, self.width, self.height)
        # Создание графической сцены
        self.scene = QGraphicsScene()
        # Создание инструмента для отрисовки графической сцены
        self.graphicView = QGraphicsView(self.scene, self)
        # Задание местоположения и размера графической сцены
        self.graphicView.setGeometry(0, 0, self.width, self.height)


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 720))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 720))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setWindowTitle("WallCast")
        icon = QtGui.QIcon(logo_wallcast)
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
        self.label_logo.setPixmap(QtGui.QPixmap(logo_wallcast))
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
        icon.addPixmap(QtGui.QPixmap(ava_wallcast), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_profil.setIcon(icon)
        self.pushButton_profil.setIconSize(QtCore.QSize(77, 54))
        self.pushButton_profil.setAutoRepeat(False)
        self.pushButton_profil.setObjectName("pushButton_profil")
        self.notifications_pushbutton = QtWidgets.QPushButton(self.box_top_selection)
        self.notifications_pushbutton.setGeometry(QtCore.QRect(1160, 16, 41, 41))
        self.notifications_pushbutton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"border-color: beige;\n"
"font: bold 16px;\n"
"padding: 6px;")
        self.notifications_pushbutton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(kolokol_wallcast), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.notifications_pushbutton.setIcon(icon1)
        self.notifications_pushbutton.setIconSize(QtCore.QSize(28, 28))
        self.notifications_pushbutton.setObjectName("pushButton")
        self.label_logo.raise_()
        self.pushButton_subscriptions.raise_()
        self.pushButton_messages.raise_()
        self.pushButton_profil.raise_()
        self.pushButton_tape.raise_()
        self.notifications_pushbutton.raise_()
        self.fon_subscriptions = QtWidgets.QFrame(self.centralwidget)
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
        self.window_subscriptions_box_ava.setPixmap(QtGui.QPixmap(logo_wallcast))
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
        self.box_notifications = QtWidgets.QFrame(self.centralwidget)
        self.box_notifications.setGeometry(QtCore.QRect(990, 70, 291, 271))
        self.box_notifications.setMouseTracking(False)
        self.box_notifications.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                             "border-bottom-left-radius: 20px;")
        self.box_notifications.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.box_notifications.setFrameShadow(QtWidgets.QFrame.Raised)
        self.box_notifications.setObjectName("box_notifications")
        self.box_notifications.setVisible(False)
        self.box_notifications_ava = QtWidgets.QPushButton(self.box_notifications)
        self.box_notifications_ava.setGeometry(QtCore.QRect(25, 17, 51, 51))
        self.box_notifications_ava.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: beige;\n"
"font: bold 16px;\n"
"padding: 6px;\n"
"border-bottom-left-radius: 0px;")
        self.box_notifications_ava.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(ava_kivalex),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.box_notifications_ava.setIcon(icon3)
        self.box_notifications_ava.setIconSize(QtCore.QSize(51, 51))
        self.box_notifications_ava.setObjectName("box_notifications_ava")
        self.box_notifications_name1 = QtWidgets.QPushButton(self.box_notifications)
        self.box_notifications_name1.setGeometry(QtCore.QRect(10, 70, 81, 23))
        self.box_notifications_name1.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-bottom-left-radius: 0px;\n"
"font: bold 0px;")
        self.box_notifications_name1.setObjectName("pushButton_4")
        self.textEdit = QtWidgets.QTextEdit(self.box_notifications)
        self.textEdit.setGeometry(QtCore.QRect(90, 2, 181, 81))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-bottom-left-radius: 0px;")
        self.textEdit.setObjectName("textEdit")
        self.pushbutton_box_notifications_gotopodcast = QtWidgets.QPushButton(self.box_notifications)
        self.pushbutton_box_notifications_gotopodcast.setGeometry(QtCore.QRect(90, 90, 181, 23))
        self.pushbutton_box_notifications_gotopodcast.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-bottom-left-radius: 0px;")
        self.pushbutton_box_notifications_gotopodcast.setObjectName("pushButton_5")
        self.box_notifications_ava_2 = QtWidgets.QPushButton(self.box_notifications)
        self.box_notifications_ava_2.setGeometry(QtCore.QRect(25, 137, 51, 51))
        self.box_notifications_ava_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: beige;\n"
"font: bold 16px;\n"
"padding: 6px;\n"
"border-bottom-left-radius: 0px;")
        self.box_notifications_ava_2.setText("")
        self.box_notifications_ava_2.setIcon(icon3)
        self.box_notifications_ava_2.setIconSize(QtCore.QSize(51, 51))
        self.box_notifications_ava_2.setObjectName("box_notifications_ava_2")
        self.pushbutton_box_notifications_gotopodcast2 = QtWidgets.QPushButton(self.box_notifications)
        self.pushbutton_box_notifications_gotopodcast2.setGeometry(QtCore.QRect(90, 210, 181, 23))
        self.pushbutton_box_notifications_gotopodcast2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-bottom-left-radius: 0px;")
        self.pushbutton_box_notifications_gotopodcast2.setObjectName("pushButton_6")
        self.textEdit_2 = QtWidgets.QTextEdit(self.box_notifications)
        self.textEdit_2.setGeometry(QtCore.QRect(90, 122, 181, 81))
        self.textEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-bottom-left-radius: 0px;")
        self.textEdit_2.setObjectName("textEdit_2")
        self.box_notifications_name2 = QtWidgets.QPushButton(self.box_notifications)
        self.box_notifications_name2.setGeometry(QtCore.QRect(10, 190, 81, 23))
        self.box_notifications_name2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-bottom-left-radius: 0px;\n"
"font: bold 0px;")
        self.box_notifications_name2.setObjectName("pushButton_8")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(160, 60, 960, 661))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.register_login = QtWidgets.QFrame(self.centralwidget)
        self.register_login.setGeometry(QtCore.QRect(360, 140, 561, 481))
        self.register_login.setStyleSheet("background-color: rgb(158, 151, 182);")
        self.register_login.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.register_login.setFrameShadow(QtWidgets.QFrame.Raised)
        self.register_login.setObjectName("register_login")
        self.label_regLog = QtWidgets.QLabel(self.register_login)
        self.label_regLog.setGeometry(QtCore.QRect(0, 20, 561, 91))
        self.label_regLog.setStyleSheet("font: 28pt \"Bahnschrift SemiLight Condensed\";")
        self.label_regLog.setAlignment(QtCore.Qt.AlignCenter)
        self.label_regLog.setObjectName("label_regLog")
        self.username_register = QtWidgets.QLineEdit(self.register_login)
        self.username_register.setGeometry(QtCore.QRect(70, 130, 361, 41))
        self.username_register.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                             "border-radius: 14px;\n"
                                             "font: 18pt \"Bahnschrift SemiLight Condensed\";\n"
                                             "border: 3px solid green;")
        self.username_register.setInputMask("")
        self.username_register.setText("")
        self.username_register.setMaxLength(32767)
        self.username_register.setObjectName("username_register")
        self.password_register = QtWidgets.QLineEdit(self.register_login)
        self.password_register.setGeometry(QtCore.QRect(70, 190, 361, 41))
        self.password_register.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                             "border-radius: 14px;\n"
                                             "font: 18pt \"Bahnschrift SemiLight Condensed\";\n"
                                             "border: 3px solid red;")
        self.password_register.setInputMask("")
        self.password_register.setText("")
        self.password_register.setMaxLength(32767)
        self.password_register.setObjectName("password_register")
        self.further_register = QtWidgets.QPushButton(self.register_login)
        self.further_register.setGeometry(QtCore.QRect(380, 240, 111, 41))
        self.further_register.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "font: 20pt \"Bahnschrift SemiLight Condensed\";\n"
                                            "border-style: outset;\n"
                                            "border-width: 2px;\n"
                                            "border-radius: 14px;\n"
                                            "border-color: beige;\n"
                                            "font: bold 28px;\n"
                                            "padding: 2px;")
        self.further_register.setObjectName("further_register")
        self.label_2 = QtWidgets.QLabel(self.register_login)
        self.label_2.setGeometry(QtCore.QRect(80, 400, 401, 41))
        self.label_2.setStyleSheet("font: 18pt \"Bahnschrift SemiLight Condensed\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.login_registerWin = QtWidgets.QPushButton(self.register_login)
        self.login_registerWin.setGeometry(QtCore.QRect(180, 430, 191, 31))
        self.login_registerWin.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                             "font: 20pt \"Bahnschrift SemiLight Condensed\";\n"
                                             "color: rgb(0, 102, 0);")
        self.login_registerWin.setObjectName("login_registerWin")
        self.label_3 = QtWidgets.QLabel(self.register_login)
        self.label_3.setGeometry(QtCore.QRect(70, 240, 221, 41))
        self.label_3.setStyleSheet("font: 16pt \"Bahnschrift SemiLight Condensed\";")
        self.label_3.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.register_login)
        self.label_4.setGeometry(QtCore.QRect(70, 290, 421, 101))
        self.label_4.setStyleSheet("font: 16pt \"Bahnschrift SemiLight Condensed\";")
        self.label_4.setObjectName("label_4")
        self.show_password_register = QtWidgets.QPushButton(self.register_login)
        self.show_password_register.setGeometry(QtCore.QRect(450, 190, 41, 41))
        self.show_password_register.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                      "border-radius: 14px;")
        self.show_password_register.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(open_eye), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.show_password_register.setIcon(icon4)
        self.show_password_register.setIconSize(QtCore.QSize(43, 43))
        self.show_password_register.setObjectName("showhide_password_register")
        self.hide_password_register = QtWidgets.QPushButton(self.register_login)
        self.hide_password_register.setGeometry(QtCore.QRect(450, 190, 41, 41))
        self.hide_password_register.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                      "border-radius: 14px;")
        self.hide_password_register.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(closed_eye), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.hide_password_register.setIcon(icon5)
        self.hide_password_register.setIconSize(QtCore.QSize(43, 43))
        self.hide_password_register.setObjectName("showhide_password_register")
        self.incorrect_data_for_registration = QtWidgets.QLabel(self.register_login)
        self.incorrect_data_for_registration.setGeometry(QtCore.QRect(160, 226, 201, 31))
        self.incorrect_data_for_registration.setStyleSheet("color: red;\n"
                                 "font: 13pt \"Bahnschrift SemiLight Condensed\";\n"
                                 "background-color: rgb(255, 255, 255, 0)")
        self.incorrect_data_for_registration.setAlignment(QtCore.Qt.AlignCenter)
        self.incorrect_data_for_registration.setObjectName("label")
        self.incorrect_data_for_registration.setVisible(False)
        self.frame.raise_()
        self.fon_subscriptions.raise_()
        self.box_top_selection.raise_()
        self.box_settings.raise_()
        self.box_tape_slection.raise_()
        self.pushbutton_hide_window1.raise_()
        self.pushbutton_hide_window2.raise_()
        self.box_notifications.raise_()
        self.register_login.raise_()
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
        self.box_notifications_name1.setText(_translate("MainWindow", "Kivalex"))
        self.textEdit.setHtml(_translate("MainWindow",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Название:</p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Тема:</p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Описание: шцуипшгзгуиывтолитвылфмлдьцфшурпуццуппцупуцпуупцупцупц</p></body></html>"))
        self.pushbutton_box_notifications_gotopodcast.setText(_translate("MainWindow", "Перейти на подкаст"))
        self.pushbutton_box_notifications_gotopodcast2.setText(_translate("MainWindow", "Перейти на подкаст"))
        self.textEdit_2.setHtml(_translate("MainWindow",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Название:</p>\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Тема:</p>\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Описание: шцуипшгзгуиывтолитвылфмлдьцфшурпуццуппцупуцпуупцупцупц</p></body></html>"))
        self.box_notifications_name2.setText(_translate("MainWindow", "kr7a-J"))
        self.label_regLog.setText(_translate("MainWindow", "Зарегестрируйте аккаунт"))
        self.username_register.setPlaceholderText(_translate("MainWindow", "Имя пользователя"))
        self.password_register.setPlaceholderText(_translate("MainWindow", "Пароль"))
        self.further_register.setText(_translate("MainWindow", "Далее"))
        self.label_2.setText(_translate("MainWindow", "Уже есть аккаунт?"))
        self.login_registerWin.setText(_translate("MainWindow", "войти"))
        self.label_3.setText(_translate("MainWindow", "Пароль должен:"))
        self.label_4.setText(_translate("MainWindow", "<p>Состоять из букв латинского алфавита (A-z)<br>\n"
                                                      "Длина пароля должна быть от 6 до 18 символов<br>\n"
                                                      "Минимум 2 специальных знака(!@#^*)<br>\n"
                                                      "Состоять из строчных и прописных букв</p>"))
        self.incorrect_data_for_registration.setText(_translate("MainWindow", "Вы ввели данные не правильно!"))

    '''Все функции кнопок и тп'''
    def function_wallcast(self):
        '''Функции всех кнопок'''
        self.pushButton_tape.clicked.connect(self.wallcast_tape_button_click)
        self.pushButton_profil.clicked.connect(self.wallcast_profil_top_button_click)
        self.pushButton_subscriptions.clicked.connect(self.wallcast_subscriptions_button_click)
        self.pushButton_messages.clicked.connect(self.wallcast_messages_button_click)
        self.pushbutton_hide_window1.clicked.connect(self.wallcast_hide_window_after_click)
        self.pushbutton_hide_window2.clicked.connect(self.wallcast_hide_window_after_click)
        self.notifications_pushbutton.clicked.connect(self.wallcast_notification_button_click)
        self.pushButton_tape_2.clicked.connect(self.wallcast_tape_2_button_click)
        self.show_password_register.clicked.connect(self.wallcast_show_password)
        self.hide_password_register.clicked.connect(self.wallcast_hide_password)
        self.further_register.clicked.connect(self.wallcast_further_register_clicked)
        '''Функции текстовых значений'''
        self.password_register.textEdited.connect(self.wallcast_password_check)

    def wallcast_tape_button_click(self):    #При нажатии на кнопку 'Лента' происходит
        self.box_tape_slection.setVisible(True)
        self.box_tape_slection.raise_()
        self.pushbutton_hide_window1.setVisible(True)
        self.pushbutton_hide_window2.setVisible(True)
    def wallcast_profil_top_button_click(self):    #При нажатии на кнопку 'Профиль' происходит
        self.box_settings.setVisible(True)
        self.pushbutton_hide_window1.setGeometry(QtCore.QRect(0, 290, 1281, 431))
        self.pushbutton_hide_window2.setGeometry(QtCore.QRect(0, 70, 1131, 291))
        self.pushbutton_hide_window1.setVisible(True)
        self.pushbutton_hide_window2.setVisible(True)
    def wallcast_tape_2_button_click(self):    #При нажатии на кнопку 'Глобальная лента' происходит
        self.fon_subscriptions.setVisible(True)
        self.box_tape_slection.setVisible(False)
    def wallcast_subscriptions_button_click(self):    #При нажатии на кнопку 'Подписки' происходит
        self.fon_subscriptions.setVisible(False)
    def wallcast_messages_button_click(self):    #При нажатии на кнопку 'Сообщения' происходит
        self.fon_subscriptions.setVisible(False)
    def wallcast_hide_window_after_click(self):    #Скрывает окна (профиль, уведомления, выбор ленты) при нажатии в любое место на экране
        self.box_settings.setVisible(False)
        self.box_notifications.setVisible(False)
        self.box_tape_slection.setVisible(False)
        self.pushbutton_hide_window1.setVisible(False)
        self.pushbutton_hide_window2.setVisible(False)
    def wallcast_notification_button_click(self):   #Закрытие окна при клике в любую точку
        self.box_notifications.setVisible(True)
        self.pushbutton_hide_window1.setVisible(True)
        self.pushbutton_hide_window2.setVisible(True)

    '''Регистрационное окно'''
    def wallcast_show_password(self):   #Показать пароль
        self.show_password_register.setVisible(False)
        self.hide_password_register.setVisible(True)
        self.password_register.setEchoMode(QLineEdit.Normal)
    def wallcast_hide_password(self):   #Скрыть пароль
        self.hide_password_register.setVisible(False)
        self.show_password_register.setVisible(True)
        self.password_register.setEchoMode(QLineEdit.Password)
    def wallcast_password_check(self, password):    #Проверка пароля
        if validate_password(password) == True:
            self.password_register.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                 "border-radius: 14px;\n"
                                                 "font: 18pt \"Bahnschrift SemiLight Condensed\";\n"
                                                 "border: 3px solid green;")
            self.password = password
        else:
            self.password_register.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                 "border-radius: 14px;\n"
                                                 "font: 18pt \"Bahnschrift SemiLight Condensed\";\n"
                                                 "border: 3px solid red;")
    def wallcast_further_register_clicked(self):    #Активация кнопки "Далее"
        print(self.password)
        if self.password != None:
            self.register_login.setVisible(False)
        else:
            self.incorrect_data_for_registration.setVisible(True)

'''Запуск программы'''
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
