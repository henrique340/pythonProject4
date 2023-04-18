def Arquivo_existe(nome):
    try:
        a = open(nome, 'r')
        a.close()
    except:
        print('ERRO, arq não existe')

def Criar_arquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('ERRO ao criar arq')


