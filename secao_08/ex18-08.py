"""
Faça uma função que receba dois valores X e Z. Calcule e retorne o resultado de X^z para o programa principal. Atenção, não utilize nenhuma função pronta de exponenciação.

Doctests:

>>> expoente(2,2)
4
>>> expoente(5,9)
1953125
>>> expoente(12,4)
20736
>>> expoente(6,0)
1
>>> expoente(3,3)
27
"""


def expoente(x: int, z: int):
    resposta = x ** z
    return resposta