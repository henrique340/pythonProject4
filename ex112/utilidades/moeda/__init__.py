def aumentar(preço = 0, taxa = 0, formato=False):
    res = preço + (preço * taxa)/100
    return res if formato is False else moeda(res)


def diminuir(preço = 0, taxa = 0, formato=False):
    res = preço - (preço * taxa)/100
    return res if formato is False else moeda(res)


def dobro(preço = 0, formato=False):
    res = preço * 2
    return res if formato is False else moeda(res)


def metade(preço = 0, formato=False):
    res = preço / 2
    return res if not formato else moeda(res)


def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')


def resumo(preço=0, taxaa=0, taxad=0):
    print('-' * 45)
    print('RESUMO DO VALOR'.center(45))
    print('-' * 45)
    print(f'Preço analisado: \t\t\t{moeda(preço)}')
    print(f'Preço dobrado: \t\t\t\t{dobro(preço, True)}')
    print(f'Preço metade: \t\t\t\t{metade(preço, True)}')
    print(f'Preço com aumento de {taxaa}%: \t{aumentar(preço, taxaa, True)}')
    print(f'Preço com redução de {taxad}%: \t{diminuir(preço, taxad, True)}')
    print('-' * 45)


