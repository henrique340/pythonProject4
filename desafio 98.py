from time import sleep
def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    print('-=' * 40)
    print(f'contagem de {inicio} até {fim} de {passo} em {passo}')
    print('-=' * 40)
    #contagem começando do início e recebendo + passo
    cont = inicio
    if inicio < fim:
        while cont <= fim:
            sleep(0.3)
            print(f'{cont}',end=' ')
            cont += passo
        print('FIM!')
    if inicio > fim:
        while cont >= fim:
            sleep(0.3)
            print(f'{cont}',end=' ')
            cont -= passo
        print('FIM!')


#programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('personalize sua propria contagem')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
