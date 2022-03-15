"""
Elabore uma função que receba três notas de um aluno como parâmetro e uma letra. Se a letra for A, a função deverá calcular a média aritmética das notas do aluno; se for P, deverá calcular a média poderada, com pesos 5, 3, 2.

Doctests:
>>> media_nota(5,8,6,'p')
6.1
>>> media_nota(6,9,7,'f')
"tipo so aceita as letras 'a' ou 'p'."
>>> media_nota(5,8,6,'a')
6.3
"""


def media_nota(n1: float, n2: float, n3: float, tipo: str):
    if tipo != 'a' and tipo != 'p':
        return "tipo so aceita as letras 'a' ou 'p'."
    elif tipo == 'a':
        media = float(f'{(n1 + n2 + n3)/3:.1f}')
        return media
    else:
        media = float(f"{(n1*5 + n2*3 + n3*2)/10:.1f}")
        return media
