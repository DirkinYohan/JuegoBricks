import unittest

def ordenar_lista(lista):
    return sorted(lista)

class TestListas(unittest.TestCase):
    def test_ordenar_lista(self):
        self.assertEqual(ordenar_lista([3, 1, 2]), [1, 2, 3])
        self.assertEqual(ordenar_lista([5, 0, -1]), [-1, 0, 5])

if __name__ == '__main__':
    unittest.main()