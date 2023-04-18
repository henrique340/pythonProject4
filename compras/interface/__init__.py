def cabeçalho(txt, tam):
    print('-' * tam)
    print(txt.center(tam))
    print('-' * tam)


def menu(lista):
    cabeçalho('Loja YUJI', 42)
    c = 1
    for item in lista:
        print(f'{c} - {item} ')
        c += 1
    print('-' * 42)
    opção = int(input('opção: '))
    return opção
