termo = int(input('digite o termo: '))
razao = int(input('digite a razao: '))
c = 0
total = 0
mais = 10
while mais != 0:
    total += mais   #total comeca com 10
    while c <= total:    #enquanto contador <= total(10)
        print('{}'.format(termo),end='=>')
        c += 1
        termo += razao
    print('pausa')
    mais = int(input('quantos termos a mais: '))
print('foram calculados {} termos no total'.format(total))
print('FIM')
