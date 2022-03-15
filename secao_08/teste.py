numero = 251

if numero < 1:
    print('Número inválido')
else:
    unidades = str(numero)
    soma = 0
    for c in range(0, len(unidades)):
        soma += int(unidades[c])
        print(soma)
