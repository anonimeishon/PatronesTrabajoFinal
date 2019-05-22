class Pregunta:
    def __init__(self, enunciado, A, B, C, D, correcta):
        self.enunciado = enunciado
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.correcta = correcta



if __name__ == '__main__':
    fh = open("preguntas.txt", "r").readlines()
    vector = []

for line in fh:
    row = line.split(',')
    print (row)
    enunciado, A, B, C, D, correcta  = [i.strip() for i in row]
    vector.append(Pregunta(enunciado,A,B,C,D,correcta))