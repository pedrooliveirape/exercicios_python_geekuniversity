"""
Faça uma função que receba um vetor de inteiros e preencha com números aleatórios sem repetição.
"""


def gerador(n: int):
    """

    :param n: Número inteiro que define o tamanho da lista.
    :return: retorna uma lista com tamanho 'n', números aleatórios e não repetidos.
    """
    from random import randint

    lista = []
    for c in range(0, n):
        num = randint(1, 999)
        if num not in lista:
            lista.append(num)
    return lista


