def imprimir(nombre):
    print("Hola, bienvenido " + nombre)

def leer_nombre():
    name = input("Ingrese su nombre: ")
    return name

nombre = leer_nombre()
imprimir(nombre)