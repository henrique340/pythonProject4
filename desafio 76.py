lista = ('lapis', 1.75,
        'borracha', 3.00,
        'papel', 4.00,
        'lixo', 5.00)
print('=' * 45)
print(f'{"listagem de preços":^44}')
print('=' * 45)
for pos in range(0,len(lista)):
    if pos % 2 == 0:            #nome do produto posicao par
        print(f'{lista[pos]:.<30}',end='')
    else:
        print(f'R${lista[pos]:>5.2f}')
print('=' * 45)