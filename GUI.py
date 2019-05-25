from PyQt5.QtWidgets import *
import Main
from PyQt5 import QtCore, QtWidgets, QtGui                                                                                                                                                                                                                                        


def questionwindow(app, preguntas):

    for i in range (len(preguntas)):
        window = QWidget()
        app.setStyleSheet("QPushButton { margin: 1ex; }")
        layout = QVBoxLayout()
        layout.addWidget(QLabel(preguntas[i].enunciado))
#################

        buttonA = QPushButton(preguntas[i].A)
        buttonA.clicked.connect(clickedbutton)
        layout.addWidget(buttonA)

        buttonB = QPushButton(preguntas[i].B)
        layout.addWidget(buttonB)

        buttonC = QPushButton(preguntas[i].C)
        layout.addWidget(buttonC)

        buttonD = QPushButton(preguntas[i].D)
        layout.addWidget(buttonD)

##################
        window.setLayout(layout)
        window.show()
        app.exec_()
    
def clickedbutton():

    alert= QMessageBox()
    if True:
        alert.setText("That's right! +1 Point")
        window.close()
    else:
        alert.setText("Wrong!")
        windows.close()

if __name__ == '__main__':

    app = QApplication([])
    app.setStyle('Fusion')
    preguntas = Main.maingui()

    questionwindow(app, preguntas)
