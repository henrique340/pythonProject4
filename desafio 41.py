ani = int(input('Digite o ano de nascimento: '))
ano = 2021 - ani
if ano<=9:
    print('o atleta está na categoria mirim')
elif ano>9 and ano<14:
    print('o atleta está na categoria infantil')
elif ano>=14 and ano<19:
    print('o atleta está na categoria junior')
elif ano>=19 and ano<25:
    print('o atleta está na categoria sênior')
else:
    print('o aluno está na categoria master')
# ou pode fazer usando a biblioteca data
#from datetime import date
#atual = date.today().year
#idade = atual - ani