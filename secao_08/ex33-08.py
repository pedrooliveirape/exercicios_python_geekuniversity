"""
Faça uma função que receba um número N e retorne a soma dos algarítimos de N!. Ex: se N = 4, N! = 24. Logo, a soma de seus algarismos é 2 + 4 = 6.

Doctests:

>>> somaalgarismos(4)
6
>>> somaalgarismos(12)
27
>>> somaalgarismos(7)
9
>>> somaalgarismos(0)
1
"""


def somaalgarismos(n: int):
    fat = 1
    soma = 0
    for c in range(1, n+1):
        fat *= c
    fat = str(fat)
    for p in range(0, len(fat)):
        soma += int(fat[p])
    return soma
