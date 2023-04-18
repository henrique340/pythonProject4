from random import randint
computador = randint(0,2)
item = ('pedra', 'papel', 'tesoura')

print(''' escolha um dos itens abaixo para jogar
[0] pedra
[1] papel
[2] tesoura''')

jogador = int(input('digite o número escolhido: '))
print('-=' * 20)
print('você escolheu {}'.format(item[jogador]))
print('o computador escolheu {}'.format(item[computador]))
print('-=' * 20)
if computador == 0:#pcu pedra
    if jogador == 1:    #play papel
        print('PARABENS você ganhou')
    elif jogador == 2:    #play tesoura:
        print('você PERDEU')
    elif jogador == computador:
        print('EMPATE')
elif computador == 1:#pcu papel
    if jogador == 0:    #play pedra
        print('você PERDEU')
    elif jogador == 2:    #play tesoura
        print('Parabens você ganhou')
    elif jogador == computador:
        print('EMPATE')
elif computador == 2:#pcu tesoura
    if jogador == 0:    #play pedra
        print('PARABENS você ganhou')
    elif jogador == 1:  #play papel
        print('você PERDEU')
    elif jogador == computador:
        print('EMPATE')
else:
    print('opcao INVALIDA')