from sys import argv
script, nome_arquivo = argv
while True:
    print('''\t[1] ver lista
        [2] adicionar um usuário
        [3] sair do programa''')
    opc = int(input('Digite sua opção: '))
    if opc == 1:
        txt = open(nome_arquivo)
        print('='*45)
        print('CADASTROS'.center(45))
        print('Nome          Idade')
        print('-'*45)
        print(txt.read())
        print('-'*45)
        txt.close()
    elif opc == 2:
        txt = open(nome_arquivo, 'at')
        nome = str(input('Digite seu nome: '))
        idade = str(input('Digite sua idade: '))
        txt.write(f'{nome}; {idade}')
        txt.close()
    elif opc == 3:
        txt.close()
        break