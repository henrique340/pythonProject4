#variável expressão e lista
expressao = str(input('digite uma expressão matemática: '))
lista = list()

#causa do '(' ou ')'
#criacao da variavel simbolo
for simbolo in expressao:
    if simbolo == '(':
        lista.append('(')
    elif simbolo == ')':

#se a lista nã oestiver vazia
       if len(lista) > 0:
           lista.pop()
       else:
            lista.append(')')
            break

#escrever a lista se n tiver ( ou ) a mais
if len(lista) == 0:
    print('sua expressão está válida')
else:
    print('sua espressão é inválida')