"""
Faça uma função que receba uma matriz 4x4 e retorne quantos valores maiores do que 10 ela possui.
"""


def matriz4x4(l1: list, l2: list, l3: list, l4: list):
    matriz = [l1, l2, l3, l4]
    lista = []
    if len(l1) == len(l2) == len(l3) == len(l4) == 4:
        for i in range(0, len(matriz)):
            lista.extend(matriz[i])
    maior = 0
    for c in range(0, len(lista)):
        if lista[c] > 10:
            maior += 1
    return maior
