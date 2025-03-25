import unittest
from src.palabra import contar_palabras_y_letras  # Importa la función desde tu archivo

class TestContarPalabrasYLetras(unittest.TestCase):
    def test_contar_palabras_y_letras(self):
        self.assertEqual(contar_palabras_y_letras("Hola mundo"), (2, 9))
        self.assertEqual(contar_palabras_y_letras("Python es genial"), (3, 13))
        self.assertEqual(contar_palabras_y_letras(""), (0, 0))
        self.assertEqual(contar_palabras_y_letras("123 4567"), (2, 7))
        self.assertEqual(contar_palabras_y_letras("Un solo"), (2, 6))

if __name__ == '__main__':
    unittest.main()
