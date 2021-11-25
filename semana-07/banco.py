class Cliente:
    
    def __init__(self) -> None:
        self.nombre = input("Nombre del Cliente: ")
        self.saldo = 0.0

    def depositar(self) -> None:
        # self.saldo = self.saldo + monto
        monto = float(input("Monto a depositar: "))
        self.saldo += monto
    
    def retirar(self) -> None:
        monto = float(input("Monto a retirar: "))
        if self.consultar_saldo() >= monto:
            self.saldo -= monto
        else:
            print("Saldo insuficiente")

    # def transferir(self, bco: Banco) -> None:
    #     monto = float(input("Monto a transferir: "))
    #     nombre_receptor = input("Cliente a transferir")
    #     if nombre_receptor

    def consultar_saldo(self) -> float:
        return self.saldo

class Banco:
    def __init__(self) -> None:
        self.cliente1 = Cliente()
        self.cliente2 = Cliente()
        self.cliente3 = Cliente()

    def operaciones(self) -> None:
        # self.cliente1.depositar(100)
        # self.cliente2.depositar(50)
        # self.cliente1.retirar(70)
        # self.cliente3.depositar(200)
        pass

    # def buscar_cliente(self, nombre) -> Cliente:
    #     if self.cliente1 == nombre:
    #         return self.cliente1
    #     if self.cliente2 == nombre:
    #         return self.cliente2
    #     if self.cliente3 == nombre:
    #         return self.cliente3

    def depositos_totales(self) -> float:
        return self.cliente1.consultar_saldo() + self.cliente2.consultar_saldo() + self.cliente3.consultar_saldo()