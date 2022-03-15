"""
Faça uma função que receba a altura e o raio de um cilindro circular e retorne o volume do cilíndro. O volume do cilíndro circular é calculado por meio da seguinte fórmula:
V = π * raio² * altura, onde π = 3.141592

Doctests:

>>> vol_cilindro(15,3)
424.11
>>> vol_cilindro(21,4.5)
1335.96
>>> vol_cilindro(4,1)
12.57
"""


def vol_cilindro(altura: float, raio: float):
    volume = float(f'{3.141592 * raio ** 2 * altura:.2f}')
    return volume
