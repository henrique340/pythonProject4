c = d = 0
while True:
    tabuada = int(input('Digite um número para ver sua tabuada: '))
    if tabuada < 0:
        break
    c += 1
    print('-=' * 30)
    for d in range(1, 11):
        mult = tabuada * d
        print(f'{tabuada} x {d} = {tabuada * d} ')
    print('-=' * 30)
print(f'você solicitou {c} tabuadas.Fim do programa')