n1 = float(input('digite a sua primeira nota: '))
n2 = float(input('digite a sua segunda nota: '))
media = (n1+n2)/2
print(' a media do aluno é {:.1f}'.format(media))
if media <= 6.0:
    print('o aluno está aprovado')
else:
    print('o aluno está reprovado')