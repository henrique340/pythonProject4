nome = str(input('digite seu nome completo: ')).strip()
num = nome.lower()
lista = num.split()
pri = lista[0]
sob = lista[len(lista)-1]
print('seu primeiro nome é: {}'.format(pri))
print('seu sobrenome é: {}'.format(sob))

