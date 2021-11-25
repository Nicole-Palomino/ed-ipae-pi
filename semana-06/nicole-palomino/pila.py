#pilai = [] #contiene la pila de contenedores iniciales
#pilaTemporal = [] #contiene la pila temporalmente

class Pila:   

    def __init__(self) -> None:
        self.pilai = []
        self.pilaTemporal = []

    def push(self, element):
        self.pilai.append(element)

    def pop(self):
        valor = self.pilai[-1]
        del self.pilai[-1]
        return valor
