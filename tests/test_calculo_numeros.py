import unittest
from unittest.mock import patch
import sys
import os

# Agregar directorio src al path para importar los módulos
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

if __name__ == '__main__':
    unittest.main()