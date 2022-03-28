"""
Faça uma função chamada 'comamatriz()' que recebe, por parãmetro, uma matriz A[4][4] e retorna a soma dos seus elementos.
"""


def somamatriz(linha0: list, linha1: list, linha2: list, linha3: list):
    """

    :param linha0: Primeira linha da matriz 4x4. Revebe 4 números inteiros.
    :param linha1: Segunda linha da matriz 4x4. Revebe 4 números inteiros.
    :param linha2: Terceira linha da matriz 4x4. Revebe 4 números inteiros.
    :param linha3: Quarta linha da matriz 4x4. Revebe 4 números inteiros.
    :return: Soma de todos os elementos da matriz.
    """

    matriz = [linha0, linha1, linha2, linha3]
    valid = True
    # validando se matriz é 4x4:
    fourto = 0
    for c in range(0, 4):
        if len(matriz[c]) == 4:
            fourto += 1
    if fourto != 4:
        valid = False
    if valid is False:
        return False
    else:
        # Somando matriz:
        soma = 0
        for i in range(0, 4):
            soma += sum(matriz[i])
        return soma
