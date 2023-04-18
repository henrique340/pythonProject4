termo = int(input('digite o termo: '))
razao = int(input('digite a razao: '))
c = 0
while c < 10:
    print('{}'.format(termo),end='=>')
    c += 1
    termo += razao
print('FIM')
