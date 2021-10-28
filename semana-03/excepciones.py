def llenar():
    n = 3
    i = 0
    while i < n :
        lista.append(input("Ingrese número "))
        i = i + 1

def mostrar_elemento():    
    try:
        pos = int(input("Ingrese posición a mostrar: "))
        print(lista[pos])
    except ValueError:
        print("No ingresó un valor correcto")
    except IndexError:
        print("La posición ingresada no existe")
    except:
        print("Ocurrió un error")

lista = []
llenar()
mostrar_elemento()


# Crear un paquete con el nombre traductor
# dicho paquete debe contener 3 módulos: p.e. espaniol.py, english.py o portugues.py
# cada módulo debe tener definido una función saludar() que retornará el saludo en dicho idioma.
# crear un script (fuera del paquete) que permita trabajar con el paquete
# El script debe pedir ingresar en qué idioma saludar
# dependiendo del idioma ingresado el programa saludará en dicho idioma

# espaniol.py
# Para saludar en español debe ingresar ES
# def saludar():
#    print("Hola, ¿cómo estas?")

# english.py
# Para saludar en inglés debe ingresar EN
# def saludar():
#    print("Hello, how are you?")


# idioma = input("Ingrese idioma: ") # ES, EN, PO

# if (idioma == "ES")
#    traductor.espaniol.saludar()