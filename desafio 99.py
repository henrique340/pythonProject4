#bibliotecas
from time import sleep

#função maior
def maior(*num):
    cont = maior = 0
    print('\nanalisando os valores ...')
    print('-=' * 40)
    for valor in num:
        print(f'{valor}', end=' ', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print('forma informados {} valores'.format(cont))
    print('o maior valor informado foi {}'.format(maior))



#programa principal
maior(2, 9, 4, 5)
maior(5, 7, 9)
maior(1, 3)
maior()
