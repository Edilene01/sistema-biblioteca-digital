import os
import unittest
from gerenciador import adicionar_documento, renomear_documento, remover_documento

class TestBiblioteca(unittest.TestCase):

    def setUp(self):
        with open("teste.txt", "w") as f:
            f.write("arquivo de teste")

    def test_renomear(self):
        renomear_documento("teste.txt", "renomeado.txt")
        self.assertTrue(os.path.exists("renomeado.txt"))

    def test_remover(self):
        remover_documento("renomeado.txt")
        self.assertFalse(os.path.exists("renomeado.txt"))

if __name__ == "__main__":
    unittest.main()
