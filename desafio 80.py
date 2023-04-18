lista = list()
for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if c == 0 or num > lista[-1]:
        lista.append(num)
        print('adicionando no fim da lista')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print('adicionando na posição {} da lista'.format(pos))
                break
            pos += 1
print('os valores digitados em ordem são {}'.format(lista))

