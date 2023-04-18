from time import sleep
cores = ('\033[m',       #-sem cor  - 0
        '\033[0;30;41m', #-vermelho - 1
        '\033[0;30;42m', #-verde    - 2
        '\033[0;30;43m', #-amarelo  - 3
        '\033[0;30;44m', #-azul     - 4
        '\033[0;30;45m', #-roxo     - 5
        '\033[7;30m'     #-branco   - 6
         )


def ajuda(nome):
    título(f'aceesando o manual do comando \'{nome}\'', 4)
    print(cores[4], end='')                                 #cor do título acessando manual ...
    help(nome)
    print(cores[0], end='')                                 #cor da ajuda
    sleep(2)


def título(msg, cor=0):
    print(cores[cor], end='')
    print('~' * len(msg))
    print(msg)
    print('~' * len(msg))
    print(cores[0], end='')
    sleep(1)au

#programa principal
escolha = ''
while True:
    título('Sistema de ajuda PyHELP', 6)
    escolha = str(input('Biblioteca ou função: '))
    if escolha.upper() == 'FIM':
        break
    else:
        ajuda(escolha)
título('Fim do programa', 1)
