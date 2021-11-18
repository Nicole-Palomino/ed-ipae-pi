from clases.espectador import Espectador

class Sala:

    nro_sala : int
    pelicula : str
    aforo : int
    espectadores = []

    def __init__(self) -> None:        
        self.nro_sala = int(input("Nro de Sala: "))
        self.pelicula = input("Nombre de la película: ")
        self.aforo = int(input("Aforo: "))
    
    def mostrar_datos(self) -> None:
        print("Nro de sala: ", self.nro_sala)
        print("Nombre de película: ", self.pelicula)
        print("Aforo: ", self.aforo)

    def ingresar_espectador(self, espectador: Espectador) -> None:
        self.espectadores.append(espectador)

    def listar_espectadores(self) -> None:
        for esp in self.espectadores:
            print("La sala {} tiene {}:".format(self.nro_sala, len(self.espectadores)))
            (Espectador)(esp).imprimir_datos()