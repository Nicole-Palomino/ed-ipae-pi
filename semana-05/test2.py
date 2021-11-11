# Ejemplo de clase animal
class Animal:

    def __init__(self) -> None:
        self.nombre = input("Ingrese nombre: ")
        self.grupo = input("Grupo: ")

    def desplazamiento(self) :
        if (self.grupo == 'Ave'):
            return "Se desplaza volando"
        elif self.grupo == 'Serpiente':
            return "Se desplaza arrastrando"
        else:
            return "Se deplaza caminando"

# perro = Animal()
# gato = Animal()
# boa = Animal()
# aguila = Animal()

# print("El {} {} ".format(perro.nombre, perro.desplazamiento()))
# print("El {} {} ".format(gato.nombre, gato.desplazamiento()))
# print("La {} {} ".format(boa.nombre, boa.desplazamiento()))
# print("La {} {} ".format(aguila.nombre, aguila.desplazamiento()))

# Crear una lista con 5 animales y de los animales ingresados hagan andar al primero y al último de la lista
animales = []
for i in range(3):
    animales.append(Animal())

print("El primer animal: ", animales[0].desplazamiento())
print("El último animal: ", animales[len(animales) - 1].desplazamiento())