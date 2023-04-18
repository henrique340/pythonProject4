def area(largura, comprimento):
    a = largura * comprimento
    print(f'a área de um terreno {largura}x{comprimento} é de {a}m²')


#programa principal
print('controle de terrenos')
print('-=' * 30)
largura = int(input('Largura [m]: '))
comprimento = int(input('Comprimento [m]: '))
area(largura, comprimento)
