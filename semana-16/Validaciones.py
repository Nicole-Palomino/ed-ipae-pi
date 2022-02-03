def validarRUC(ruc:str) -> bool:
    if len(ruc) == 11:
        iniciales = ["10", "15", "17", "20"]
        val = ruc[0:2]
        if val in iniciales:
            multiplicadores = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
            suma_mult = 0
            for idx in range(10):
                suma_mult += multiplicadores[idx] * int(ruc[idx])
            part_ent = suma_mult // 11
            calculo = 11 - (suma_mult - part_ent*11)
            s_calculo = str(calculo)[-1:] # faltó obtener el último dígito
            return s_calculo == ruc[10:11]
        return False
    return False

#print(validarRUC(input("Ingrese RUC: ")))