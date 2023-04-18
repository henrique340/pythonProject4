mil = c = menor = total = 0
barato = ''
while True:
    prod = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: '))
    c += 1
    escolha = str(input('Quer continuar?[S/N] ')).upper()
    total += preco
    if preco > 1000:
        mil += 1
    if c == 1:
        menor = preco
        barato = prod
    else:
        if preco < menor:
            menor = preco
            barato = prod
    if escolha == 'N':
        break
print('''o total da compra é de R${:.2f}
temos {} produtos custando mais do que R$1000,00
o produto mais barato foi {} que custa {:.2f} '''.format(total, mil, barato, menor))
print('{:-^30}'.format('Fim do programa'))
