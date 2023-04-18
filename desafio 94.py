dado = dict()
pessoas = list()
soma = media = 0
while True:
    dado.clear()
    dado['nome'] = str(input('Nome: '))
    while True:
        dado['sexo'] = str(input('Sexo: [M/F] ')).upper()
        if dado['sexo'] in 'MF':
            break
        print('Erro, digite novamente com M ou F')
    dado['idade'] = int(input('Idade: '))
    soma += dado['idade']
    # pessoas recebe o dicionário na forma de lista
    pessoas.append(dado.copy())
    while True:
        escolha = str(input('Quer continuar? [S/N] ')).upper()
        if escolha in 'SN':
            break
        print('Erro, digite novamente com S ou N')
    if escolha == 'N':
        break
print('-=' * 30)
print(f'A) temos {len(pessoas)} pessoas cadastradas')
media = soma/len(pessoas)
print('B) a media de idade é de {:.2f} anos'.format(media))
print('C) as mulheres cadastradas foram: ',end='')
for c in pessoas:
    if c['sexo'] == 'F':
        print(f'{c["nome"]} ',end='')
print()
print('D) as pessoas acima da media são: ',end='')
for c in pessoas:
    if c['idade'] > media:
        print(f'{c["nome"]} ',end='')
print()
print('-=' * 30)
print('ENCERRANDO')