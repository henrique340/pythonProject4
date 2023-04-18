lista = list()
pares = list()
impar = list()
while True:
    valor = int(input('digite um número: '))
    while valor not in lista:
        lista.append(valor)
    escolha = str(input('Quer continuar?[S/N] ')).upper()
    if valor%2 == 0:
        pares.append(valor)
    if valor%2 == 1:
        impar.append(valor)
    if escolha == 'N':
        break
print('a lista de todos os números é {}'.format(lista))
print('a lista dos numeros pares é {}'.format(pares))
print('a lista dos numeros impares é {}'.format(impar))