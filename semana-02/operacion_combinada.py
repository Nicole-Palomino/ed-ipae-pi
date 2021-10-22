import calculadora
#resolver 3 + 5 * 10 = 53
def inicio():
    operar = input('Ingrese la operacion: ')
    lista = operar.split(maxsplit=5)
    
    try:
        if (lista[1] == '*'):
            val1 = calculadora.multiplicar(int(lista[0]), int(lista[2]))
            if (lista[3] == '+'):
                res = calculadora.imprimir('operacion', calculadora.sumar(val1, int(lista[4])))
                return res
            if (lista[3] == '-'):
                res1 = calculadora.imprimir('operacion', calculadora.restar(val1, int(lista[4])))
                return res1
            if (lista[3] == '/'):
                res2 = calculadora.imprimir('operacion', calculadora.dividir(val1, int(lista[4])))
                return res2
            if (lista[3] == '*'):
                go = calculadora.imprimir('operacion', calculadora.multiplicar(val1, int(lista[4])))
                return go   
        if (lista[1] == '/'):
            val2 = calculadora.dividir(int(lista[0]), int(lista[2])) 
            if (lista[3] == '+'):
                res3 = calculadora.imprimir('operacion', calculadora.sumar(val2, int(lista[4])))
                return res3
            if (lista[3] == '-'):
                res4 = calculadora.imprimir('operacion', calculadora.restar(val2, int(lista[4])))
                return res4
            if (lista[3] == '*'):
                res5 = calculadora.imprimir('operacion', calculadora.multiplicar(val2, int(lista[4])))
                return res5    
            if (lista[3] == '/'):
                go1 = calculadora.imprimir('operacion', calculadora.dividir(val2, int(lista[4]))) 
                return go1   
        


        for c in lista:
            if (c == '*' and c == lista[3]):
                val3 = calculadora.multiplicar(int(lista[2]), int(lista[4]))
                if (lista[1] == '+'):
                    res6 = calculadora.imprimir('operacion', calculadora.sumar(val3, int(lista[0])))
                    return res6 
                if (lista[1] == '-'):
                    res7 = calculadora.imprimir('operacion', calculadora.restar(int(lista[0]), val3))
                    return res7
            if (c == '/' and c == lista[3]):
                val4 = calculadora.dividir(int(lista[2]), int(lista[4]))
                if (lista[1] == '+'):
                    res8 = calculadora.imprimir('operacion', calculadora.sumar(val4, int(lista[0])))
                    return res8  
                if (lista[1] == '-'):
                    res9 = calculadora.imprimir('operacion', calculadora.restar(int(lista[0]), val4 ))
                    return res9
            if (c == '+'):
                val5 = calculadora.sumar(int(lista[0]), int(lista[2]))         
                if (lista[3] == '-'):
                    res10 = calculadora.imprimir('operacion', calculadora.restar(val5, int(lista[4])))
                    return res10
                if (lista[3] == '+'):
                    go2 = calculadora.imprimir('operacion', calculadora.sumar(val5, int(lista[4]))) 
                    return go2   
            if (c == '-'):
                val6 = calculadora.restar(int(lista[0]), int(lista[2]))         
                if (lista[3] == '+'):
                    res11 = calculadora.imprimir('operacion', calculadora.sumar(int(lista[4]), val6))
                    return res11  
                if (lista[3] == '-'):
                    go3 = calculadora.imprimir('operacion', calculadora.restar(val6, int(lista[4])))
                    return go3          
    except IndexError:  
        print('***Se debe ingresar como el ejemplo: 9 * 2 + 2***')
        print('')
        inicio()

inicio()   
    