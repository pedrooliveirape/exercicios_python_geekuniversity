"""
Faça uma função que receba uma matriz de 3x3 elementos. Calcule e retorne a soma dos elementos que estão na diagonal principal.
"""


def soma_digprincipal(l1: list, l2: list, l3: list):
    matriz = [l1, l2, l3]
    resultado = 0
    for c in range(0, len(matriz)):
        resultado += matriz[c][c]
    return resultado
