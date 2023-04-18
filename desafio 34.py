n = int(input('Digite seu salário mensal: '))
aum10 = n/10
aum15 = n*0.15
if n>1250:
    print('seu aumento será de 10% seu novo salário será R${:.0f},00'.format(aum10))
else:
    print('seu aumento será de 15 % seu novo salário será R${>,0f},00'.format(aum15))