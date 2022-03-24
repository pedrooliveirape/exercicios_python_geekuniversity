"""
Faça uma função que receba uma matriz de 3x3 elementos. Calcule e retorne a soma dos elementos que estão na diagonal secundária.
"""


def soma_digsecundaria(l1: list, l2: list, l3: list):
    matriz = [l1, l2, l3]
    resultado = 0
    for c in range(0, len(matriz)):
        resultado += matriz[c][2-c]
    return resultado
