cont = 0
soma = 0
num = 0
num = int(input('digite um número ou [999] para parar: '))
cont += 1
while num != 999:
    cont += 1
    soma = soma + num
    num = int(input('digite um número ou [999] para parar: '))
print('você digitou {} números e a soma deles é {}'.format(cont, soma))