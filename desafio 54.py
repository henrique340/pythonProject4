from datetime import date
cont = 0
conta = 0
atual = date.today().year
for c in range(1,8):

    nascimento = int(input('digite o seu ano de nascimento: '))
    idade = atual - nascimento
    if idade >= 18:
        cont = cont + 1

    elif idade < 18:
        conta = conta + 1

print('tem {} maiores de idade e {} menores de idade'.format(cont, conta))
