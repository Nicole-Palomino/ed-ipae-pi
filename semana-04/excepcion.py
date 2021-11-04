def encriptar(val):
    numeros = ["1", "2", "3", "4", "5", "6"] 
    if val in numeros:
        return val
    return None


# val = input("Ingrese un valor: ")
# print("El valor ingresado es: ", val)

########################################
# if encriptar(val) != None:
    # print("El valor encriptado es: ", len(encriptar(val)))
# else:
    # print("No se logró encriptar")

########################################
lista = [1,2,3]
if len(lista) > 0 :
    print("Función pop de lista", lista.pop())


###### Excepción 1 #################
"""try:
    num = int(input("Ingrese un número: "))
    print("{} / {} = {}".format(num, 10, num/0))
    lista = [1, 2, 3, 4]
    print("Elemento 5: ", lista[5])
    print(str(num) + " / 10 " + " = " + str(num/10))
except IndexError:
    print("Índice no encontrado")
except ValueError:
    print("Error al ingresar el número")
except ZeroDivisionError:
    print("No se puede dividir entre 0")    
except:
    print("Ocurrió un error inesperado")
else:
    print("Se finalizo con exito")"""

###### Excepción 2 #################
while True:
    try:
        numero = float(input('Ingrese numero: '))
    except:
        print('Valor ingresado incorrecto') 
    else:
        break
    finally:
        print('Fin del programa')        




