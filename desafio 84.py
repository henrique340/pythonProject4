principal = list()
dado = list()
maior = menor = 0
while True:
    dado.append(str(input('nome: ')))
    dado.append(float(input('peso: ')))
    if len(principal) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    principal.append(dado[:])
    dado.clear()
    escolha = str(input('quer continuar?[S/N] ')).upper()
    if escolha == 'N':
        break
print(f'os dados são {principal}')
print(f'ao todo você cadastrou {len(principal)} pessoas')
print(f'o maior peso foi de {maior}kg. Peso de ',end='')
for p in principal:
    if p[1] == maior:
        print(f'{p[0]}')
print()
print(f'o menor peso foi de {menor}kg. Peso de ',end='')
for p in principal:
    if p[1] == menor:
        print(f'{p[0]}')


