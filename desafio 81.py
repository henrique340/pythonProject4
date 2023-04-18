qnt = 0
lista = list()
while True:
    num = int(input('digite um número: '))
    while num not in lista:
        lista.append(num)
        qnt += 1
    escolha = str(input('deseja continuar?[S/N] ')).upper()
    if escolha == 'N':
        break
print('você digitou {} elementos'.format(qnt))
lista.sort(reverse=True)
print('os valores em ordem decrescente são {}'.format(lista))
if 5 in lista:
    print('o número 5 faz parte da lista')
else:
    print('o número 5 não faz parte da lista')
