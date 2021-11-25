# Repaso de métodos propios de python
# cadena = "1,2,3,4,5"
# list = cadena.split(",")
# print(cadena)
# print(list)

# uso del método __init__ de una clase
# from Persona import Persona

# print("****** PERSONA UNO **********")
# persona1 = Persona()
# persona1.imprimir_datos()
# persona1.imprimir_mayor_edad()
# persona1.apto_licencia_conducir()

# print("****** PERSONA DOS **********")
# persona2 = Persona()
# persona2.imprimir_datos()
# persona2.imprimir_mayor_edad()
# persona2.apto_licencia_conducir()


# Operaciones bancarias
# from Banca import Cliente
# from Banca import Banco

# bco = Banco()
# # bco.operaciones()

# # cliente1 = Cliente()
# cliente1 = bco.cliente1
# cliente1.depositar()
# cliente1.retirar()
# cliente1.depositar()
# print("El saldo del cliente {} es {}".format(cliente1.nombre, cliente1.consultar_saldo()))

# # cliente2 = Cliente()
# cliente2 = bco.cliente2
# cliente2.depositar()
# cliente2.retirar()
# cliente2.depositar()
# print("El saldo del cliente {} es {}".format(cliente2.nombre, cliente2.consultar_saldo()))

# # cliente3 = Cliente()
# cliente3 = bco.cliente3
# cliente3.depositar()
# cliente3.retirar()
# cliente3.depositar()
# print("El saldo del cliente {} es {}".format(cliente3.nombre, cliente3.consultar_saldo()))

# print("El monto total en el banco es: ", bco.depositos_totales())


# Para descomentar en grupo ctrl + k + u

# Solución 2 de banca
from banca2.banco import Banco


bco = Banco()
print(bco.clientes)