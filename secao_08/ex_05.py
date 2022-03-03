"""
Faça uma função e um programa de teste para o cálculo do volume de uma esfera. Sendo que o raio é passado por
parâmetro: V = 4/3 * π * R³ 3.14159265

Doctests:

>>> volumecir(50)
523598.33
>>> volumecir(12)
7238.22
>>> volumecir(87)
2758328.59
>>> volumecir(5)
523.60
"""


def volumecir(raio: int):
    resp = float((4 * 3.14159265 * raio ** 3) / 3)
    # resp = f'{resp:.2f}'
    # resp = float(resp)
    return resp
