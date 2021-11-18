class Espectador:

    nombre : str
    tipo : str

    def __init__(self) -> None:
        self.nombre = input("Ingrese su nombre: ")
        self.tipo = input("Indique el tipo de espectador: ")

    def imprimir_datos(self) -> None:
        print("Nombre: ", self.nombre)
        print("Tipo: ", self.tipo)