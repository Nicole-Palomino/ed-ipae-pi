import unittest 
from ejercicio1 import es_potencia
from ejercicio2 import posiciones_de_beta

class ejerciciosTest(unittest.TestCase):

    def test_ejercicio_uno_ok(self):
        es_potencia(8,2)

    def test_ejercicio_uno_fail(self):
        es_potencia(7,2) 

    def test_ejercicio_dos(self):
        posiciones_de_beta('hola mundo', 'do')   

    def test_ejercicio_dos_1(self):
        posiciones_de_beta('','do')   

    def test_ejercicio_dos_2(self):   
        posiciones_de_beta('hola','')        

if __name__ == '__main__':
    unittest.main()