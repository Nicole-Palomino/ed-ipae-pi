import persona
import datos_encomiendas

persona_envia = persona.ingreso()
encomienda = datos_encomiendas.ingreso()
persona_recibe = persona.ingreso()

print("%s está enviando %s a %s"
    %(persona.ver_datos(persona_envia["nombre"], persona_envia["dni"]),
    encomienda,
    persona.ver_datos(persona_recibe["nombre"], persona_recibe["dni"])))

