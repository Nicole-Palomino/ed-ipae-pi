import pila

#preguntar cuantos contenedores desea apilar
n = int(input('¿Cuántos contenedores desea apilar? \n> '))

#colocar el identificador 
print('Ingrese ',n,'identificadores para los contenedor')
for i in range(n):
    id = input('Coloque el identificador: ')
    pila.push(id)
print('Su pila inicial es: ', pila.pilai)
print()

#eliminar un contenedor en especifico
contenedor = input('Ingrese el identificador del contenedor a retirar: ')
temp = 0

print('El contenedor a retirar es el: ',contenedor)
input('Presione ENTER para efectuar el retiro ... ')
print('')

while(temp != contenedor):
    temp = pila.pop()
    print(pila.pilai) #va almacenando en temporal los numeros hasta llegar al numero a sacar
    if (temp != contenedor):
        pila.pilaTemporal.append(temp)

print('**El contenedor a sido retirado**')
input('Presione ENTER para observar los números almacenados en la pila temporal ... ')
print('Pila temporal: ', pila.pilaTemporal) #pilatemporal 
print()

while(pila.pilaTemporal):
    pila.pilai.append(pila.pilaTemporal.pop())
input('Presione ENTER para regresar los números almacenados en la pila temporal ... ')    
print(pila.pilai)
print()
print('***El programa se ha ejecutado correctamente***')