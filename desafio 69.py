c = d = e = 0
while True:
    nome = str(input('digite seu nome: '))
    idade = int(input('Digite a idade: '))
    sexo = str(input('digite o sexo[M/F]: ')).upper()
    print(f'{nome} {idade} {sexo}')
    print('-=' * 30)
    escolha = str(input('Quer continuar?[S/N] ')).upper()
    if idade > 18:
        c += 1
    if sexo == 'M':
        d += 1
    if sexo == 'F' and idade < 20:
        e += 1
    if escolha == 'N':
        break
print(f'''total de pessoas com mais de 18 anos:{c} 
 ao todo tem {d} homens cadastrados
 e temos {e} mulher com menos de 20 anos''')


#while True:
#    idade=int(input('idade: '))
#    sexo = ' '
#    while sexo not in 'MF':
#        sexo = str(input('sexo?[S/F] '))

