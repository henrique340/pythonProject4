frase = input('')
frase = frase.strip('')
c = 0
nova_frase = " "
for c in range(0, len(frase)+1):
    if frase[c] == ' ':
        nova_frase += ' '
    elif c%2 == 0:
        nova_frase += frase[c].upper()
    else:
        nova_frase += frase[c].lower()
print(nova_frase)