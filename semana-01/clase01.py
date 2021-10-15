# diccionario: Permite almacenar datos con llave - valor. No usa índices.
# diccionario = {}
# tuplas: Usan índices. No permite cambios.
# tupla = ()
# listas: Usan índices. Si permite cambios.
# lista = []

alumno = {"nombre": "Christian", "carrera": "Informática", "ciudad": "Piura"}
print(alumno["ciudad"])


abreviaturas = ("Sr.", "Dr.", "Ing.", "Sra.")
print(abreviaturas[1])

notas = [13, 16, 15]
notas[0] = 17
print(notas[0])

# Tarea: Usar una lista que permita ingresar número enteros. (mínimo permita ingresar 10 números)
# Luego crear una función que los ordene de manera ascendente, 
# por último imprimir la lista ordenada.