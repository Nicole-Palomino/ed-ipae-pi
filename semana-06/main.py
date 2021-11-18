# Pilas es una lista
# lista es un arreglo
# método
# lista = []
# lista.append("Piura") # agregar un elemento
# lista.append("Sullana")
# lista.append("Talara")
# lista.append("Ayabaca")
# lista.append("Paita")
# print(lista)
# print("La lista tiene {} elementos".format(len(lista))) # tamaño de la lista
# lista.pop() # remueve el último elemento
# print("Se eliminió el último elemento de la lista. Lista actual: ", lista)
# ciudad = input("Ingrese ciudad a buscar: ")
# print("La ciudad {} se encuentra en la posición {}".format(ciudad, lista.index(ciudad)))
# lista.remove(ciudad)
# print("Se procede a eliminar {} de la lista. Lista actualizada: {}".format(ciudad, lista))

# atajo para comentar varias líneas ctrl + k + c

# PILAS
# LIFO: Last-In, First-out
# Pila de moneda
# import Pila
# # Apilamiento de monedas
# Pila.push("S/ 5")
# Pila.push("S/ 2")
# Pila.push("S/ 1")
# print(Pila.lista)
# print(Pila.pop())

# Otra forma
# monedas = Pila()
# monedas.push("S/ 5.00")
# monedas.push("S/ 1.00")
# monedas.push("S/ 2.00")
# monedas.push("S/ 2.00")
# monedas.push("S/ 0.50")

# print(monedas.pop())
# print(monedas.pop())

# print(monedas.items)

from estructuras import Pila

monedas = Pila.Pila()
monedas.push("5")
monedas.push("3")
monedas.push("2")

print(monedas.items)