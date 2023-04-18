lista = list()
dado = list()
media = 0
while True:
    nome = str(input('nome: '))
    n1 = float(input('nota 1: '))
    n2 = float(input('nota 2: '))
    media = (n1 + n2) / 2
    lista.append([nome, [n1, n2], media])
    escolha = str(input('quer continuar?[S/N] ')).upper()
    if escolha == 'N':
        break
print('-=' * 30)
print(f'{"N°":<4}{"Nome":<10}{"Média":>8}')
print('-=' * 30)
for i, l in enumerate(lista):
    print(f'{i:<4}{l[0]:<10}{l[2]:>8.1f}')
while True:
    escol = int(input('deseja ver as notas de qual aluno?[999 para finalizar] '))
    for i, l in enumerate(lista):
        if escol == i:
            print('-=' * 30)
            print(f'as notas do aluno {i} são {l[1]}')
            print('-=' * 30)
    if escol == 999:
        print('-=' * 30)
        print('finalizando ...  ...')
        break