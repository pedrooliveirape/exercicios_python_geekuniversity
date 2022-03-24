"""
Faça uma função que receba uma matriz de 3x3 elementos. Calcule e retorne a soma dos elementos que estão abaixo da diagonal principal.
"""


def abaixomatriz(l1: list, l2: list, l3: list):
    matriz = [l1, l2, l3]
    resultado = 0
    for c in range(1, len(matriz)):
        for i in range(0, c):
            resultado += matriz[c][i]
    return resultado
