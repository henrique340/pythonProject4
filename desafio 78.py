listanum = list()
for c in range(0,5):
    listanum.append(int(input('Digite um valor para a posição {}: '.format(c))))
print('-=' * 30)
print(f'o menor número é o {min(listanum)} na posição - ',end='')
for pos, valor in enumerate(listanum):
    if valor == min(listanum):
        print('{}...'.format(pos),end='')
print(f'\no maior número é o {max(listanum)} na posição - ', end='')
for pos, valor in enumerate(listanum):
    if valor == max(listanum):
        print('{}...'.format(pos),end='')

