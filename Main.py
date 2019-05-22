class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]




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
        
class DB(metaclass = Singleton):
    def __init__(self, lista):
        self.vec = lista


def conv(vec):
    vector=[]
    for line in vec:
        row = line.split(',')
        print (row)
        enunciado, A, B, C, D, correcta  = [i.strip() for i in row]
        vector.append(Pregunta(enunciado,A,B,C,D,correcta))
    return (vector)


def ftoq():
    fh = open("preguntas.txt", "r")
    lines = fh.read().splitlines()
    fh.close()
    return lines



if __name__ == '__main__':
    lines=ftoq()
    Database = DB(lines)
    Database2 = DB(lines)
    assert Database is Database2
    print(Database)
    print(Database2)
    conv(Database.vec)
