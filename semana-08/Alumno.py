from Persona import Persona


class Alumno(Persona):
    def __init__(self) -> None:
        super().__init__()
        self.grado = input('Ingrese grado: ')

    def imprimir(self) -> None:
        super().imprimir()
        print('Grado: ', self.grado)    