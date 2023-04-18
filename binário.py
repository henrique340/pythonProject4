opc = int(input('Digite 1 para bin - dec e 2 para dec - bin: '))

# binário para decimal
if opc == 1:
        bin = int(input('digite o número em binário: '))
        bi = str(bin)
        b = list(bi)
        n = len(bi)
        decimal = 0
        while n > 0:
                for item in b:
                        if item == '1':
                                decimal += 2 ** (n - 1)
                        n -= 1
        print(decimal)

# decimal para binário
elif opc == 2:
        dec = int(input('digite o número em decimal: '))
        binario = ''
        while dec > 0:
                resto = dec % 2
                binario = str(resto) + binario
                dec = dec // 2
        print(binario)

else:
        print('Não foi possível escolher uma resposta')
