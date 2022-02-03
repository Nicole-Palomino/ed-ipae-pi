def posiciones_de_beta(a: str, b: str):
    #print(a)
    try:
        if len(a) == 0:
            return
        else:
            index = a.index(b)
            if len(posiciones)==0:
                posiciones.append(index)
            else:
                posiciones.append(posiciones[len(posiciones) - 1]+index+1)
            return posiciones_de_beta(a[index+1:], b)
    except:
        print("Fin Programa")

index = 0
posiciones = []    
""" cadena=  input("INGRESE TEXTO : ")
busca=input("INGRESE LETRA A BUSCAR: ") """
# posiciones_de(cadena, busca, index)
""" posiciones_de_beta(cadena, busca) """
#print(posiciones)