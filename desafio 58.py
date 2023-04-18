import random
cont = 0
print('''sou seu computador
eu pensei em um número de 0 à 10,
será que você consegue adivinhar?''')
n = int(input('digite o seu palpite: '))
cont = cont + 1
comp = random.randrange(0, 10)
while n != comp:
    if n > comp:
        n = int(input('digite outro palpite < que {}: '.format(n)))
        cont += 1
    elif n < comp:
        n = int(input('digite outro palpite > que {}: '.format(n)))
        cont += 1
print('Parabens,o número era {} e você acertou com {} tentativas'.format(comp, cont))