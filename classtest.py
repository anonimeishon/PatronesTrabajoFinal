import sys
import Main
from PyQt5 import QtCore, QtWidgets, QtGui                                                                                                                                                                                                                                        


class MyWidget(QtWidgets.QWidget):
    def __init__(self, preguntas):
        QtWidgets.QWidget.__init__(self)
        self.buttonA = QtWidgets.QPushButton("Click me!")
        self.buttonB = QtWidgets.QPushButton("Click me!")
        self.buttonC = QtWidgets.QPushButton("Click me!")
        self.buttonD = QtWidgets.QPushButton("Click me!")


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    preguntas = Main.maingui()
    widget = MyWidget(preguntas)
    widget.show()
    sys.exit(app.exec_())

