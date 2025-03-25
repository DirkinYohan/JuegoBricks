import unittest
import string
from src.contraseña import generar_contraseña  # Reemplaza 'tu_archivo' con el nombre real del archivo donde está la función

class TestGenerarContrasena(unittest.TestCase):
    
    def test_longitud_por_defecto(self):
        """Verifica que la contraseña generada tenga la longitud por defecto (12 caracteres)."""
        contraseña = generar_contraseña()
        self.assertEqual(len(contraseña), 12)

    def test_longitud_personalizada(self):
        """Verifica que la función respete la longitud personalizada dada."""
        for longitud in [8, 16, 20, 32]:
            with self.subTest(longitud=longitud):
                contraseña = generar_contraseña(longitud)
                self.assertEqual(len(contraseña), longitud)

    def test_caracteres_validos(self):
        """Verifica que la contraseña solo contenga caracteres válidos."""
        caracteres_validos = string.ascii_letters + string.digits + string.punctuation
        contraseña = generar_contraseña(20)  # Se genera una contraseña de 20 caracteres
        self.assertTrue(all(c in caracteres_validos for c in contraseña))

if __name__ == '__main__':
    unittest.main()
