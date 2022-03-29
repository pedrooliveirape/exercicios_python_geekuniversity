"""
Faça uma função chamada 'somaprisec()' que recebe, por parâmetro, uma matriz A[3][3] e retorne a soma dos elementos da sua diagonal principal e da soma da sua secundária.
"""


def somaprisec(linha_0: list, linha_1: list, linha_2: list):
    # Testando se a matriz é 3x3:
    matriz = [linha_0, linha_1, linha_2]
    for c in range(3):
        if len(matriz[c]) != 3:
            return False
    # Somando diagonal principal:
    soma = 0
    for p in range(3):
        soma += matriz[p][p]
    # Somando diagonal secundária:
    for s in range(3):
        soma += matriz[s][2-s]
    return soma
