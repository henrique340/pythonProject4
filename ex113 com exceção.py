def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO!, digite um número inteiro válido\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[0;31mEntrada de dados interrompida pelo usuário\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mErro! digite um número real válido\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mEntrada de dados interrompida pelo usuário\033[m')
            return 0
        else:
            return n



#programa principal
num = leiaInt('Digite um número inteiro: ')
print(f'o valor digitado foi {num}')
nf = leiaFloat('Digite um número real: ')
print(f'o valor digitado foi {nf:.1f}')

