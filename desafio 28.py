import random
n1 = int(input('Digite um número aleatório entre 0 e 5: '))
n = int(random.randrange(0, 5))
if n==n1:
    print('parabens, você acertou o número {} aleatório'.format(n))
else:
    print('o número era {}'.format(n))


