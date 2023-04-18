from math import sqrt
import os

def linha():
    print('-'*30)


def cabeca(msg):
    linha()
    print(msg)
    linha()


#programa principal
while True:
    cabeca('Equação de 2° grau')
    print('equação do tipo -- ax²+bx+c')
    a = float(input('digite o número a: '))
    b = float(input('digite o número b: '))
    c = float(input('digite o número c: '))
    delta = (b**2) - 4*a*c
    if delta < 0:
        print('nã existem resultados reais')
    elif delta == 0:
        x1 = -b/2*a
        print(f'x = {x1:.2f}')
    elif delta > 0:
        x1 = -b+sqrt(delta)/2*a
        x2 = -b-sqrt(delta)/2*a
        print(f'x1 = {x1:.2f} e x2 = {x2:.2f}')
    opt = str(input('Digite 999 para encerar ou qualquer tecla para continuar: '))
    if opt == '999':
        break


