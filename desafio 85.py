valores = [[], []]
dado = list()
for c in range(1, 8):
    dado = int(input(f'digite o {c}° número: '))
    if dado % 2 == 0:
        valores[0].append(dado)
    else:
        valores[1].append(dado)
print('-=' * 20)
print(f'os valores são {valores}')
valores[0].sort()
valores[1].sort()
print(f'os valores pares são {valores[0]}')
print(f'os valores são impares são {valores[1]}')
