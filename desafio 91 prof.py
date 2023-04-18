from random import randint
from time import sleep
from operator import itemgetter
print('--=-=-=JOGO DADOS=-=-=--')
jogo = {'jogador1' : randint(1,6),
        'jogador2' : randint(1,6),
        'jogador3' : randint(1,6),
        'jogador4' : randint(1,6)}
ranking = dict()
print('valores sorteados:')
for k, i in jogo.items():
    print(f'{k} tirou {i} no dado')
    sleep(0.5)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-----=-=-=RANK=-=-=-----')
for pos, v in enumerate(ranking):
    print(f'{pos+1}° lugar: {v[0]} com {v[1]}')
    sleep(0.5 )