tupla =('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
escolha = 'S'
while True:
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        print('tente novamente ',end ='')
    print(f'você digitou o número {tupla[num]}')
    escolha = str(input('você quer continuar? [S/N] ')).upper()
    if escolha == 'N':
        break
print('Fim do programa')


