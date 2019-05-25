import sys
import Main
from PyQt5 import QtCore, QtWidgets, QtGui                                                                                                                                                                                                                                        


class MyWidget(QtWidgets.QWidget):
    def __init__(self, preguntas):
        QtWidgets.QWidget.__init__(self)
        self.text = QtWidgets.QLabel("Hello World")
        self.text.setAlignment(QtCore.Qt.AlignCenter)
        self.buttonA = QtWidgets.QPushButton("Click me!")
        self.buttonB = QtWidgets.QPushButton("Click me!")
        self.buttonC = QtWidgets.QPushButton("Click me!")
        self.buttonD = QtWidgets.QPushButton("Click me!")
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.buttonA)
        self.layout.addWidget(self.buttonB)
        self.layout.addWidget(self.buttonC)
        self.layout.addWidget(self.buttonD)
        self.options = ["A","B","C","D"]
        self.buttonA.clicked.connect(lambda: magic("A"))
        self.buttonB.clicked.connect(lambda: magic("B"))
        self.buttonC.clicked.connect(lambda: magic("C"))
        self.buttonD.clicked.connect(lambda: magic("D"))
        self.setLayout(self.layout)

def magic(Opt):
    opt = Opt
    alert= QtWidgets.QMessageBox()
    if opt == "A":
        alert.setText("That's right! +1 Point")
    else:
        alert.setText("Wrong!")



    def magic(self,Opt):
        opt = Opt
        alert= QtWidgets.QMessageBox()
        if opt == "A":
            alert.setText("That's right! +1 Point")
            self.layout.addWidget(alert)
            self.setLayout(self.layout)


        else:
            alert.setText("Wrong!")


            self.setLayout(self.layout)


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    preguntas = Main.maingui()
    widget = MyWidget(preguntas)
    widget.show()
    sys.exit(app.exec_())

