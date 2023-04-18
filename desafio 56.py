soma = 0
cont = 0
velho = 0
nomevelho = ''
for c in range(1, 5):
   print('========== {}° candidato =========='.format(c))
   nome = str(input('nome: ')).strip()
   idade = int(input('idade: '))
   sexo = str(input('sexo[M\F]: ')).strip()
   soma = soma + idade
   media = soma / 4
   if c == 1 and sexo in 'Mm':
      velho = idade
      nomevelho = nome
   if sexo in 'Mm' and idade > velho:
      velho = idade
      nomevelho = nome
   if sexo in 'Fm' and idade < 20:
      cont = cont + 1


print('a media das idades é {}'.format(media))
print('0 homem mais velho é {} com {} anos'.format(nomevelho, velho))
print('tem {} mulhares com menos de 20 anos'.format(cont))


