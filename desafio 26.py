nome = str(input('digite uma frase: ')).strip()
num = nome.lower()
print('a letra A aparece {} vezes'.format(num.count('a')))
print('a primeira letra A apareceu na posição {}'.format(num.find('a')+1))
print('a ultima letra A apareceu na posição {}'.format(num.rfind('a')+1))

