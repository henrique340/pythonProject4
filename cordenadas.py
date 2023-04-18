# Parte A - Plano cartesiano com origem translada


# biblioteca math python
import math

# Lê as coordenadas da origem transladada
x_origem, y_origem = map(int, input("Digite as coordenadas X Y da origem transladada:").split())

# Lê a quantidade de pontos a serem processados
npontos = int(input("Digite a quantidade de pontos a serem processados: "))

# Cria as variáveis para contagem de pontos em cada quadrante e de menor e maior distância
quadrante1 = quadrante2 = quadrante3 = quadrante4 = 0
ponto_menor_distancia = (0, 0)
ponto_maior_distancia = (0, 0)
menor_distancia = float('Inf')  # https://stackoverflow.com/questions/34264710/what-is-the-point-of-floatinf-in-python
maior_distancia = 0


# formula para calcular a distância entre dois pontos da geomatria analitica   /  dAB² = (xB – xA)² + (yB – yA)².
def distancia(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# results = []
# FOR com range npontos que verifica cada ponto requisitado
for i in range(npontos):
    # coordenadas do(s) ponto(s)
    x_ponto = int(input(f"Digite a coordenada X do ponto {i + 1} :"))
    y_ponto = int(input(f"Digite a coordenada Y do ponto {i + 1} :"))

    # Calcula a distância do ponto em relação à origem transladada
    distvalue = distancia(x_origem, y_origem, x_ponto, y_ponto)

    # Verifica em qual quadrante o ponto se encontra ou se está sobre um dos eixos em relacao a origem transladada:
    if x_ponto > x_origem and y_ponto > y_origem:
        print("Ponto ({},{}) está no 1º quadrante.".format(x_ponto, y_ponto))
        quadrante1 += 1
    elif x_ponto < x_origem and y_ponto > y_origem:
        print("Ponto ({},{}) está no 2º quadrante.".format(x_ponto, y_ponto))
        quadrante2 += 1
    elif x_ponto < x_origem and y_ponto < y_origem:
        print("Ponto ({},{}) está no 3º quadrante.".format(x_ponto, y_ponto))
        quadrante3 += 1
    elif x_ponto > x_origem and y_ponto < y_origem:
        print("Ponto ({},{}) está no 4º quadrante.".format(x_ponto, y_ponto))
        quadrante4 += 1
    else:
        print("sobre o eixo de coordenadas.")

    # Verifica se o ponto tem a menor distância até a origem transladada
    if distvalue < menor_distancia:
        ponto_menor_distancia = (x_ponto, y_ponto)
        menor_distancia = distvalue

    # Verifica se o ponto tem a maior distância até a origem transladada
    if distvalue > maior_distancia:
        ponto_maior_distancia = (x_ponto, y_ponto)
        maior_distancia = distvalue

# Imprime o total de coordenadas com as estatisticas solicitadas
print("Ponto", ponto_menor_distancia, "eh o mais proximo, distancia=", "{:.2f}".format(menor_distancia), ".")
print("Ponto", ponto_maior_distancia, "eh o mais distante, distancia=", "{:.2f}".format(maior_distancia), ".")
print("Existe(m) ", quadrante1, "ponto(s) no 1º quadrante;", quadrante2, "no 2º quadrante;", quadrante3,
      "no 3º quadrante e", quadrante4, "ponto(s) no 4º quadrante.")

# Parte B - robô
# coordenadas X / Y do ponto de inicio do robo
xrobo = int(input("\nDigite a coordenada X do ponto de origem A do robô:"))
yrobo = int(input("Digite a coordenada Y do ponto de origem A do robô:"))

# tempo de caminhada
tempo = int(input("Digite por quanto tempo o robô irá caminhar:"))

# cria as variáveis para movimento
movimento_x = 0
movimento_y = 0
unidade = 1

# Movendo o robô com o tempo declarado
for i in range(tempo):
    if unidade == 1:
        movimento_y += 1
        unidade = 2
    elif unidade == 2:
        movimento_x += 1
        unidade = 3
    elif unidade == 3:
        movimento_x += 1
        unidade = 1

# Imprimindo as coordenadas finais
print("Resposta: ao final da caminhada o robô estará no ponto (", xrobo + movimento_x, ",", yrobo + movimento_y,
      ") do plano cartesiano.")