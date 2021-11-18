lista = []

def push(element):
    lista.append(element)

def pop():
    valor = lista[-1]
    del lista[-1]
    return valor