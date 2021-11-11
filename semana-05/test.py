# El identificador de clase es la palabra class 
# Es una clase vacía
class Alumno:
    pass # Se usa para definir una clase vacía

# Es una clase con atributos por defecto
class Persona:
    nombre = "Pedro"
    edad = 20
    sexo = "Masculino"

# Es una clase con un método de inicialización que permite iniciar atributos con valores diferentes
class Vehiculo:
    nro_ruedas = 4    

    def __init__(carro, marca, anio_fabricacion):
        carro.marca = marca
        carro.anio_fabricacion = anio_fabricacion
    
    def mostrar_datos(self):
        print("Es un vehículo de la marca {}, con año de fabricación {}, número de ruedas {}".format(self.marca, self.anio_fabricacion, self.nro_ruedas))

# Crear un objeto de la clase persona - instanciar
pedro = "Es un persona"
juan = Persona()

print(pedro)
print("Nombre: {}, edad: {}, sexo: {}".format(juan.nombre, juan.edad, juan.sexo))

# Creación de 2 objetos de la clase vehículo
veh1 = Vehiculo("Toyota", 2010)
veh2 = Vehiculo("Kia", 2019)
veh3 = Vehiculo("Honda", 2020)
marca = input("Ingrese Marca del vehículo: ")
anio_fab = input("Ingrese Año de fabricación del vehículo: ")
veh4 = Vehiculo(marca, anio_fab)
veh4.nro_ruedas = 2

# Se está invocando el método mostrar_datos() de los vehículos creados
veh1.mostrar_datos()
veh2.mostrar_datos()
veh3.mostrar_datos()
veh4.mostrar_datos()