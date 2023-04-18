n = int(input('digite um número: '))
cont = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[34m', end=' ')
        cont = cont + 1         #calcular qnts números dividiram
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO numero {} é divisível {} vezes'.format(n, cont))
if cont < 3:
    print('o número {} é primo pois é divisível por {} vezes'.format(n, cont))
elif cont > 2:
    print('o número {} não é primo pois é divisível por {} vezes'.format(n, cont))
    
