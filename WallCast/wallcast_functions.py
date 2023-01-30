from PyQt5 import QtCore, QtGui, QtWidgets


def function_wallcast(self):
    self.pushButton_tape.clicked.connect(self.wallcast_tape_but_click)


def wallcast_tape_but_click(self):
    self.frame_2.setVisible(True)