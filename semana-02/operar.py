import calculadora

calculadora.imprimir('suma', calculadora.sumar(20, 4))
calculadora.imprimir('resta', calculadora.restar(20, 4))
calculadora.imprimir('multiplicación', calculadora.multiplicar(20, 4))
calculadora.imprimir('división', calculadora.dividir(20, 4))

#resolver (3+5)*10

val1 = calculadora.sumar(3, 5)
calculadora.imprimir('operacion', calculadora.multiplicar(val1, 10))