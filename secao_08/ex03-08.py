"""
Faça uma função para verificar se um número é positivo ou negativo. sendo que o valor de retorno será 1 se positivo,
-1 se negativo e 0 se for igual a 0.

Doctests:

>>> posneg(1)
1
>>> posneg(-4)
-1
>>> posneg(0)
0
>>> posneg(8)
1
"""


def posneg(num: int):
    if num > 0:
        resp = 1
    elif num < 0:
        resp = -1
    else:
        resp = 0
    return resp
