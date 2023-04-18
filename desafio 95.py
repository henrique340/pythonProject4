time = list()
dado = dict()
listapart = list()

#enquanto verdade
while True:
    dado.clear()
    dado['nome'] = str(input('nome do jogador: '))
    partidas = int(input(f'Quantas partidas {dado["nome"]} jogou? '))
    listapart.clear()
    for c in range(0, partidas):
        listapart.append(int(input(f'   Quantos gols na partida {c+1}: ')))
        dado['gols'] = listapart[:]
    dado['total'] = sum(listapart)
    time.append(dado.copy())
    while True:
        escolha = str(input('quer continuar? [S/N]')).upper()
        if escolha in 'SN':
            break
        print('responda S ou N')
    if escolha == 'N':
        break
print('-' * 40)
print('cod', end='')


#nome;  gols;   total
for i in dado.keys():
    print(f' {i:<15}', end='')
print()
print('-' * 40)


# pos[] nome[]; gols[]  total[]
for k, v in enumerate(time):
    print(f'{k:<3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
print('-' * 40)

#enquanto verdade
while True:
    busca = int(input('Mostrar dados de qual jogador?[999 para parar] '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro, não é possível fazer um levantamento com o código {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]["gols"]):
            print(f' No jogo {i+1} fez {g} gols')
    print('- * 40')
print('volte sempre')