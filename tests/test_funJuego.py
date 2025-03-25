import unittest
from unittest.mock import patch
from src.funJuego import StringIO

# Código original
def iniciar_juego():
    print("¡Iniciando juego!!!")

def mover_personaje(direccion):
    print(f"Moviendo personaje hacia {direccion}")

def finalizar_juego():
    print("¡Fin del juego!!")

# Pruebas unitarias
class TestJuego(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_iniciar_juego(self, mock_stdout):
        iniciar_juego()
        self.assertEqual(mock_stdout.getvalue().strip(), "¡Iniciando juego!!!")

    @patch('sys.stdout', new_callable=StringIO)
    def test_mover_personaje(self, mock_stdout):
        mover_personaje("izquierda")
        self.assertEqual(mock_stdout.getvalue().strip(), "Moviendo personaje hacia izquierda")

    @patch('sys.stdout', new_callable=StringIO)
    def test_finalizar_juego(self, mock_stdout):
        finalizar_juego()
        self.assertEqual(mock_stdout.getvalue().strip(), "¡Fin del juego!!")

if __name__ == '__main__':
    unittest.main()
