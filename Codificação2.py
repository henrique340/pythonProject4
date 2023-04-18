frase = input("")

for linha in frase:
    linha = linha.strip()  # remove espaços em branco no início e no final da linha
    nova_linha = ""
    if 'Exit' == linha.rstrip():
        print('Fim do programa')
        break
    else:
        for char in linha:
            if char == '@':
                nova_linha += 'a'
            elif char == '&':
                nova_linha += 'e'
            elif char == '!':
                nova_linha += 'i'
            elif char == '*':
                nova_linha += 'o'
            elif char == '#':
                nova_linha += 'u'
            else:
                nova_linha += char
        for item in nova_linha:
            print(item, end='')