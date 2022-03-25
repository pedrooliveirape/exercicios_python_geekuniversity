"""
Escreva uma função chamada matrizTransposta() que receba uma matriz quadrada de ordem N e calcule sua transposta (se B é a matriz transposta de A então aij = bji).
"""


def matriztransposta(linha: int, coluna: int, **kwargs: list):
    """
    Retorna a matriz transposta de uma matriz passada seguindo os parâmentros do exemplo a seguir para uma matriz 3x4:

    matriztransposta(3, 4, linha_0=[3, 4, linha_0=[1, 2, 3, 4], linha_1=[5, 6, 7, 8], linha_2=[9, 10, 11, 12]]

    :param linha: Quantidade de linhas da matriz.
    :param coluna: Quantidade de colunas da matriz.
    :param kwargs: Lista contendo os n números das linhas da matriz. Respeitando a quantidade de linhas e colunas.
    :return: Retorna a matriz transposta da matriz informada.
    """
    matriz_axb = [linha, coluna]
    lin = []
    matriz_original = []
    matriz_transposta = []
    for m in range(matriz_axb[0]):
        matriz_original.append(kwargs.get(f'linha_{m}'))
    for c in range((matriz_axb[1])):
        for i in range(matriz_axb[0]):
            lin.append(matriz_original[i][c])
        matriz_transposta.append(lin[:])
        lin.clear()
    return matriz_transposta
