"""
Faça uma função chamada 'matrizIdentidade()' que verifica se uma matriz quadrada de ordem N é a matriz identidade.
"""


def matrizidentidade(linha: int, coluna: int, **kwargs: list):
    matriz_axb = [linha, coluna]
    matriz = []
    identidade = True
    somamatriz = 0
    if linha != coluna:
        identidade = False
    for m in range(matriz_axb[0]):
        matriz.append(kwargs.get(f'linha_{m}'))
        if len(kwargs.get(f'linha_{m}')) != linha:
            identidade = False
    print(matriz)
    for c in range(matriz_axb[0]):
        for i in range(c, c+1):
            if matriz[c][i] != 1:
                identidade = False
    for p in range(len(matriz)):
        somamatriz += sum(matriz[p])
    if somamatriz - linha != 0:
        identidade = False
    print(identidade)


matrizidentidade(3, 3, linha_0=[1, 0, 0], linha_1=[0, 1, 0], linha_2=[0, 0, 1])
