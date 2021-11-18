# Ana es palíndromo
# ¿Rosa es palíndromo?
from estructuras import Pila

palabra = input("Ingrese palabra: ")
pila1 = Pila.Pila()

# for i in range(len(palabra)):
#     pila1.push(palabra[i])

for letra in palabra:
    pila1.push(letra)

cont = 0
for letra in palabra:
    letra_aux = pila1.pop()
    if letra == letra_aux:
        cont += 1

if cont == len(palabra):
    print("Sí es palíndromo")
else:
    print("No es palíndromo")

# print(pila1.items)