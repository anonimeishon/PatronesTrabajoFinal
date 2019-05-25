from PyQt5.QtWidgets import *
import Main

def questionwindow(app, preguntas):
    for i in range (len(preguntas)):
        window = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel(preguntas[i].enunciado))
        layout.addWidget(QPushButton(preguntas[i].A))
        layout.addWidget(QPushButton(preguntas[i].B))
        layout.addWidget(QPushButton(preguntas[i].C))
        layout.addWidget(QPushButton(preguntas[i].D))
        window.setLayout(layout)
        window.show()
        app.exec_()
    


if __name__ == '__main__':

    app = QApplication([])
    app.setStyle('Fusion')
    preguntas = Main.maingui()

    questionwindow(app, preguntas)
