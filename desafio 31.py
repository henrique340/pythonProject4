n = int(input('Digite a distância em Km: '))
n1 = n*0.45
n2 = n*0.50
if n>200:
    print('o preço da passagem de {} Km é de {}'.format(n, n1))
else:
    print('o preço da passagem de {} Km é {}'.format(n, n2))
