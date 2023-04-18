dado = dict()
listapart = list()
dado['nome'] = str(input('nome do jogador: '))
partidas = int(input(f'Quantas partidas {dado["nome"]} jogou? '))
for c in range(0, partidas):
    listapart.append(int(input(f'   Quantos gols na partida {c}: ')))
    dado['gols'] = listapart[:]
dado['total'] = sum(listapart)
print('-=' * 30)
for k, i in dado.items():
    print(f'o campo {k} tem o valor {i}')
print('-=' * 30)
print(dado)
print('-=' * 30)
for pos, v in enumerate(listapart):
    print(f'    => Na partida {pos}, fez {v} gols')
print(f'    -->foi um total de {dado["total"]} gols')