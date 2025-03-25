import unittest
import math
from src.circulo import calcular_area_circulo, calcular_perimetro_circulo

class TestCirculo(unittest.TestCase):
    def test_calcular_area_circulo(self):
        self.assertAlmostEqual(calcular_area_circulo(1), math.pi, places=5)
        self.assertAlmostEqual(calcular_area_circulo(0), 0, places=5)
        self.assertAlmostEqual(calcular_area_circulo(2), 4 * math.pi, places=5)

    def test_calcular_perimetro_circulo(self):
        self.assertAlmostEqual(calcular_perimetro_circulo(1), 2 * math.pi, places=5)
        self.assertAlmostEqual(calcular_perimetro_circulo(0), 0, places=5)
        self.assertAlmostEqual(calcular_perimetro_circulo(2), 4 * math.pi, places=5)

if __name__ == '__main__':
    unittest.main()