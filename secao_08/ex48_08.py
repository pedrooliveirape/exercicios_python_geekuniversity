"""
Faça uma função que receba uma matriz de 3x3 elementos . Calcule a soma dos elementos que estão acima da diagonal principal.
"""


def acimamatriz(l1: list, l2: list, l3: list):
    matriz = [l1, l2, l3]
    resultado = 0
    for c in range(0, len(matriz)):
        for i in range(c+1, len(matriz)):
            resultado += matriz[c][i]
    return resultado


acimamatriz([1, 2, 3], [4, 5, 6], [7, 8, 9])
