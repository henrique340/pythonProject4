from random import randint
dados = dict()
maior = menor = 0
print('---=-=-=JOGO DADOS=-=-=---')
for c in range(0, 4):
    comp = randint(1, 6)
    dados['jogador'] = (f'jogador{c+1}')
    dados['dado'] = (f'{comp}')
    print(f'{dados["jogador"]} tirou {comp} no dado')
print('---=-=-=RANK=-=-=---')
for k, i in dados.items():
    print(f'1° lugar: {k["jogador"]} com {i["comp"]}')
