class Persona:
    
    def __init__(self) -> None:
        self.nombre = input("Ingrese nombre: ")
        self.edad = int(input("Ingrese edad: "))
        self.estado_civil = input("Ingrese estado civil (S|C|V|D): ")

    def es_mayor_edad(self) -> bool:
        # if self.edad >= 18:
        #     return True
        # else:
        #     return False
        # Un return corta el programa para devolver un valor
        # if self.edad >= 18:
        #     return True
        # return False
        return self.edad >= 18
    
    def imprimir_datos(self) -> None:
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)

    def imprimir_mayor_edad(self) -> None:
        if self.es_mayor_edad():
            print("Es mayor de edad")
        else:
            print("No es mayor de edad")

    # definir un método que indique si puede tramitar licencia de conducir
    # Una persona puede tramita una licencia si es mayor de edad o es casado y tiene 16 años
    def apto_licencia_conducir(self) -> None:
        if self.es_mayor_edad() or (self.edad == 16 and (self.estado_civil.upper() == 'C')):
            print("Puede tramitar la licencia de conducir")
        else:
            print("No Puede tramitar la licencia de conducir")