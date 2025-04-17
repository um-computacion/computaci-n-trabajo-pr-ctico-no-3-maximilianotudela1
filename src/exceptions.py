class NumeroDebeSerPositivo(Exception):
    
    def __init__(self, mensaje="El número debe ser positivo (mayor que cero)."):
        self.mensaje = mensaje
        super().__init__(self.mensaje) 
        
import os
import sys
import unittest
from unittest.mock import patch

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.exceptions import NumeroDebeSerPositivo
from src.calculo_numeros import ingrese_numero

class TestCalculoNumeros(unittest.TestCase):
    @patch('builtins.input', return_value='100')
    def test_ingreso_feliz(self, _):
        self.assertEqual(ingrese_numero(), 100)

    @patch('builtins.input', return_value='-100')
    def test_ingreso_negativo(self, _):
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()

    @patch('builtins.input', return_value='AAA')
    def test_ingreso_letras(self, _):
        with self.assertRaises(ValueError):
            ingrese_numero()

    @patch('builtins.input', return_value='0')
    def test_ingreso_cero(self, _):
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()

    @patch('builtins.input', return_value='12.5')
    def test_ingreso_decimal(self, _):
        self.assertEqual(ingrese_numero(), 12.5)

if __name__ == '__main__':
    unittest.main()


       