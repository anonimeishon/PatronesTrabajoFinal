class Singleton(type):
    def __init__(self, *args):
        type.__init__(self, *args)
        self._instances = {}

    def __call__(self, *args):
        if not args in self._instances:
            self._instances[args] = type.__call__(self, *args)
        return self._instances[args]

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
        
class DB:
    __metaclass__= Singleton
    def __init__(self, vec):
        self.vec = vec
        
    def ide(self):
        print(id) 

    def conv(self,vec):
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
    DB(lines)
    fh.close()


if __name__ == '__main__':
    ftoq()



#    ta1, ta2 = Test, Test
#    assert ta1 is ta2
#    print (ta1.ide, ta2.ide)
