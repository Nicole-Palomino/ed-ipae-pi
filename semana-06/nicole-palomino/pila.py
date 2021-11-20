pilai = [] #contiene la pila de contenedores iniciales
pilaTemporal = [] #contiene la pila temporalmente

def push(element):
    pilai.append(element)

def pop():
    valor = pilai[-1]
    del pilai[-1]
    return valor