from matematica import geometria
from matematica import calculadora

lado = int(input('Ingresar lado del cuadrado: '))
print('El perimetro del cuadrado de lado {} es {}'.format(lado, geometria.perimetro_cuadrado(lado)))

num1 = int(input('Ingrese un valor: '))
num2 = int(input('Ingrese otro valor: '))
print('La suma de los numeros es: ', calculadora.sumar(num1, num2))

