from random import randint
from time import sleep
cont = 0
total = 1
jogo = list()
lista = list()
escolha = int(input('Quantos jogos você quer fazer: '))
while total <= escolha:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
            cont += 1
        if cont >= 6:
            break
    jogo.sort()
    lista.append(jogo[:])
    jogo.clear()
    total += 1
print('-=' * 30)
print('SORTEANDO {} números'.format(escolha))
print('-=' * 30)
for i, l in enumerate(lista):
    print('......')
    sleep(2)
    print(f'jogo {i+1} é {l}')
