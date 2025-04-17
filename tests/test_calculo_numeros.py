import unittest
from unittest.mock import patch
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestCalculoNumeros(unittest.TestCase):
    @patch('builtins.input', return_value='100')
    def test_ingreso_feliz(self, patch_input):
        """Prueba el caso de ingreso de un número válido positivo."""
        from src.calculo_numeros import ingrese_numero
        numero = ingrese_numero()
        self.assertEqual(numero, 100)
    
    @patch('builtins.input', return_value='12.5')
    def test_ingreso_decimal(self, patch_input):
        """Prueba el caso de ingreso de un número decimal positivo."""
        from src.calculo_numeros import ingrese_numero
        numero = ingrese_numero()
        self.assertEqual(numero, 12.5)


    def test_ingreso_negativo(self, patch_input):
        """Prueba el caso de ingreso de un número negativo."""
        from src.calculo_numeros import ingrese_numero
        from src.exceptions import NumeroDebeSerPositivo
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()
    
    @patch('builtins.input', return_value='0')
    def test_ingreso_cero(self, patch_input):
        """Prueba el caso de ingreso del número cero."""
        from src.calculo_numeros import ingrese_numero
        from src.exceptions import NumeroDebeSerPositivo
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()
    def test_ingreso_letras(self, patch_input):
        """Prueba el caso de ingreso de texto no numérico."""
        from src.calculo_numeros import ingrese_numero
        with self.assertRaises(ValueError):
            ingrese_numero()
            
    @patch('builtins.input', return_value='123abc')
    def test_ingreso_alfanumerico(self, patch_input):
        """Prueba el caso de ingreso de texto alfanumérico."""
        from src.calculo_numeros import ingrese_numero
        with self.assertRaises(ValueError):
            ingrese_numero()       

if __name__ == '__main__':
    unittest.main()