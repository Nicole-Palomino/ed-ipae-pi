# El script debe pedir ingresar en qué idioma saludar
# dependiendo del idioma ingresado el programa saludará en dicho idioma
import traductor.espaniol, traductor.english, traductor.portugues

print('Los idiomas son: ')
print('Español = es')
print('Inglés = en')
print('Portugués = po')
print('')

idioma = input('Seleccione su idioma por favor: ')
print('')

if (idioma == 'es'.upper() or idioma == 'es'.lower()) :
    print(traductor.espaniol.saludar())
elif (idioma == 'en'.upper() or idioma == 'en'.lower()):
    print(traductor.english.saludar())
elif (idioma == 'po'.upper() or idioma == 'po'.lower()):
    print(traductor.portugues.saludar())    
else:
    print('Aun no tenemos disponible dicho idioma')    
    
