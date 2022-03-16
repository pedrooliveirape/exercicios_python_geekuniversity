"""
Crie um programa que receba três valores (obrigatoriamente maiores que zero), representando as medidas de três lados de um a triângulo. Elabore funções para:
A) Determinar se esses lados formam um triângulo.
B) Caso as medidas formem um triângulo, determinar e mostrar o tipo do triângulo (equilátero, isósceles e escaleno).

Doctests:

>>> triangulo(8,7,16)
Não forma triângulo!
>>> triangulo(8,7,9)
Triângulo escaleno!
>>> triangulo(18,16,16)
Triângulo isósceles!
>>> triangulo(12,12,12)
Triângulo equilátero!
"""


def triangulo(a: int, b: int, c: int):
    if a + b > c and b + c > a and c + a > b:
        if a == b == c:
            print('Triângulo equilátero!')
        elif a == b != c or b == c != a or c == a != b:
            print('Triângulo isósceles!')
        else:
            print('Triângulo escaleno!')
    else:
        print('Não forma triângulo!')
