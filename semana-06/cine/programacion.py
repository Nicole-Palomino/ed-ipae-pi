from clases.sala import Sala
from clases.espectador import Espectador

cant_salas = int(input("Ingrese cantidad de salas a programar: "))
salas = []

for i in range(cant_salas):
    print("Ingrese datos de sala ", (i+1))
    salas.append(Sala())

for sala in salas:
    print("********* Datos de la sala *********")
    sala.mostrar_datos()

# Ingreso de espectadores
print("Primer espectador")
esp1 = Espectador()
salas[0].ingresar_espectador(esp1)
print("Segundo espectador")
esp2 = Espectador()
salas[0].ingresar_espectador(esp2)

salas[0].listar_espectadores()