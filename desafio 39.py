ano = int(input('Digite o seu ano de nascimento: '))
idade = 2021 - ano
al = 18 - idade
la = idade - 18
print('quem nasceu em {} tem {} anos em 2021'.format(ano, idade))
if idade<18:
    print('o seu alistamento militar será daqui a {} ano(s)'.format(al))
elif idade>18:
    print('o seu alistamento militar foi a {} ano(s)'.format(la))
else:
    print('o seu alistamento militar é este ano')
