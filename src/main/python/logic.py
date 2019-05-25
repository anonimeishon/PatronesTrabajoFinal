#Clase Singleton
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

#Clase para guardar preguntas individuales por medio de la funcion conv
class Pregunta:
    def __init__(self, enunciado, A, B, C, D, correcta):
        self.enunciado = enunciado
        self.A = A      
        self.B = B
        self.C = C
        self.D = D
        self.correcta = correcta

    def verificar(self, whatever):
        pass
        
#Clase para guardar preguntas leidas de archivo.txt (Usa patron singleton)
class DB(metaclass = Singleton): 
    def __init__(self, lista):
        self.vec = lista

#Convierte preguntas en una lista a preguntas individuales (1 objeto por pregunta)
def conv(vec):
    vector=[]
    for line in vec:
        row = line.split(',')
        enunciado, A, B, C, D, correcta  = [i.strip() for i in row]
        vector.append(Pregunta(enunciado,A,B,C,D,correcta))
    return (vector)

#Lee un archivo txt y lo copia a uns lista
def ftoq():
    fh = open("preguntas.txt", "r")
    lines = fh.read().splitlines()
    fh.close()
    return lines


def play(preguntas):
    '''
    Q = 5
    show question object
    input answer
    verify if T or F
    next question
    Q-1
    '''
    pass

def maingui():
    lines=ftoq()
    Database = DB(lines)
    preguntas = conv(Database.vec)
    return preguntas

if __name__ == '__main__':
    lines=ftoq()
    Database = DB(lines)
    preguntas = conv(Database.vec)
    print (preguntas)

