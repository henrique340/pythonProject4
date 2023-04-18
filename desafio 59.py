n1 = int(input('digite o primeiro valor: '))
n2 = int(input('digiteo segudo valor: '))
op = 0
soma = n1 + n2
mult = n1 * n2
maior = 0
while op != 5:
    print('''    [1] soma
    [2] multiplicacao
    [3] maior
    [4] novos numeros
    [5] sair''')
    op = int(input('digite sua opção: '))
    if op == 1:
        print('a soma entre {} e {} é {}'.format(n1, n2, soma))
    elif op == 2:
        print('a multiplicação entre {} e {} é {}'.format(n1, n2, mult))
    elif op == 3:
        if n1 >= n2:
            print('o maior numero é {}'.format(n1))
        else:
            print('o maior numero é {}'.format(n2))
    elif op == 4:
        print('informe os números novamente')
        n1 = int(input('digite um número: '))
        n2 = int(input('digite outro número: '))
    else:
        print('tente novamente')
    print('=' * 30)
print('FIM')

