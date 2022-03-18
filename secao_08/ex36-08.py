"""
Faça uma função não-recursiva que receba um número inteiro positivo N e retorne o superfatorial desse número. O superfatorial de um número N é definida pelo produto dos N primeiros fatoriais de N. Assim, o superfatorial de 4 é sf4)=1!*2!*3!*4!=288.

Doctests:

>>> superfatorial(4)
288
>>> superfatorial(1)
1
>>> superfatorial(3)
12
>>> superfatorial(7)
125411328000
"""


def superfatorial(n: int):
    listfat = []
    sf = 1
    for c in range(1, n+1):
        fat = 1
        for i in range(1, c+1):
            fat *= i
        listfat.append(fat)
    for x in range(0, len(listfat)):
        sf *= listfat[x]
    return sf
