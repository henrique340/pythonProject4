num = cont = soma = maior = menor = 0
escolha = 'S'
while escolha == 'S':
        num = int(input('Digite um número: '))
        soma = soma + num
        cont += 1
        if cont == 1:
                maior = num
                menor = num
        else:
                if num > maior:
                        maior = num
                elif num < menor:
                        menor = num
        escolha = str(input('que continuar?[S,N] ')).upper()
media = soma/cont
print('você digitou {} números'.format(cont))
print('o maior é {}'.format(maior))
print('o menor é {}'.format(menor))
print('média é {}'.format(media))
print('a soma é {}'.format(soma))
