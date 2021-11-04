### Concatenar cadenas
""" cad1 = "Bienvenido "
cad2 = "a Piura"
val = 10
print(cad1 + cad2)
print(cad1 +  cad2 + str(val))
print("{} {} {}".format(cad1, cad2, val)) """

### Replicado
""" cad = "hola"
cad2 = 10
print(cad2*cad)
print(cad*9) """

### chr() and ord()
""" print(ord("a"))
print(ord("A"))
print(chr(99)) """

### cadenas como listas
""" cadena = "Estructura de datos"
for i in range(len(cadena)):
    print(cadena[i], end = "") """

### Rebanadas
""" cadena = "Computadora" """
#0: c 1:o 
# parámetros por defecto son [:::]
# start (inclusivo, defecto en 0), end (exclusivo, defecto tamaño - 1), step (por defecto 1)
""" print(cadena[4:6]) #ut
print(cadena[5:]) #tadora
print(cadena[:5]) #compu
print(cadena[4:-2]) #utado
print(cadena[-7:7]) #omputa
print(cadena[1:7:2]) #opt
print(cadena[::3]) #opt """


### in
""" cad = "Hola mundo"
find = "ola"
print(cad not in find) """

### min() and max()
""" numeros = [6,3,5]
cadena = "Holamundo"
print(min(numeros))
print(min(cadena))
print(max(numeros))
print(max(cadena)) """

### find()
""" cadena = "Bienvenidos a Piura"
find = "Piura"
print(cadena.find(find)) """

### upper() lower()
""" cadena = "Hola Mundo"
print(cadena.upper())
print(cadena.lower()) """

### Comparación de cadenas
cad1 = "hola"
cad2 = "Hola"
print(cad1 == cad2)
print(cad1 != cad2)
print("10" < "@10")