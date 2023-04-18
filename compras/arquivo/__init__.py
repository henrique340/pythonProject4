from compras.interface import *

def criar_arquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('houve um erro')


def arquivo_existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def ler_arquivo(nome):
    global dado
    try:
        a = open(nome, 'rt')
    except:
        print('erro ao ler arq')
    else:
        cabeçalho('compras', 42)
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3}')
    finally:
        a.close()


def cadastro(arq, item, preço):
    try:
        a = open(arq, 'at')
    except:
        print('não foi possível abrir')
    else:
        try:
            a.write(f'{item}; R${preço:.2f}\n')
        except:
            print('erro ao inserir dado')
        else:
            print(f'{item} adicionado com sucesso')