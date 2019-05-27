import Main
from PyQt5 import QtCore, QtWidgets, QtGui 

                                                                                                                                                                                                                                    
score=0
def questionwindow(app, preguntas):
    f = QtGui.QFont()
    f.setPointSize(14)
    global score 
    for i in range (len(preguntas)):
        window = QtWidgets.QWidget()
        app.setStyleSheet("QPushButton { margin: 1ex; }")

        layout = QtWidgets.QVBoxLayout()
        enunciado = QtWidgets.QLabel(preguntas[i].enunciado)
        enunciado.setFont(f)
        layout.addWidget(enunciado)
#################

        buttonA = QtWidgets.QPushButton(preguntas[i].A)
        buttonA.clicked.connect((lambda: magic("A",preguntas[i].correcta,window,f)))
        buttonA.setMinimumSize(100,50) 
        buttonA.setFont(f) 
        layout.addWidget(buttonA)

        buttonB = QtWidgets.QPushButton(preguntas[i].B)
        buttonB.clicked.connect((lambda: magic("B",preguntas[i].correcta,window,f)))
        buttonB.setMinimumSize(100,50)  
        buttonB.setFont(f) 
        layout.addWidget(buttonB)

        buttonC = QtWidgets.QPushButton(preguntas[i].C)
        buttonC.clicked.connect((lambda: magic("C",preguntas[i].correcta,window,f)))
        buttonC.setMinimumSize(100,50) 
        buttonC.setFont(f) 
        layout.addWidget(buttonC)

        buttonD = QtWidgets.QPushButton(preguntas[i].D)
        buttonD.clicked.connect((lambda: magic("D",preguntas[i].correcta,window,f)))
        buttonD.setMinimumSize(100,50) 
        buttonD.setFont(f) 
        layout.addWidget(buttonD)

##################
        window.setLayout(layout)
        window.show()
        app.exec_()
    sc= str(score)
    alert= QtWidgets.QMessageBox()
    alert.setFont(f) 
    alert.setWindowTitle("Score: ")
    alert.setText("Score: " + sc)
    alert.exec_()


def magic(opt,correcta,window,f):
    global score 
    alert= QtWidgets.QMessageBox()
    alert.setFont(f)
    if opt == correcta:
        alert.setText("That's right! +1 Point")
        score += 1
        print ("right")
    else:
        alert.setText("Wrong!")
        print ("wrong")
    alert.exec_()
    window.close()

if __name__ == '__main__':
    score = 0
    app = QtWidgets.QApplication([])
    app.setStyle('Fusion')
    preguntas = Main.maingui()
    questionwindow(app, preguntas)
