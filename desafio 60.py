n = int(input('digite um número para calcular o fatorial: '))
cont = n
f = 1
print('calculando {}! = '.format(n), end='')
while cont > 0:
    print('{}'.format(cont),end='')
    print('x'if cont > 1 else '=',end='')
    f *= cont
    cont = cont - 1
print(' {}'.format(f))
