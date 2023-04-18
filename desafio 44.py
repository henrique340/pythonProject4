print('{:=^20}'.format('loja yuji'))
preco = float(input('Preço total das compras:R$ '))
print('''formas de pagamento
[1] à vista dinheiro ou cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão ''')
cond = int(input('digite a sua escolha: '))
if cond == 1:
    des = 10/100 * preco
    print('a opção 1 oferece 10% de desconto totalizando a compra em R${:.2f}'.format(preco - des))
elif cond == 2:
    desc = 5/100 * preco
    print('a opção 2 oferece 5% de desconto totalizando a compra em R${:.2f}'.format(preco - desc))
elif cond == 3:
    print('a opção 3 não oferece desconto totalizando a comopra em R${:.2f}'.format(preco))
elif cond == 4:
    parcela = int(input('em quantas parcelas? '))
    juros = parcela * (20/100 * preco)
    print('a opção 4 tem 20% de juros por parcela totalizando em {:.2f}'.format(preco + juros))