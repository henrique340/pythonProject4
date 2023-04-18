palavras = ('jogo', 'palavra', 'virgula', 'motor', 'videogame', 'estojo')
for c in palavras:
    print('\nna palavra {} temos: '.format(c.upper()))
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')