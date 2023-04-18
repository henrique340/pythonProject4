def LeiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'\033[0;31mERRO! Digite um número inteiro válido\033[m')
        if ok:
            break
    return valor


def LeiaFloat(msg):
    escolha = False
    numero = 0
    while True:
        f = str(input(msg)).strip().replace(',', '.') 
        if f.isalpha() or f == ' ' or f == '':
            print(f'\033[0;31mERRO! Digite um número real válido\033[m')
            escolha = False
        else:
            escolha = True
            numero = float(f)
        if escolha == True:
            break
    return numero






#programa principal
n = LeiaInt('Digite um número inteiro: ')
print(f'Você acabou de digitar o número inteiro {n}')
f = LeiaFloat('Digite um número real: ')
print(f'Você acabou de digitar o número real {f}')