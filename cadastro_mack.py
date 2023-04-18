contador_funcionario = 0
contador65 = 0
media = 0
novo_sal = 0
soma = 0
contador_masc = 0
contador_fem = 0
sexp = ''
while True:
    opc = input('Deseja cadastrar mais um funcionário?[S]/[N]: ')
    if opc == 'S':
        contador_funcionario += 1
        nome = input('Digite o nome do funcionário: ')
        sexo = input('Digite o sexo do funcionário [M]/[F]: ')
        while sexo != 'M' and sexo != 'F':
            sexo = input('Digite o sexo do funcionário [M]/[F]: ')
        salario = float(input('Digite o salário do funcionário: '))
        while salario < 850:
            salario = float(input('Digite o salario do funcionário: '))
        if salario >= 3000:
            novo_sal = salario*1.045
            print(f'o novo salário do funcionário é {nome} é de R$ {novo_sal:,.2f}')
            print('-'*70)
        elif 2000 < salario < 3000:
            novo_sal = salario * 1.065
            print(f'o novo salário do funcionário é {nome} é de R$ {novo_sal:,.2f}')
            contador65 += 1
            print('-'*70)
        else:
            novo_sal = salario * 1.085
            print(f'o novo salário do funcionário é {nome} é de R$ {novo_sal:,.2f}')
            print('-'*70)
        if sexo == 'M':
            contador_masc += 1
            soma = soma + novo_sal
        elif sexo == 'F':
            contador_fem += 1
    else:
        break
media = soma/contador_masc
print(f'{contador65} funcionários receberam reajuste de 6,5%')
print(f'a média dos salários dos funcionários homens é de R$ {media:,.2f}')
print(f'o porcentual de empregados femininos entre todos os funcionários é de {100*contador_fem/contador_funcionario}')