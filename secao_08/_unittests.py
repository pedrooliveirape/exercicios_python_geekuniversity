import unittest
from ex42_08 import mediavetor
from ex41_08 import maiorvalor
from ex43_08 import gerador
from ex44_08 import par_impar
from ex45_08 import desviopadrao
from ex46_08 import normal, inversa, media
from ex47_08 import matriz4x4
from ex48_08 import acimamatriz
from ex49_08 import abaixomatriz
from ex50_08 import soma_digprincipal
from ex51_08 import soma_digsecundaria
from ex52_08 import matriztransposta


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


class Test45(unittest.TestCase):
    def test_desvio_padrao_um(self):
        self.assertEqual(
            desviopadrao([78, 72, 66]), 4.90
        )

    def test_devio_padrao_dois(self):
        self.assertEqual(
            desviopadrao([83, 65, 65]), 8.49
        )


class Test46(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(
            normal([83, 65, 65, 78, 72, 66]), print(83, 65, 65, 78, 72, 66)
        )

    def test_inversa(self):
        self.assertEqual(
            inversa([83, 65, 65, 78, 72, 66]), print([66, 72, 78, 65, 65, 83])
        )

    def test_media(self):
        self.assertEqual(
            media([83, 65, 65, 78, 72, 66]), 71.5
        )


class Test47(unittest.TestCase):
    def test_matriz4x4(self):
        self.assertEqual(
            matriz4x4([1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]), 6
        )


class Test48(unittest.TestCase):
    def test_acima_matriz(self):
        self.assertEqual(
            acimamatriz([1, 2, 3], [4, 5, 6], [7, 8, 9]), 11
        )


class Test49(unittest.TestCase):
    def test_abaixo_matriz(self):
        self.assertEqual(
            abaixomatriz([1, 2, 3], [4, 5, 6], [7, 8, 9]), 19
        )


class Test50(unittest.TestCase):
    def test_soma_diagonal_principal(self):
        self.assertEqual(
            soma_digprincipal([1, 2, 3], [4, 5, 6], [7, 8, 9]), 15
        )


class Test51(unittest.TestCase):
    def test_soma_diagonal_secundaria(self):
        self.assertEqual(
            soma_digsecundaria([1, 2, 3], [4, 5, 6], [7, 8, 9]), 15
        )


class Test52(unittest.TestCase):
    def test_matriz_transposta(self):
        self.assertEqual(
            matriztransposta(3, 4, linha_0=[1, 2, 3, 4], linha_1=[5, 6, 7, 8], linha_2=[9, 10, 11, 12]), [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
        )


if __name__ == '__main__':
    unittest.main()
