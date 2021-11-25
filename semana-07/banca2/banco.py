from banca2.cliente import Cliente

class Banco:
    def __init__(self) -> None:
        print("Creando banco")
        self.cliente1 = Cliente()
        self.cliente2 = Cliente()
        self.cliente3 = Cliente()
        self.clientes = []
        self.clientes.append(self.cliente1)
        self.clientes.append(self.cliente2)
        self.clientes.append(self.cliente3)

    # def operaciones(self) -> None:
    #     # self.cliente1.depositar(100)
    #     # self.cliente2.depositar(50)
    #     # self.cliente1.retirar(70)
    #     # self.cliente3.depositar(200)
    #     pass

    # def buscar_cliente(self, nombre) -> Cliente:
    #     for cl in self.clientes:
    #         if cl.nombre == nombre:
    #             return cl

    # def depositos_totales(self) -> float:
    #     return self.cliente1.consultar_saldo() + self.cliente2.consultar_saldo() + self.cliente3.consultar_saldo()