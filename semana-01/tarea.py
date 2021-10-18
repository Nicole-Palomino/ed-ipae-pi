numeros=[]

def ordenar():
    ordenado = sorted(numeros)
    print('La lista ordenada: ',ordenado)

x=int(input('Cuántos números desea ingresar? '))

if (x >= 10):
    print('**Ingrese los',x, 'números**')
    for n in range(x):
        num=int(input('Ingrese un número: '))
        numeros.append(num)
    print(numeros)
    ordenar()
else:
    print('Mínimo se deben ingresar 10 números') 