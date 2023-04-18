maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('digite o peso da {}°a pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('o maior peso é {}Kg'.format(maior))
print('o menor peso é {}kg'.format(menor))

