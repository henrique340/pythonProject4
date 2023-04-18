alfabeto = 'abcdefghijklmnopqrstuvwxyz'


cifra = input()
texto = input()

message = ''

for item in texto:
    message += alfabeto[cifra.index(item)]

print(message)