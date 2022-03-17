"""
Faça um algorítimo que receba um número inteiro posito n e calcule o somatório de 1 até n.

doctests:

>>> somatorio(3)
6
>>> somatorio(17)
153
>>> somatorio(1)
1
>>> somatorio(84)
3570
"""


def somatorio(n: int):
    soma = 0
    for c in range(1, n+1):
        soma += c
    return soma
