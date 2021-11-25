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
    #     cliente_receptor = bco.buscar_cliente(nombre_receptor)
    #     if cliente_receptor != None:
    #         self.saldo -= monto
    #         cliente_receptor.saldo += monto

    def consultar_saldo(self) -> float:
        return self.saldo