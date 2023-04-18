dado = dict()
aposentadoria = idade = 0
dado['nome'] = str(input('Nome: '))
dado['Nascimento'] = int(input('Ano de nascimento: '))
dado['carteira'] = int(input('carteira de trabalho[0 não tem]: '))
if dado['carteira'] > 0:
    dado['contratação'] = int(input('ano de contratação: '))
    dado['salário'] = float(input('salário: R$ '))
#aposentadoria == 35 anos de contratação == idade no ano de contratacao mais 35
    idade = dado['contratação'] - dado['Nascimento']
    dado['aposentadoria'] = idade + 35
print('-=' * 30)
for k, i in dado.items():
    print(f'    - {k} tem o valor {i}')
print('-=' * 30)