"""
Faça uma função que retorne o maior fator primo de um número.

Doctests:

>>> fatorprimo(18)
3
>>> fatorprimo(250)
5
>>> fatorprimo(830)
83
>>> fatorprimo(99)
11
"""


def fatorprimo(numero: int):
    fatores = []
    resultado = numero
    cont = 0
    primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
              107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223,
              227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347,
              349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463,
              467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547]

    while resultado > 1:
        try:
            if resultado % primos[cont] == 0:
                resultado = resultado / primos[cont]
                fatores.append(primos[cont])
                cont = 0
            else:
                cont += 1
        except:
            print('Não foi pssível realizar a operação')
    fatores.sort()
    return fatores[-1]
