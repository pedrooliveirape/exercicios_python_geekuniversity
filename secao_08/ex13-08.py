"""
Faça uma função que receba dois valores numéricos e um símbolo. Este símbolo representará a operação que se deseja efetuar com os números. Se o símbolo for + deverá ser realizada uma adição, se for - uma subtração, se for / uma divisão e se for * será efetuada uma multiplicação.

doctests:

>>> operacao(2,5,'+')
7
>>> operacao(5,3,'-')
2
>>> operacao(12,2,'/')
6.0
>>> operacao(5,5,'*')
25
>>> operacao(6,6,'f')
Operação inválida
"""


def operacao(a: int, b: int, opc: str):
    if opc == '+':
        return a + b
    elif opc == '-':
        return a - b
    elif opc == '/':
        return a / b
    elif opc == '*':
        return a * b
    else:
        print('Operação inválida')
