matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = somacol = mai = 0
#digitar na tela a linha e coluna

for linha in range(0, 3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}], [{coluna}]: '))
print('-=' * 15)
#escrever a matriz na tela

for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]',end='')
    print()
print('-=' * 15)
#calcular a soma de todos os pares

for linha in range(0, 3):
    for coluna in range(0, 3):
        if matriz[linha][coluna]%2 == 0:
            soma += matriz[linha][coluna]
#mesma coluna(2) e linhas diferentes

for linha in range(0, 3):
    somacol += matriz[linha][2]
#mesma linha e colunas diferentes

for coluna in range(0, 3):
    mai = matriz[1][coluna]
    if matriz[1][coluna] > mai:
        mai = matriz[1][coluna]
print(f'A soma dos valores pares é {soma}')
print(f'A soma dos valores da terceira coluna é {somacol}')
print(f'O maior valor da segunda linha é {mai}')
