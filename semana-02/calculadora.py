def fib(n):
    a, b = 0, 1
    while b < n:
        print(b, end=" ")
        a, b = b, a + b
    print()

def sumar(a, b):
    return a + b 

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b   

def imprimir(operacion, resultado):
    print('La %s es: %d'% (operacion, resultado))

