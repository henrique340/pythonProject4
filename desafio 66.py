c = soma = 0
while True:
    n = int(input('digite um número ou [999] para parar: '))
    if n == 999:
        break
    c += 1
    soma += n
print(f'você escreveu {c} números e a soma deles é {soma}')