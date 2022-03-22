import unittest
from ex42_08 import mediavetor
from ex41_08 import maiorvalor
from ex43_08 import gerador


class Test42(unittest.TestCase):
    def test_mediavetor_um(self):
        self.assertEqual(
            mediavetor([48, 15, 16, 51, 5, 65, 17, 15, 6, 51]), 28.9
        )

    def test_mediavetor_dois(self):
        self.assertEqual(
            mediavetor([9, 2, 4, 6, 1, 5]), 4.5
        )


class Test41(unittest.TestCase):
    def test_maiorvalor_um(self):
        self.assertEqual(
            maiorvalor([5, 4, 3, 2, 1]), 5
        )


class test43(unittest.TestCase):
    def test_gerador_true(self):
        lista = gerador(6)
        tipo = type(lista)
        resp = False
        if tipo is list:
            resp = True
        self.assertEqual(
            resp, True
        )

    def test_gerador_repetido(self):
        vetor = gerador(5)
        resultado = True
        for i in range(len(vetor)):
            if vetor.count(i) > 1:
                resultado = False
        self.assertEqual(
            resultado, True
        )


if __name__ == '__main__':
    unittest.main()
