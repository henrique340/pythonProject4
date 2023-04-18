soma = 0
cont = 0
for c in range (1,7):
    n1 = int(input('digite um número: '))
    if n1 %2 == 0:
        cont = cont + 1
        soma = soma + n1
print('a soma dos {} numeros pares é {}'.format(cont, soma))

