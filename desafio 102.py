def fatorial(x=1, show=False):
    """
    -->
    :param num: número a ser calculado o fatorail
    :param show: (opcional) mostrar ou não a conta
    :return: o valor fatorial de num
    """
    n = 1
    for cont in range(x, 0, -1):
        if show:
            print(cont, end='')
            if cont > 1:
                print(' x ',end='')
            else:
                print(' = ',end='')
        n *= cont
    return n

#programa principal
x = int((input('numero: ')))
print(fatorial(x, show=True))
help(fatorial)