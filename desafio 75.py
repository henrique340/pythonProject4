n = (int(input('Digite um número: ')),
    int(input('Digite um número: ')),
    int(input('Digite um número: ')),
    int(input('Digite um número: ')))
print('você digitou os valores {}'.format(n))
print('o número 9 apareceu {} vezes'.format(n.count(9)))
if 3 in n:
    print(f'o número 3 está na posição {n.index(3)+1}')
    print('os valores pares digitados são ' , end='')
else:
    print('o numero 3 não está em nenhuma posição')
    print('os valores pares digitados são ', end='')
for c in n:
    if c % 2 == 0:
        print(c,end=' ')