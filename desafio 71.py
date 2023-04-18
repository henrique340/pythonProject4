empres = int(input('Digite o valor de empréstimo R$'))
total = empres
ced = 50
totalced = 0
while True:
    if total >= ced:                    #se o emprestimo é >= a cédula de 50
        total -= ced                    #entao emprestimo - 50
        totalced += 1                   #as cédulas aumenta 1
    else:                               #se nao
        if totalced > 0:                #se o total de cedulas for maior que 0
            print('total de cédulas de {} é {}'.format(ced, totalced))#total de cedulas de 50 é o total de cedulas

        if ced == 50:                   #se cedula é igual a 50
            ced = 20                    #cedula recebe 20
        elif ced == 20:                 #senao se a cedula é igaul a 20
            ced = 10                    #cedula recebe 10
        elif ced == 10:                 #senao se a célula é igaul a 10
            ced = 1                     #cedula recebe 1
        totalced = 0                    #
        if total == 0:
            break

