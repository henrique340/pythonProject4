nome = str(input('digite uma frase: ')).strip().upper()
pal =   nome.split()
junto = ''.join(pal)
inv = ''
for c in range(len(junto)-1, -1, -1):
    inv = inv + junto[c]
#inves de usar for pode usar
#inv = junto[::-1]
print('a frase é {}'.format(junto))
print('a frase inversa é {}'.format(inv))
if inv == junto:
    print('a frase é um polindromo')
else:
    print('a frase não é um polindromo')

