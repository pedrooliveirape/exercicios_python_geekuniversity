"""
Faça uma função chamada 'somalinha()' que recebe, por parâmetro, uma matriz A[7][6] e uma linha N e retorne a soma dos elementos dessa linha.
"""


def somalinha(line_0: list, line_1: list, line_2: list, line_3: list, line_4: list, line_5: list, line_6: list, linha: int):
    """Retorna a soma dos elementos contidos na linha passada como parâmetro.

    :param line_0: Primeira linha da matriz 7x6.
    :param line_1: Segunda linha da matriz 7x6.
    :param line_2: Terceira linha da matriz 7x6.
    :param line_3: Quarta linha da matriz 7x6.
    :param line_4: Quinta linha da matriz 7x6.
    :param line_5: Sexta linha da matriz 7x6.
    :param line_6: Sétima linha da matriz 7x6.
    :param linha: Linha que terá seus elementos somados.
    :return: retorna, False caso não ouver seis números por linha ou a soma dos elementos da linha.
    """
    matriz = [line_0, line_1, line_2, line_3, line_4, line_5, line_6]
    # Testando se a matriz é 7x6:
    for c in range(6):
        if len(matriz[c]) != 6:
            return False
    # Somando linha 2 da matriz:
    soma = 0
    for m in range(6):
        soma += matriz[linha][m]
    return soma
