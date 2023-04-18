n1 = int(input('Digite o tamanho do primeiro segmento: '))
n2 = int(input('Digite o tamanho do segundo segmento: '))
n3 = int(input('Digite o tamanho do terceiro segmento: '))
if n1<n2+n3 and n2<n1+n3 and n3<n1+n2:
    print('é possível fazer um triângulo')
    if n1 == n2 and n2 == n3:
        print('o triângulo é equilátero')
    elif n1 != n2 and n2 != n3 and n3 != n1:
        print('o triângulo é escaleno')
    else:
        print('o triângulo é isósceles')
else:
    print('não é possivel fazer um triângulo')