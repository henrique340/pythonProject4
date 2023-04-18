n = int(input('Digite um numero para calcular seu fatorial: '))
c = 0
f = 1
for c in range (n, 0, -1):
    f *= n
    n -= 1
print('{}'.format(c))
print('Seu fatorial é {}.'.format(f))
