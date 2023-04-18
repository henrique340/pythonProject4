from random import randrange
print('-=' * 30)
soma = par = c = 0
while True:
    Pi = str(input('par ou ímpar[P/I]? ')).upper()
    escolha = int(input('Digite quantos dedos: '))
    comp = randrange(0, 11)
    soma = escolha + comp
    print(f'você mostrou {escolha} e o computador mostrou {comp} dedos. total de {soma}')
    if Pi == 'P':
        if soma%2 == 0:
            print('deu PAR. Você ganhou')
            c += 1
        else:
            print('deu IMPAR. Você perdeu',end=' ')
            break
    elif Pi == 'I':
        if soma%2 == 1:
            print('deu IMPAR. Você ganhou')
            c += 1
        else:
            print('deu PAR. Você perdeu',end =' ')
            break
print(f'e ganhou {c} vezes')
