import unittest
import Validaciones

class OperacionesTest(unittest.TestCase):
    def test_positive(self):
        self.assertTrue( Validaciones.validarRUC('20512333797') is True)

    def test_ruc_numeros_caracteres(self):
        self.assertEqual(Validaciones.validarRUC("203938"), False)

    def test_ruc_primeros_caracteres(self):
        self.assertEqual(Validaciones.validarRUC("30512333797"), False)
 
if __name__ == '__main__':
    unittest.main()