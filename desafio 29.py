n = int(input('digite a velocidade do carro: '))
n1 = n-80
multa = 7*n1
if n>80:
    print('a velocidade limite é de 80km/h e você está rodando a {} km/h acima do limite sua multa será de R${},00'.format(n1, multa))
