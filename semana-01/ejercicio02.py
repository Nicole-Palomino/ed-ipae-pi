# Se tiene que ingresar 3 números, y de ellos debe imprimir cuál es el mayor
# p.e. 5 6 3, me debe imprimir 6

def buscar_mayor(a,b,c):
    mayor = None
    if a>b:
        if a>c:
            mayor = a
        else:
            mayor = c
    else:
        if b > c:
            mayor = b
        else:
            mayor = c
    return mayor

def leer_numero():
    number = int(input("Ingrese número: "))
    return number

a = leer_numero()
b = leer_numero()
c = leer_numero()
print("El mayor es: ", buscar_mayor(a, b, c))