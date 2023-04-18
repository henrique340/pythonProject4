from ex112.utilidades import moeda
from ex112.utilidades import dado


p = dado.leiaDinheiro('Digite o preço: R$')
a = int(input('Digite a taxa de aumento: '))
b = int(input('Digite a taxa de redução: '))
moeda.resumo(p, a, b)




