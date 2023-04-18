sexo = 'Mm'
sexo = str(input('sexo[M,F]: ')).upper()
while sexo != 'M'and sexo != 'F':
    sexo = str(input('inválido. Por favor responda denovo '
                     'sexo[M,F]: ')).upper()
if sexo == 'M':
    print('o seu sexo é masculino. Fim')
elif sexo == 'F':
    print('o seu sexo é feminino. Fim')

