numeros=[]
x=int(input('Cuántos números desea ingresar? '))
if (x >= 10):
    print('**Ingrese los',x, 'números**')
    for n in range(x):
        num=int(input('Ingrese un número: '))
        numeros.append(num)
    print(numeros)
    ordenados = sorted(numeros)
    print('La lista ordenada: ',ordenados)
else:
    print('Mínimo se deben ingresar 10 números')    