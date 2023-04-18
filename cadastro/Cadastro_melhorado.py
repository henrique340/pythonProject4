from time import sleep
import os

def LeiaInt(msg):
    '''
    --> ler numero inteiro
    :param msg: recebe número
    :return: retorna o valor com correção se for número
    '''
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'ERRO! Digite um número válido')
        if ok:
            break
    return valor


def Linha(tam=42):
    return '-' * tam


def Cabeçalho(txt):
    print(Linha())
    print(txt.center(42))
    print(Linha())


def Menu(lista):
    Cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(Linha())
    opc = LeiaInt('Sua opção: ')
    return opc

def Limpar():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')



def ArquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def CriarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquvo')
    else:
        print(f'Arquivo {nome} encontrado com sucesso')


def LerArquivo(nome):
    global dado
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arq!')
    else:
        Cabeçalho('pessoas cadastradas')
        for Linha in a:
            dado = Linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def CriarCadastro(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Não foi possível abrir o arq')
    else:
        try:
            a.write(f'{nome}; {idade}\n')
        except:
            print('Houve um erro na inserção de dados')
        else:
            print('novo cadastro adicionado com sucesso')
            print(f'{nome} adicionado')






arq = 'cadastros.txt'


if not ArquivoExiste(arq):
    CriarArquivo(arq)


while True:
    resposta = Menu(['ver pessoas cadastradas', 'cadastrar novas pessoas', 'sair do sistema'])
    if resposta == 1:
        Limpar()
        LerArquivo(arq)
        sleep(1)
    elif resposta == 2:
        Limpar()
        Cabeçalho('novo cadastro')
        nome = str(input('Nome: '))
        idade = LeiaInt('idade: ')
        CriarCadastro(arq, nome, idade)
        sleep(1)
    elif resposta == 3:
        Cabeçalho('Fechando sistema...')
        sleep(1)
        break
    else:
        print('ERRO! digite um número válido')
        sleep(1)