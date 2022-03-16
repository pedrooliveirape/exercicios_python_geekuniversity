"""
Faça uma função que receba dois números inteiros positivos por parâmetro e um parâmetro boleano opcional (por padrão True) e retorne a soma dos N números inteiros existentes entre eles. Caso False, a soma ocorrerá excluindo os números selecionados (a=10, b=13, retorno=23). Caso True, a soma incluirá os parâmetros digitados (a=10, b=13, retorno=46)

Doctests:

>>> somaintervalo(10,13)
46
>>> somaintervalo(10,13,False)
23
>>> somaintervalo(45,84)
2580
>>> somaintervalo(84,45,False)
2451
"""


def somaintervalo(a: int, b: int, intervalo: bool = True):
    if a > b:
        maior = a
        menor = b
    else:
        maior = b
        menor = a
    soma = 0

    if intervalo is True:
        for c in range(menor, maior + 1):
            soma += c
        print(soma)
    else:
        for c in range(menor + 1, maior):
            soma += c
        print(soma)
