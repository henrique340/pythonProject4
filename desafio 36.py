casa = float(input('qual é o valor da casa desejada: '))
sal = float(input('qual é o seu salário: '))
anos = int(input('em quantos anos gostaria de pagar: '))
mes = anos * 12
por = 0.3 * sal
prestacao = (casa/mes)
final = prestacao * 12
print('a casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(casa, anos, prestacao))
print('sabendo que a prestacao mensal nao pode ser superior a 30% de seu salário')
if prestacao < sal:
    print('ent o emprestimo é VALIDO')
else:
    print('ent o emprestimo é INVALIDO')
