def ficha(nome='<desconhecido>', gols=0):
    print(f'o jogador {nome} fez {gols} gol(s)')


#programa principal
n = str(input('nome: '))
g = str(input('gols: '))
if g.isnumeric():
    int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols = g)
else:
    ficha(n, g)