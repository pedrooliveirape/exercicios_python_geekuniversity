"""
Faça uma função chamada 'par_impar()' que receba como parâmetro um vetor X de 30 elementos inteiros e retorne, também por parâmetro, dois vetores A e B. O vetor A deve conter os elementos pares de X e o vetor B, os elementos ímpares.
"""


def par_impar(lista: list):
    a = []
    b = []
    for c in range(30):
        if lista[c] % 2 == 0:
            a.append(lista[c])
        else:
            b.append(lista[c])
    return a, b
