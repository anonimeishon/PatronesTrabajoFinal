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


def ftoq():
    vector = []
    fh = open("preguntas.txt", "r")
    lines = fh.read().splitlines()
    for line in lines:
        row = line.split(',')
        print (row)
        enunciado, A, B, C, D, correcta  = [i.strip() for i in row]
        vector.append(Pregunta(enunciado,A,B,C,D,correcta))
    fh.close()
    return (vector)

if __name__ == '__main__':
    print(ftoq())


    


