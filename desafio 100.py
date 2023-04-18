#bibliotecas
from random import randint
from time import sleep

#função que sorteia
def sorteia(dado):
    for c in range(0, 5):
        n = randint(1, 10)
        dado.append(n)
        print(n, end=' ')
        sleep(0.3)

#função soma de par
def somaPar(dado):
    soma = 0
    for valor in dado:
        if valor % 2 == 0:
            soma += valor
    print(f'somando os valores pares de {dado} temos {soma}')


#programa principal
numeros = list()
sorteia(numeros)
somaPar(numeros)

#conclusões
# dado é uma lista das funções
# valor é a varredura do dado
# números é a lista final com o sorteio
# numeros também é a lista final com a soma dos pares

