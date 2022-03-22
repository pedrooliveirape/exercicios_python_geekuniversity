import unittest
from ex42_08 import mediavetor
from ex41_08 import maiorvalor
from ex43_08 import gerador
from ex44_08 import par_impar


class Test41(unittest.TestCase):
    def test_maiorvalor_um(self):
        self.assertEqual(
            maiorvalor([5, 4, 3, 2, 1]), 5
        )


class Test42(unittest.TestCase):
    def test_mediavetor_um(self):
        self.assertEqual(
            mediavetor([48, 15, 16, 51, 5, 65, 17, 15, 6, 51]), 28.9
        )

    def test_mediavetor_dois(self):
        self.assertEqual(
            mediavetor([9, 2, 4, 6, 1, 5]), 4.5
        )


class Test43(unittest.TestCase):
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


class Test44(unittest.TestCase):
    def test_numero_elementos(self):
        listas = par_impar([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32])
        tamanho = len(listas[0]) + len(listas[1])
        self.assertEqual(
            tamanho, 30
        )

    def test_a_pares(self):
        resposta = False
        listas = par_impar(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])
        par = listas[0]
        erro = 0
        for c in range(len(par)):
            if par[c] % 2 != 0:
                erro += 1
        if erro == 0:
            resposta = True
        self.assertEqual(
            resposta, True
        )

    def test_b_impar(self):
        resposta = False
        listas = par_impar(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])
        impar = listas[1]
        erro = 0
        for c in range(len(impar)):
            if impar[c] % 2 == 0:
                erro += 1
        if erro == 0:
            resposta = True
        self.assertEqual(
            resposta, True
        )


if __name__ == '__main__':
    unittest.main()
