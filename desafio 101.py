def voto(ano):
    idade = 2021 - ano
    if idade <= 15:
        return f'Com {idade} anos: Não Vota'
    elif idade < 18:
        return f'Com {idade} anos: Voto opcional'
    elif idade < 60:
        return f'Com {idade} anos: Voto obrigatório'
    else:
        return f'Com {idade} anos: Voto opcional'


#programa principal
ano = int(input('Em que ano você nasceu? '))
print(voto(ano))
