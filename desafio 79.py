listnum = list()
escolha = 'S'
while True:
    valor = int(input('digite um valor: '))
    if valor not in listnum:
        print('valor adicionado com sucesso')
        listnum.append(valor)
    else:
        print('número duplicado, tente denovo')
    escolha = str(input('deseja continuar?[S/N] ')).upper()
    while escolha not in 'SN':
        print('valor inválido. Tente novamente')
    if escolha == 'N':
        break
listnum.sort()
print('você digitou os valores {}'.format(listnum))