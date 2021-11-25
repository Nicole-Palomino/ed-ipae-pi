from pila import Pila

n = int(input('¿Cuántos contenedores desea apilar? \n> '))

pila1 = Pila()

print('Ingrese ',n,'identificadores para los contenedor')
for i in range(n):
    id = input('Coloque el identificador {}: '.format(i+1))
    pila1.pilai.append(id)
print('Su pila inicial es: ', pila1.pilai)
print()

contenedor = input('Ingrese el identificador del contenedor a retirar: ')
temp = 0

print('El contenedor a retirar es el: ',contenedor)
input('Presione ENTER para efectuar el retiro ... ')
print('')

while(temp != contenedor):
    temp = pila1.pop()
    print(pila1.pilai) #va almacenando en temporal los numeros hasta llegar al numero a sacar
    if (temp != contenedor):
        pila1.pilaTemporal.append(temp)

print('**El contenedor a sido retirado**')
input('Presione ENTER para observar los números almacenados en la pila temporal ... ')
print('Pila temporal: ', pila1.pilaTemporal) #pilatemporal 
print()

while(pila1.pilaTemporal):
    pila1.pilai.append(pila1.pilaTemporal.pop())
input('Presione ENTER para regresar los números almacenados en la pila temporal ... ')    
print(pila1.pilai)
print()
print('***El programa se ha ejecutado correctamente***')