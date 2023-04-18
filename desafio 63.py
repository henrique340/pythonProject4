qnt = int(input('digite a quantidade de números da sequecia de Fibonacci: '))
t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2),end='')
cont = 3
while cont <= qnt:
    t3 = t2 + t1
    print('-> {}'.format(t3),end='')
    t1 = t2
    t2 = t3
    cont += 1
print('-> 123FIM')