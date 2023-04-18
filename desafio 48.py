soma = 0
cont = 0
for contador in range(1, 501, 2):
    if contador %3 == 0:
        soma = soma + contador
        cont = cont + 1
print('a soma de todos os {} valores multiplos de 3 impares é {}'.format(cont, soma))



