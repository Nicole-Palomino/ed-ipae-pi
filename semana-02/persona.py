def ingreso():
    nombre = input('Ingrese el nombre: ')
    dni = input('Ingrese el DNI: ')
    celular = input('Ingrese el telefono: ')

    return {'nombre': nombre, 'dni': dni, 'celular': celular}

def ver_datos(nombre, dni):
    return 'La persona %s con DNI %s'%(nombre, dni)    